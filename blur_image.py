import cv2

img = cv2.imread("C:\\Users\\Peter\\Documents\\COURSES\EMBEDDED SYSTEMS\\Term 3\\Practice_1\\lena_resized.jpg")
img_blur = cv2.GaussianBlur(img, (19,19), 0)

cv2.imshow("Blurred Image", img_blur)
cv2.waitKey(0)
