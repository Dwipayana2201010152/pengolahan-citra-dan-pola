# Memanggil Library opencv
import cv2
from cv2 import waitKey

img = cv2.imread("SLL.jpg")

print(img.shape)
print(img.size)
print(img.dtype)

#waitKey(0)

b, g, r = cv2.split(img)

b = img[...,0] 
g = img[...,1] 
r = img[...,2] 

cv2.imshow("Didok", img)
cv2.imshow("Biru", b)
cv2.imshow("Hijau", g)
cv2.imshow("Merah", r)
waitKey(0)




H, W = img.shape[:2]

degree = 90
rotationMatrix = cv2.get

#Untuk Memposisikan gambar pada titik 0
# cos = np.abs(rotationMatrix[0, 0])
# sin = np.abs(rotationMatrix[0, 1])
# print(cos, sin, rotationMatrix[0, 0])
# nW = int((H * sin) + (W * cos))
# nH = int((H * cos) + (W * sin))
# rotationMatrix[0, 2] += (nW / 2) - W / 2
# rotationMatrix[1, 2] += (nH / 2) - H / 2

rot_image = cv2.warpAffine(img, rotationMatrix, (H,W))
cv2.imshow('Gambar Hasil', rot_image)
waitKey(0)
