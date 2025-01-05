
import cv2

def applyColourFilter(image, filterType):
    filterImage = image.copy() # Create a copy of the image to avoid modifing the original picture

    if filterType == "red_tint":
        filterImage[:, :, 1] = 0 # Green channel to zero
        filterImage[:, :, 0] = 0 # Blue channel to zero
    elif filterType == "blue_tint":
        filterImage[:, :, 1] = 0 # Green channel to zero
        filterImage[:, :, 2] = 0 # Red channel to zero
    elif filterType == "green_tint":
        filterImage[:, :, 0] = 0 # Blue channel to zero
        filterImage[:, :, 2] = 0 # Red channel to zero

    elif filterType == "increase_red": 
        # Increase the intensity of the red channel 
        filterImage[:, :, 2] = cv2.add(filterImage[:, :, 2], 50)
    elif filterType == "increase_blue": 
        # Increase the intensity of the blue channel 
        filterImage[:, :, 0] = cv2.add(filterImage[:, :, 0], 50)
    elif filterType == "increase_green": 
        # Increase the intensity of the green channel 
        filterImage[:, :, 1] = cv2.add(filterImage[:, :, 1], 50)
    
    elif filterType == "decrease_blue":
        # Decrease the intensity of the blue channel 
        filterImage[:, :, 0] = cv2.subtract(filterImage[:, :, 0], 50)
    elif filterType == "decrease_red":
        # Decrease the intensity of the red channel 
        filterImage[:, :, 2] = cv2.subtract(filterImage[:, :, 2], 50)
    elif filterType == "decrease_green":
        # Decrease the intensity of the green channel 
        filterImage[:, :, 1] = cv2.subtract(filterImage[:, :, 1], 50)
    
    return filterImage

# Load the Image
image = cv2.imread("lesson-11/example.jpg")

if image is None:
    print("Error: Image not found!")
else:
    # Setting the default filter type
    filterType = "original"

print("Press the following keys to apply filters")
print("r : red tint")
print("b : blue tint")
print("g : green tint")

print("i : increase red intensity")
print("y : increase green intensity")
print("u : increase blue intensity")

print("d : decrease blue intensity")
print("f : decrease green intensity")
print("c : decrease red intensity")

print("q : quit")
print()

while True:
    filterImage = applyColourFilter(image, filterType)

    # Display the filtered image
    cv2.imshow("Filtered Image", filterImage)

    # Waiting for keypress
    key = cv2.waitKey(0)

    if key == ord("r"):
        filterType = "red_tint"
    elif key == ord("b"):
        filterType = "blue_tint"
    elif key == ord("g"):
        filterType = "green_tint"

    elif key == ord("i"):
        filterType = "increase_red"
    elif key == ord("y"):
        filterType = "increase_green"
    elif key == ord("u"):
        filterType = "increase_blue"

    elif key == ord("d"):
        filterType = "decrease_blue"
    elif key == ord("f"):
        filterType = "decrease_green"
    elif key == ord("c"):
        filterType = "decrease_red"

    elif key == ord("q"):
        print("Exiting")
        break
    else:
        print("Invalid keys, please use 'r', 'g', 'b', 'i', 'd', 'q' ")

cv2.destroyAllWindows()