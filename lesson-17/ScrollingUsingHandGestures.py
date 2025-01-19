
import cv2
import mediapipe as mp
import pyautogui
import time

# Parameters configuration
scrollSpeed = 300 # Positive for scroll up, negative value for scroll down

# Delay between consecutive scroll actions to prevent rapid scrolling
scrollDelay = 1

# Camera Setting
cameraWidth = 640
cameraHeight = 480

# Initalize Mediapipe hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mpDraw = mp.solutions.drawing_utils 

# Gesture Detector Function
def detectGesture(handLandmarks, handedness): 
    
    """
    Hand landmarks is whether the hand gesture 
    is an open palm or close fist.

    Handedness means left or right hand
    """

    # List to hold status of each finger, 1 is up, 0 is down
    fingers = []

    # Define fingertip Landmarks
    fingerTipID = [
        mpHands.HandLandmark.INDEX_FINGER_TIP, 
        mpHands.HandLandmark.MIDDLE_FINGER_TIP,
        mpHands.HandLandmark.RING_FINGER_TIP,
        mpHands.HandLandmark.PINKY_TIP
    ]

    # Retrieve Nesscary Landmarks
    thumbTip = handLandmarks.landmark[mpHands.HandLandmark.THUMB_TIP]

    thumbIP = handLandmarks.landmark[mpHands.HandLandmark.THUMB_IP] 

    # Check each finger except thumb to see if it is up
    for tipID in fingerTipID:
        fingerTip = handLandmarks.landmark[tipID]
        fingerPIP = handLandmarks.landmark[tipID - 2]

        if fingerTip.y < fingerPIP.y:
            fingers.append(1) # Finger is up
        else: 
            fingers.append(0) # Finger is down 

    if handedness == "Right": 
        if thumbTip.x > thumbIP.x:
            fingers.append(1) # Thumb is open
        else:
            fingers.append(0) # Thumb is closed

    else:
        if thumbTip.x < thumbIP.x:
            fingers.append(1) # Thumb is open
        else:
            fingers.append(0)

    # Total number of fingers up
    totalFingers = fingers.count(1) 

    # Determine gesture based on number of fingers up
    if totalFingers == 5:
        return "scroll_up" 
    elif totalFingers == 0:
        return "scroll_down"
    else: 
        return "none"

def main():

    # Initalize Webcam
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, cameraWidth)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, cameraHeight)

    if not capture.isOpened():
        print("Error: could not open webcame")
        return

    ptime = 0 # Previous time for fps calculation
    lastScrollTime = 0 # Time stamp of the last scroll action

    print("Hand Gesture Scroll Control is running") 
    print("Show an open palm to scroll up")
    print("Make a fist to scroll down")
    print("Press 'q' to exit")

    while True:
        success, image = capture.read()
        if not success:
            print("Failed to capture image")
            break

        image = cv2.flip(image, 1) # Flip image for mirror effect 
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = hands.process(imageRGB)

        gesture = "none"
        handedness = "unknown"

        if result.multi_hand_landmarks and result.multi_handedness:
            for handlandmarks, handinfo in zip(result.multi_hand_landmarks, result.multi_handedness):
                # Get hand label, left or right
                handednessLabel = handinfo.classification[0].label
                handedness = handednessLabel

                # Draw hand landmarks on the image
                mpDraw.draw_landmarks(
                    image, handlandmarks, mpHands.HAND_CONNECTIONS, 
                    mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2), 
                    mpDraw.DrawingSpec(color=(0, 0, 255), thickness=2)
                ) 

                # Detect the gesture
                gesture = detectGesture(handlandmarks, handedness) 

                # Get Current Time
                currentTime = time.time()

                # Perform scrolling action based on gesture with delay
                if gesture == "scroll_up" and (currentTime - lastScrollTime) > scrollDelay:
                    pyautogui.scroll(scrollSpeed)
                    lastScrollTime = currentTime
                elif gesture == "scroll_down" and (currentTime - lastScrollTime) > scrollDelay:
                    pyautogui.scroll(-scrollSpeed)
                    lastScrollTime = currentTime
        
        # Calculate frames per second (fps)
        ctime = time.time() 
        fps = 1 / (ctime - ptime) if (ctime - ptime) > 0 else 0
        ptime = ctime

        # Display gesture and fps on the image
        cv2.putText(image, f"Gesture = {gesture}", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2) 
        cv2.putText(image, f"Frames per second = {int(fps)}", (10, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2) 
        cv2.putText(image, f"Hand = {handedness}", (10, 130), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2) 

        cv2.imshow("Hand Gesture Scroll Control", image) 

        # Exit the loop when 'q' is pressed 
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
