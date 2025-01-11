
import cv2

def applyFilter(image, filterType):
    
    # Create copy of the original image to avoid modifying the original one 
    filterImage = image.copy()

    if filterType == "sobel":
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelX = cv2.Sobel(grayImage, cv2.CV_64F, 1, 0, ksize=3)
        sobelY = cv2.Sobel(grayImage, cv2.CV_64F, 0, 1, ksize=3)

        combinedSobel = cv2.bitwise_or(sobelX.astype("uint8"), sobelY.astype("uint8"))
        filterImage = cv2.cvtColor(combinedSobel, cv2.COLOR_GRAY2BGR)

    elif filterType == "canny":
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(grayImage, 100, 200)
        filterImage = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    elif filterType == "red_tint":
        filterImage[:, :, 0] = 0 # Blue channel into zero
        filterImage[:, :, 1] = 0 # Green channel into zero

    elif filterType == "blue_tint":
        filterImage[:, :, 1] = 0 # Green channel into zero
        filterImage[:, :, 2] = 0 # Red channel into zero

    elif filterType == "green_tint":
        filterImage[:, :, 0] = 0 # Blue channel into zero
        filterImage[:, :, 2] = 0 # Red channel into zero

    elif filterType == "increase_red":
        filterImage[:, :, 2] = cv2.add(filterImage[:, :, 2], 50) # Increase red hue by 50
    elif filterType == "increase_blue":
        filterImage[:, :, 0] = cv2.add(filterImage[:, :, 0], 50) # Increase blue hue by 50
    elif filterType == "increase_green":
        filterImage[:, :, 1] = cv2.add(filterImage[:, :, 1], 50) # Increase green hue by 50

    elif filterType == "decrease_red":
        filterImage[:, :, 2] = cv2.subtract(filterImage[:, :, 2], 50) # Decrease red hue by 50
    elif filterType == "decrease_blue":
        filterImage[:, :, 0] = cv2.subtract(filterImage[:, :, 0], 50) # Decrease blue hue by 50
    elif filterType == "decrease_green":
        filterImage[:, :, 1] = cv2.subtract(filterImage[:, :, 1], 50) # Decrease green hue by 50

    elif filterType == "original":
        filterImage = image.copy()

    return filterImage

# Laod the image
image = cv2.imread("lesson-14/example.jpg") 

if image is None:
    print("Error: Image not found")
else:
    filterType = "original" # Default filter type

print("Press the following keys to apply filters:")
print("R = Red Tint")
print("B = Blue Tint")
print("G = Green Tint")

print("S = Sobel Edge Detection")
print("C = Canny Edge Detection")

print("I = Increase red intensity")
print("Y = Increase blue intensity")
print("A = Increase green intensity")

print("D = Decrease red intensity")
print("P = Decrease blue intensity")
print("H = Decrease green intensity")
print("Q = Quit")

while True:

    # Apply the selected filter
    filteredImage = applyFilter(image, filterType) 

    cv2.imshow("Filtered Image", filteredImage) # Display the Filtered Image

    # Wait for keypress
    key = cv2.waitKey(0)
    if key == ord("r"):
        filterType = "red_tint"
    elif key == ord("b"):
        filterType = "blue_tint"
    elif key == ord("g"):
        filterType = "green_tint"

    elif key == ord("s"):
        filterType = "sobel"
    elif key == ord("c"):
        filterType = "canny"

    elif key == ord("i"):
        filterType = "increase_red"
    elif key == ord("y"):
        filterType = "increase_blue"
    elif key == ord("a"):
        filterType = "increase_green"

    elif key == ord("d"):
        filterType = "decrease_red"
    elif key == ord("p"):
        filterType = "decrease_blue"
    elif key == ord("h"):
        filterType = "decrease_green"
    
    elif key == ord("o"):
        filterType = "original"
    elif key == ord("q"):
        print("Exiting..")
        break
    else: 
        print("Error: Invalid key, please use 'r', 'b', 'g', 's', 'c', 'i', 'y', 'a', 'd', 'p', 'h' or 'q' ")

cv2.destroyAllWindows()
