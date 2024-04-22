import cv2
import numpy as np
img = cv2.imread("jiso.jpg")
H, W = img.shape[:2]

gray = np.zeros((H, W), np.uint8)
for i in range(H):
    for j in range(W):
        #Perhatikan format gambar B,G,R
        gray[i,j]= np.clip(0.299 * img[i, j, 2] + 0.587 * img[i, j, 1] + 0.114 * img[i, j, 0], 0, 255)


img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
brightness = 50
h, w = img2.shape[:2]

for i in np.arange(h):
    for j in np.arange(w):
        a = img2.item(i, j)
        b = a + brightness
        
        if b > 255:
            b = 255
        elif b < 0:
            b =0
        else:
            b =b
        img2.itemset((i, j), b)

cv2.imshow("Gambar asli", img)
cv2.imshow("Greyscale", gray)
cv2.waitKey(0)