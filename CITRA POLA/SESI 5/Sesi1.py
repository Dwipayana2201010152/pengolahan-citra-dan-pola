import cv2

img1 = cv2.imread("Kotak.jpeg")
print(img1.shape)
print(img1.dtype)

img2 = cv2.imread("Bundar.jpeg")
print(img2.shape)
print(img2.dtype)


#Resize
width = 300
height = 300
dim = (width, height)

img1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA)
img2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

#grayScalling
imgray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 
imgray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) 

#Konversu ke Citra Biner
ret, bw1 = cv2.threshold(imgray1, 125, 255, cv2.THRESH_BINARY)
ret, bw2 = cv2.threshold(imgray2, 125, 255, cv2.THRESH_BINARY)

op_and = cv2.bitwise_and(bw1, bw2)
op_or = cv2.bitwise_or(bw1, bw2)


cv2.imshow('Img 1', img1)
cv2.imshow('Img 2', img2)
cv2.imshow('Hasil And', op_and)
cv2.imshow('Hasil Or', op_or)
cv2.waitKey()