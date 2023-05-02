import numpy as np
import cv2
image = cv2.imread('C:\\Users\\Peter\\Documents\\COURSES\EMBEDDED SYSTEMS\\Term 3\\Practice_1\\lena_resized.jpg')
y=200
x=220
h=190
w=150
cropped = image[y:y+h, x:x+w]

# Save cropped image
cv2.imwrite("C:\\Users\\Peter\\Documents\\COURSES\EMBEDDED SYSTEMS\\Term 3\\Practice_1\\lena_cropped.jpg", cropped)

cv2.imshow('Lena Cropped', cropped)
cv2.waitKey(0)