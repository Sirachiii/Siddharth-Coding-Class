
# Imports
import cv2
import numpy as np
import matplotlib.pyplot as plt 

# Load Image
image = cv2.imread("lesson-08/example2.jpg")

# Convert to Grayscale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display Grayscale
plt.imshow(grayImage, cmap="gray")
plt.title("Grayscale Image")
plt.show()

# Crop Image
croppedImage = image[100:300, 200:400]

# Image Dimensions for rotation
(h, w) = image.shape[:2]
center = (w//2, h//2)

# Rotate image by 65 degrees
n = cv2.getRotationMatrix2D(center, 65, 1.0)
rotate = cv2.warpAffine(image, n, (w, h))

# Convert rotated image from BGR to RGB
rotateRGB = cv2.cvtColor(rotate, cv2.COLOR_BGR2RGB) 

# Adjust Brightness
brightnessMatrix = np.ones(image.shape, dtype="uint8") * 50
brighterImage = cv2.add(image, brightnessMatrix)

# Save Image
cv2.imwrite(f"editedImage.jpg", brighterImage) # Save image

# Explanation / Documentation
"""
In this project, I converted an image to 
grayscale, cropped it, rotated it by 
50 degrees, and adjusted its brightness.
"""
