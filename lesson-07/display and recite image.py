
import cv2 

image = cv2.imread("example.jpg")

cv2.namedWindow("loadedImage", cv2.WINDOW_NORMAL) # Create resizeable window
cv2.resizeWindow("loadedImage", 800, 500) # Window is 800x500

# Display the image in the resized window
cv2.imshow("loadedImage", image) 
cv2.waitKey(0) # Wait for keypress
cv2.destroyAllWindows() # Close the window

# Print image properties
print(f"Image dimension = {image.shape}")
