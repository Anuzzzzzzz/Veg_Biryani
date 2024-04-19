%matplotlib inline
import cv2
import matplotlib
from matplotlib import colors
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import os
import skimage.io
import PIL.

def show(image):
    # Figure size in inches
    plt.figure(figsize=(15, 15))
    
    plt.imshow(image, interpolation='nearest')
    
def overlay_mask(mask, image):
    rgb_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    img = cv2.addWeighted(rgb_mask, 0.5, image, 0.5, 0)
    show(img)
    
def convex_cnt(image):
    image = image.copy()
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_ = [cv2.convexHull(cnt) for cnt in contours ]
    mask = np.zeros(image.shape, np.uint8)
    [cv2.drawContours(mask, [cnt_], -1, 255, -1) for cnt_ in contours_] 
    return contours_,mask

def dilate_img(image_bin):
    img = image_bin.copy()
    kernel1 = np.ones((7,7),np.uint8)
    image_dilation = cv2.dilate(img,kernel,iterations = 1)
    return image_dilation


image = skimage.io.imread("C:/Users/aniru/Downloads/ABCD.jpeg")
image = cv2.resize(image, None, fx=1/3, fy=1/3)
print("Dimensiones ", image.shape)

image_blur = cv2.GaussianBlur(image, (7, 7), 0)
image_blur_hsv = cv2.cvtColor(image_blur, cv2.COLOR_RGB2HSV)

min_ = np.array([0, 100, 75])
max_ = np.array([20, 230, 230])
image_bin1 = cv2.inRange(image_blur_hsv, min_, max_)

min_ = np.array([160, 100, 100])
max_ = np.array([180, 230, 230])

image_bin2 = cv2.inRange(image_blur_hsv, min_, max_)

image_bin = image_bin2+image_bin1




kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20))

image_bin_closed = cv2.morphologyEx(image_bin, cv2.MORPH_CLOSE, kernel)

image_bin_closed_then_opened = cv2.morphologyEx(image_bin_closed, cv2.MORPH_OPEN, kernel)

image_dilation = dilate_img(image_bin_closed_then_opened)
contours, mask,= convex_cnt(image_dilation)
#show_mask(mask)


overlay_mask(mask, image)


def show_mask(mask):
    plt.figure(figsize=(10, 10))
    plt.imshow(mask, cmap='gray')
show_mask(mask)
