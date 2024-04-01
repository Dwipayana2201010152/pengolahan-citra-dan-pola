import cv2

#Menyimpan gambar dengan fungsi imread dari OpenCV
img = cv2.imread("SLL.jpg")

#konversi BGR dari variable img ke colorspace HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);

#memisahkan hue, saturation dan value
h, s, v = cv2.split(hsv)

#menampilkan band hue
cv2.imshow('HSV', hsv)
cv2.imshow('Didok', img)
cv2.waitKey(0)


