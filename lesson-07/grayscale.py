
import cv2

# Load the image
image = cv2.imread("lesson-07/example.jpg")

# Convert the image into grayscale
greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize grayscale image into 224 x 224
resizeImage = cv2.resize(greyImage, (224, 224))

# Display the resized grayscale image
cv2.imshow("Processed Image", resizeImage)

# Wait for any keypress
key = cv2.waitKey(0) 

# Check if the 's' key was pressed
if key == ord("s"):

    # Save the processed image when 's' is pressed
    cv2.imwrite("grayscaleResizedImage.jpg", resizeImage)
    print("Image saved as grayscaleResizedImage.jpg")

else: 
    print("Image not saved")

# Close window
cv2.destroyAllWindows()

# Print Processed image properties
print(f"Processed image dimensions: {resizeImage.shape}")
