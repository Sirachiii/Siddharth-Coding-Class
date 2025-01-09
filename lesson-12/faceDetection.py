
import cv2
import cv2.data

# Load the pre-trained Haar cascade Classifer for face detection
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start video capture from default camera
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error: Could not open the camera")
    exit()

while True:
    # Capture frame by frame
    read, frame = capture.read()

    # If frame is read correctly the read status will be true
    if not read:
        print("Error: Failed to capture image")
        break

    # Convert frame to grayscale because face detection works better on grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecting face in the grayscale motion picture
    face = faceCascade.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangle around the face
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2) # Red Rectangle with thickness 2

    # Display resulting frame
    cv2.imshow("Face Detection - Press 'q' for quit", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 

# Release the captured image and close any open windows
capture.release()
cv2.destroyAllWindows()
