import cv2

# Read the image.
img = cv2.imread("C:\\Users\\Peter\\Documents\\COURSES\EMBEDDED SYSTEMS\\Term 3\\Practice_1\\lena_resized.jpg")

# Convert the image to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the image.
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply the Canny edge detector to the image.
edges = cv2.Canny(blur, 100, 200)

# Display the edges.
cv2.imshow("Edges", edges)
cv2.waitKey(0)
