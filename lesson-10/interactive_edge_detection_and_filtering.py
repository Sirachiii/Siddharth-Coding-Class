
import cv2
import numpy as np
import matplotlib.pyplot as plt

def displayImage(title, image):
    plt.figure(figsize=(8, 8))

    if len(image.shape) == 2: # Grayscale Image
        plt.imshow(image, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.title(title)
    plt.axis("off")
    plt.show()

def interactiveEdgeDetection(imagePath):
    image = cv2.imread(imagePath)

    if image is None:
        print("Error: The image not found")
        return
    
    # Convert image to grayscale
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    displayImage("Original Grayscale Image", grayImage)

    print("Select an option: ")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing Filterting")
    print("5. Median Filtering")
    print("6. Exit")
    print()

    while True: 
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            sobelX = cv2.Sobel(grayImage, cv2.CV_64F, 1, 0, ksize=3)
            sobelY = cv2.Sobel(grayImage, cv2.CV_64F, 0, 1, ksize=3)
            combineSobel = cv2.bitwise_or(sobelX.astype(np.uint8), sobelY.astype(np.uint8))
            displayImage("Sobel Edge Detection", combineSobel)
        elif choice == 2:
            print("Adjust threshold for canny (It's default value is 100, 200): ")
            lowerThreshold = int(input("Enter lower threshold: "))
            upperThreshold = int(input("Enter upper threshold: "))
            cannyEdge = cv2.Canny(grayImage, lowerThreshold, upperThreshold)
            displayImage("Canny Edge Detection", cannyEdge)
        elif choice == 3: 
            laplacianEdge = cv2.Laplacian(grayImage, cv2.CV_64F)
            displayImage("Laplacian Edge Detection", np.abs(laplacianEdge).astype(np.uint8))
        elif choice == 4:
            print("Adjust kernel size for gaussian blur (must be odd number, default=5) ")
            kernelSize = int(input("Enter Kernel Size (odd number): "))
            gaussianBlur = cv2.GaussianBlur(image, (kernelSize, kernelSize), 0)
            displayImage("Gaussian Smooth Image", gaussianBlur)
        elif choice == 5:
            print("Adjust kernel size for median filtering (must be odd number, default=5)")
            kernelSize = int(input("Enter kernel size (odd number): "))
            medianFilter = cv2.medianBlur(image, kernelSize)
            displayImage("Median Filter image", medianFilter)
        elif choice == 6:
            print("Exiting")
            break
        else:
            print("Invalid Choice: please select a value between 1 and 6")

interactiveEdgeDetection("lesson-10/example.jpg")