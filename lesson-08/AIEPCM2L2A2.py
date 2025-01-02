
#  Rotating and Adjusting Brightness
import cv2
import numpy as np
import matplotlib.pyplot as plt 

image = cv2.imread("lesson-08/example2.jpg")
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Rotate the image by 45 degrees around its center
(h, w) = image.shape[:2]
center = (w//2, h//2)

# rotate by 45 degrees
n = cv2.getRotationMatrix2D(center, 45, 1.0)
rotate = cv2.warpAffine(image, n, (w, h))

# Convert rotated image from BGR to RGB
rotateRGB = cv2.cvtColor(rotate, cv2.COLOR_BGR2RGB)
plt.imshow(rotateRGB)
plt.title("Rotated image")
plt.show()

# Increase brightness by adding 50 to all pixel values
# Use cv2.add to avoid negative values or overflow
brightnessMatrix = np.ones(image.shape, dtype="uint8") * 50
brighterImage = cv2.add(image, brightnessMatrix)

# Convert brighter image from BGR to RGB
RGBImage = cv2.cvtColor(brighterImage, cv2.COLOR_BGR2RGB)
plt.imshow(RGBImage)
plt.title("Brighter image RGB")
plt.show()
