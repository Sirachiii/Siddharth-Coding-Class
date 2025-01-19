
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
capture = cv2.VideoCapture() 
