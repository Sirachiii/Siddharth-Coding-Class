
# /////////////////////////////////////////////////////////// #

import cv2

# load image
image = cv2.imread("lesson-07/example.jpg")

# Image Sizes
sizes = {
    'Small': (200, 200),
    'Medium': (400, 400),
    'Large': (600, 600)
}

# Resize Images
for size, dimensions in sizes.items(): 
    newSize = cv2.resize(image, dimensions) # Resizing
    cv2.imshow(f"{size} Image", newSize) # Display Image
    cv2.imwrite(f"input_image_{size}.jpg", newSize) # Save image

cv2.waitKey(0) # Wait for keypress
cv2.destroyAllWindows() # Close all windows
print("Project completed successfully.")

# /////////////////////////////////////////////////////////// #
