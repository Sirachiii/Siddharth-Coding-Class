
import cv2
import numpy as np

# Setup the webcam capture
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:

    # Capture motion picture frame by frame
    read, frame = capture.read()

    if not read:
        print("Error: Failed to capture image")
        break
    
    # Convert to HSV for colour filtering
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range for skin colour in HSV
    lowerSkin = np.array([0, 20, 70], dtype=np.uint8)
    upperskin = np.array([20, 255, 255], dtype=np.uint8)

    # Create a mask to detect skin colour
    mask = cv2.inRange(hsv, lowerSkin, upperskin)

    # Apply the mask to the frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours of hand shape in the mask image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    # Draw the contours where the contours are found
    if contours: 

        # Get the largest contour
        maxCountour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(maxCountour) > 500: # Ignore small contours
            # Draw a square around the detected hand
            x, y, w, h = cv2.boundingRect(maxCountour) 
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # Draw green rectangle with thickness 2

            # Get the center of the hand shape for further tracking or interaction
            centerX = int(x + w / 2)
            centerY = int(y + h / 2)
            cv2.circle(frame, (centerX, centerY), 5, (0, 0, 255), -1) # Red Dot at the center

    # Displaying the original and result frames
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Filtered Frame", result)

    # break the loops when q key is pressed for quitting
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release captured motion picture and close the window
capture.release()
cv2.destroyAllWindows()

