# import cv2
# import numpy as np

# img = cv2.imread('C:\\Users\\Peter\\Documents\\COURSES\EMBEDDED SYSTEMS\\Term 3\\Practice_1\\lena_resized.jpg', 0)

# # Define kernel for morphological operations
# kernel = np.ones((5,5), np.uint8)

# # Apply erosion
# erosion = cv2.erode(img, kernel, iterations=1)

# # Apply dilation
# dilation = cv2.dilate(img, kernel, iterations=1)

# # Display the results
# cv2.imshow('Original Image', img)
# cv2.imshow('Erosion', erosion)
# cv2.imshow('Dilation', dilation)

# cv2.waitKey(0)

import cv2

# Read the image.
img = cv2.imread("C:\\Users\\Peter\\Documents\\COURSES\EMBEDDED SYSTEMS\\Term 3\\Practice_1\\lena_resized.jpg")

# Convert the image to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a structuring element.
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13))

# Erode the image.
eroded = cv2.erode(gray, kernel)

# Dilate the image.
dilated = cv2.dilate(eroded, kernel)

# Display the image.
cv2.imshow("Eroded Image", eroded)
cv2.imshow("Dilated Image", dilated)
cv2.waitKey(0)
