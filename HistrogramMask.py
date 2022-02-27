import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread("Figures/BlueColor.jpg",0)
# create a 2D mask matrix with all zero elements (Black area)
# This mask matrix has same dimension as the first 2-dimension of img

mask = np.zeros(img.shape[:2], np.uint8)
# create white area  with width = 300 pixel and height = 200 pixel
mask[100:300,100:400] = 255
masked_img = cv.bitwise_and(img,img,mask=mask)
#  cv.calcHist(images,channels,mask,histSize,ranges)
hist_full = cv.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.imshow(mask,'gray')
plt.subplot(223),plt.imshow(masked_img,'gray')
plt.subplot(224),plt.plot(hist_full,'b-'),plt.plot(hist_mask,'r-')
plt.xlim([0,256])
plt.show()