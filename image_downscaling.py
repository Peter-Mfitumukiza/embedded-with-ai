import cv2
img = cv2.imread('C:\\Users\\Peter\\Documents\\COURSES\EMBEDDED SYSTEMS\\Term 3\\Practice_1\\lena_resized.jpg', cv2.IMREAD_UNCHANGED)
print('Original Dimensions : ',img.shape)
scale_percent = 30 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Save resized image
cv2.imwrite("C:\\Users\\Peter\\Documents\\COURSES\EMBEDDED SYSTEMS\\Term 3\\Practice_1\\images\\capA1-01.jpg", resized)

print('Resized Dimensions : ',resized.shape)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()