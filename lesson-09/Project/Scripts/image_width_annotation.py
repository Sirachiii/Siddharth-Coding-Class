
import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("lesson-09/Project/Original_images/example.jpg") 

# Convert BGR to RGB for correct color display with matplotlib
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, _ = imageRGB.shape 

# Bi-Directional Arrows
# Top Right
heightArrowStart = (width - 50, 20)
# Bottom right
heightArrowEnd = (width - 50, height - 20) 
# bottom-left
widthArrowStart = (20, height - 50)
# bottom-right
widthArrowEnd = (width - 20, height - 50)

# Vertical arrow
cv2.arrowedLine(imageRGB, heightArrowStart, heightArrowEnd, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(imageRGB, heightArrowEnd, heightArrowStart, (255, 255, 0), 3, tipLength=0.05)
# Horizontal arrow
cv2.arrowedLine(imageRGB, widthArrowStart, widthArrowEnd, (0, 255, 255), 3, tipLength=0.05)
cv2.arrowedLine(imageRGB, widthArrowEnd, widthArrowStart, (0, 255, 255), 3, tipLength=0.05)

# Load Font
font = cv2.FONT_HERSHEY_PLAIN 

# Annotate the width value using Text
widthLabelPosition = ((widthArrowStart[0] + widthArrowEnd[0]) // 2, widthArrowStart[1] + 30) 
cv2.putText(imageRGB, f"Width = {width}px", widthLabelPosition, font, 2.0, (255, 255, 255), 2, cv2.LINE_AA)

# Annotate the height value using Text
heightLabelPosition = (heightArrowStart[0] - 300, (heightArrowStart[1] + heightArrowEnd[1]) // 2)
cv2.putText(imageRGB, f"Height = {height}px", heightLabelPosition, font, 2.0, (255, 255, 255), 2, cv2.LINE_AA)

# Save image
cv2.imwrite(r"lesson-09/Project/Output_images/editedImage.jpg", imageRGB) 

# Display the Annotated Image
plt.figure(figsize=(12, 8))
plt.imshow(imageRGB)
plt.title("Annotated Image with bi-directional arrows")
plt.axis("off")
plt.show()
