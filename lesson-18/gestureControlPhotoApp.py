
import cv2
import mediapipe as mp
import time 
import numpy as np

# Initilaize mediapipe hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mpDraw = mp.solutions.drawing_utils 

filters = [
    None,
    "grayscale", 
    "sepia",
    "negative", 
    "blur"  
]

currentFilter = 0 # Starting filter

# Webcam setup
capture = cv2.VideoCapture(0) 

if not capture.isOpened():
    print("Error: Could not access the webcam")
    exit()

# Time stamp for the debouncing gestures
lastActionTime = 0
debounceTime = 1

def applyFilter(frame, filterType):
    
    if filterType == "grayscale":
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    elif filterType == "sepia":
        sepiaFilter = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
        sepiaFrame = cv2.transform(frame, sepiaFilter) 
        sepiaFrame = np.clip(sepiaFrame, 0, 255) # Clip values to ensure valid range 
        return sepiaFrame.astype(np.uint8)
    
    elif filterType == "negative":
        return cv2.bitwise_not(frame) 

    elif filterType == "blur":
        return cv2.GaussianBlur(frame, (15, 15), 0) 
     
    return frame

while True:

    success, image = capture.read()
    if not success:
        print("Error: failed to read frame from webcam")
        break

    image = cv2.flip(image, 1) # Flip the image for mirror effect
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(imageRGB)

    if result.multi_hand_landmarks:
        for handLandmark in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(image, handLandmark, mpHands.HAND_CONNECTIONS) 

            # Get the key landmarks
            thumbTip = handLandmark.landmark[mpHands.HandLandmark.THUMB_TIP]
            indexTip = handLandmark.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
            middleTip = handLandmark.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP]
            ringTip = handLandmark.landmark[mpHands.HandLandmark.RING_FINGER_TIP]
            pinkyTip = handLandmark.landmark[mpHands.HandLandmark.PINKY_TIP]

            # Frame Dimension 
            frameHeight, frameWidth, _ = image.shape 

            # Convert normalise coordinates into pixel coordinates
            thumbX, thumbY = int(thumbTip.x * frameWidth), int(thumbTip.y * frameHeight)
            indexX, indexY = int(indexTip.x * frameWidth), int(indexTip.y * frameHeight)
            middleX, middleY = int(middleTip.x * frameWidth), int(middleTip.y * frameHeight)
            ringX, ringY = int(ringTip.x * frameWidth), int(ringTip.y * frameHeight)
            pinkyX, pinkyY = int(pinkyTip.x * frameWidth), int(pinkyTip.y * frameHeight)

            # Draw Circles for landmarks
            cv2.circle(image, (thumbX, thumbY), 10, (255, 0, 0), cv2.FILLED) 
            cv2.circle(image, (indexX, indexY), 10, (0, 255, 0), cv2.FILLED) 
            cv2.circle(image, (middleX, middleY), 10, (0, 0, 255), cv2.FILLED) 
            cv2.circle(image, (ringX, ringY), 10, (255, 255, 0), cv2.FILLED) 
            cv2.circle(image, (pinkyX, pinkyY), 10, (255, 0, 255), cv2.FILLED)

            # Gesture Logic
            currentTime = time.time()
             
            # Taking Picture: Thumb Touches index finger
            if abs(thumbX - indexX) < 30 and abs(thumbY - indexY) < 30:
                if currentTime - lastActionTime > debounceTime:
                    cv2.putText(image, "Picture Captured", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2) 
                    lastActionTime = currentTime
                    cv2.imwrite(f"lesson-18/Picture_{int(time.time())}.jpg", image)
                    print("Picture Saved")

            # Change Filter: Thumb touches any other finger 
            elif (abs(thumbX - middleX) < 30 and abs(thumbY - middleY) < 30) or \
                 (abs(thumbX - ringX) < 30 and abs(thumbY - ringY) < 30) or \
                 (abs(thumbX - pinkyX) < 30 and abs(thumbY - pinkyY) < 30):

                if currentTime - lastActionTime > debounceTime:
                    currentFilter = (currentFilter + 1) % len(filters) 
                    lastActionTime = currentTime
                    print(f"Switched to filter = {filters[currentFilter]}") 
                
    # Apply the current filter
    filterImage = applyFilter(image, filters[currentFilter]) 

    # Display the output
    if filters[currentFilter] == "grayscale":
        cv2.imshow("Gesture Control Photo App", cv2.cvtColor(filterImage, cv2.COLOR_GRAY2BGR)) 
    else:
        cv2.imshow("Gesture Control Photo App", filterImage)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()    
