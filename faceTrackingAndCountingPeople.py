
import cv2
import cv2.data 

# Load the pretrained Haar cascade classifer for face detection
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start video capture from default camera
capture = cv2.VideoCapture(0)

# When unable to access the camera
if not capture.isOpened():
    print("Error: Could not open the camera")
    exit()

while True:
    # Capture motion picture frame by frame
    read, frame = capture.read()

    # When camera unable to capture image
    if not read:
        print("Error: failed to capture image")
        break

    # Convert frame to grayscale, because face detection works better on grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecting face in the grayscale image
    faces = faceCascade.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=5, minSize=(35, 35))

    # Draw rectangle/sqaure around face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1) # Blue Rectangle with thickness 1

    # Display the count of faces
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, f"People Count = {len(faces)} Persons", (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display resulting frame with face detection and people count
    cv2.imshow("Face Tracking and Counting - Press 'q' for quit", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the captured image, and close any open windows
capture.release()
cv2.destroyAllWindows()
