
import cv2
import matplotlib.pyplot as plt

# Step 1: Load the Image
# User-provided image path
image = cv2.imread("lesson-09/example.jpg") 

# Convert BGR to RGB for correct color display with matplotlib
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, _ = imageRGB.shape 

# Step 2: Draw Two Rectangles Around Interesting Regions
# Rectangle 1: Top-left corner
rectangle1Width = 150
rectangle1Height = 150 

# Fixed 20 pixels padding from top-left
topLeft1 = (20, 20)
bottomRight1 = (topLeft1[0] + rectangle1Width, topLeft1[1] + rectangle1Height) 

# Yellow rectangle
cv2.rectangle(imageRGB, topLeft1, bottomRight1, (0, 255, 255), 3)

# Rectangle 2: Bottom-right corner
rectangle2Width = 200
rectangle2Height = 150

# 20 pixels padding
topLeft2 = (width - rectangle2Width - 20, height - rectangle2Height - 20)
bottomRight2 = (topLeft2[0] + rectangle2Width, topLeft2[1] + rectangle2Height)

# Magenta rectangle
cv2.rectangle(imageRGB, topLeft2, bottomRight2, (255, 0, 255), 3)

# Step 3: Draw Circles at the Centers of Both Rectangles
center1x = topLeft1[0] + rectangle1Width // 2
center1y = topLeft1[1] + rectangle1Height // 2

center2x = topLeft2[0] + rectangle2Width // 2
center2y = topLeft2[1] + rectangle2Height // 2

# Filled green circle
cv2.circle(imageRGB, (center1x, center1y), 15, (0, 255, 0), -1)

# Filled red circle
cv2.circle(imageRGB, (center2x, center2y), 15, (0, 0, 255), -1)

# Step 4: Draw Connecting Lines Between Centers of Rectangles
cv2.line(imageRGB, (center1x, center1y), (center2x, center2y), (0, 255, 0), 3)

# Step 5: Add Text Labels for Regions and Centers
font = cv2.FONT_HERSHEY_PLAIN 
cv2.putText(imageRGB, "Region 1", (topLeft1[0], topLeft1[1] - 10), font, 0.7, (255, 0, 0), 2, cv2.LINE_AA) 
cv2.putText(imageRGB, "Region 2", (topLeft2[0], topLeft2[1] - 10), font, 0.7, (0, 255, 0), 2, cv2.LINE_AA) 
cv2.putText(imageRGB, "Center 1", (center1x - 40, center1y + 40), font, 0.6, (0, 0, 255), 2, cv2.LINE_AA) 
cv2.putText(imageRGB, "Center 2", (center2x - 40, center2y + 40), font, 0.6, (0, 255, 255), 2, cv2.LINE_AA) 

# Step 6: Add Bi-Directional Arrow Representing Height
# Start near the top-right
arrowStart = (width - 50, 20)
# End near the bottom-right
arrowEnd = (width - 50, height - 20) 

# Draw arrows in both directions
# Downward arrow
cv2.arrowedLine(imageRGB, arrowStart, arrowEnd, (255, 255, 0), 3, tipLength=0.05)
# Upward arrow
cv2.arrowedLine(imageRGB, arrowEnd, arrowStart, (255, 255, 0), 3, tipLength=0.05)

# Annotate the height value
heightLabelPosition = (arrowStart[0] - 150, (arrowStart[1] + arrowEnd[1]) // 2)
cv2.putText(imageRGB, f"Height = {height}px", heightLabelPosition, font, 0.8, (120, 0, 150), 2, cv2.LINE_AA)

# Step 7: Display the Annotated Image
plt.figure(figsize=(12, 8))
plt.imshow(imageRGB)
plt.title("Annotated Image with Regions, centers and bi-directional arrows")
plt.axis("off")
plt.show()
