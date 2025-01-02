
# Color Conversions and Cropping
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("lesson-08/example2.jpg")

# Convert BGR to RGB
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(imageRGB)
plt.title("RGB Image")
plt.show()

# Convert to Grayscale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grayImage, cmap="gray")
plt.title("Grayscale Image")
plt.show()

# Cropping the image
# Assume we know the region we want: rows 100 to 300, columns 200 to 400
croppedImage = image[100:300, 200:400]

# Converting from BGR to RGB
cropRGB = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2RGB)
plt.imshow(cropRGB)
plt.title("Cropped RGB Image")
plt.show()

# Converting cropped image to grayscale
grayCroppedImage = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2GRAY)
plt.imshow(grayCroppedImage, cmap="gray")
plt.title("Cropped Grayscale Image")
plt.show()