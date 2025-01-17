
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

