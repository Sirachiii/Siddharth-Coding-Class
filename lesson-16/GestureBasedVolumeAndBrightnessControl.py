
import cv2
import mediapipe as mp 
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from math import hypot
import screen_brightness_control as sbc

# Initalize mediapipe hand
mpHands = mp.solutions.hands 
hands = mpHands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) 
mpDraw = mp.solutions.drawing_utils

# Pycaw for volume control
try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volumeRange = volume.GetVolumeRange()
    minimumVolume = volumeRange[0]
    maximumVolume = volumeRange[1]
except Exception as e:
    print(f"Error: Initalizing Pycaw {e}")
    exit()

# Webcame Setup 
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error: Could not access the web camera")
    exit()

while True:
    read, frame = capture.read()

    if not read: 
        print("Failed to capture image using webcam")
        break

    # Flip the image for a mirror effect 
    frame = cv2.flip(frame, 1) 

    # Convert from bgr to rgb standard colour
    imageRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(imageRGB) 

    if results.multi_hand_landmarks and results.multi_handedness:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            handLabel = results.multi_handedness[i].classification[0].label # Left or Right hand

            mpDraw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

            # Extract the tip of the thumb and index finger
            thumbTip = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP]
            indexTip = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]

            h, w, _ = frame.shape
            thumbPosition = (int(thumbTip.x * w), int(thumbTip.y * h))
            indexPosition = (int(indexTip.x * w), int(indexTip.y * h))

            # Draw circles at the tip
            cv2.circle(frame, thumbPosition, 10, (255, 0, 0), cv2.FILLED) 
            cv2.circle(frame, indexPosition, 10, (255, 0, 0), cv2.FILLED) 

            # Calculate the distance between thumb and index finger 
            distance = hypot(indexPosition[0] - thumbPosition[0], indexPosition[1] - thumbPosition[1])

            if handLabel == "Right": # Control volume with the right hand
                vol = np.interp(distance, [30, 300], [minimumVolume, maximumVolume])

                try:
                    volume.SetMasterVolumeLevel(vol, None)
                except Exception as e:
                    print(f"Error Adjusting Volume: {e}") 

                # Visual Feedback for volume
                volumeBar = np.interp(distance, [30, 300], [400, 150])

                cv2.rectangle(frame, (50, 150), (85, 400), (255, 0, 0), 2)
                cv2.rectangle(frame, (50, int(volumeBar)), (85, 400), (255, 0, 0), cv2.FILLED)
                cv2.putText(frame, f"Volume = {int(np.interp(distance, [30, 300], [0, 100]))}%", (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

            elif handLabel == "Left": # Control brightness with the left hand
                brightness = np.interp(distance, [30, 300], [0, 100])

                try:
                    sbc.set_brightness(brightness)
                except Exception as e:
                    print(f"Error Adjusting Brightness: {e}")

                # Visual Feeback for brightness
                brightnessBar = np.interp(distance, [30, 300], [400, 150])
                cv2.rectangle(frame, (100, 150), (135, 400), (0, 255, 0), 2)
                cv2.rectangle(frame, (100, int(brightnessBar)), (135, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, f"Brightness = {int(brightness)}%", (90, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
            
    # Show the video feed with annotations
    cv2.imshow("Gesture Volume and Brightness Controller", frame)

    # Break the loop is 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the captured motion picture and close all windows
capture.release()
cv2.destroyAllWindows()
