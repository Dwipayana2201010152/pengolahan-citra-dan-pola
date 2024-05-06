import cv2
from cv2 import waitKey
import numpy as np

img = cv2.imread("waifu.png")
cv2.imshow('Gambar Asli',img)
H, W = img.shape[:2]

degree = 90
rotationMatrix = cv2.getRotationMatrix2D((W / 2, H / 2), degree, 1)
#untuk memposisikan gambar pada titik 0,0
# cos = np.abs(rotationMatrix[0, 0])
# sin = np.abs(rotationMatrix[0, 1])
# print(cos, sin, rotationMatrix[0, 0])
# nW = int((H * sin) + (W * cos))
# nH = int((H * cos) + (W * sin))
# rotationMatrix[0, 2] += (nW / 2) - W / 2
# rotationMatrix[1, 2] += (nH / 2) - H / 2
rot_image = cv2.warpAffine(img, rotationMatrix, (H,W))

M = np.float32([[1,0,100],[0,1,50]])
hasil = cv2.warpAffine(img,M,(W,H))
cv2.imshow('Gambar Hasil', rot_image)
cv2.imshow('Gambar Asli', img)
cv2.imshow('Hasil Translasi', hasil)

waitKey(0)