import cv2

#read the image
img= cv2.imread('photo.jpg')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original Image', img)
cv2.imshow('Gray Scale image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()