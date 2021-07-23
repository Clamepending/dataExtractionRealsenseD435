import numpy as np
import cv2

def fillHole(im_in):
	im_floodfill = im_in.copy()

	# Mask used to flood filling.
	# Notice the size needs to be 2 pixels than the image.
	h, w = im_in.shape[:2]
	mask = np.zeros((h+2, w+2), np.uint8)

	# Floodfill from point (0, 0)
	cv2.floodFill(im_floodfill, mask, (0,0), 255);

	# Invert floodfilled image
	im_floodfill_inv = cv2.bitwise_not(im_floodfill)

	# Combine the two images to get the foreground.
	im_out = im_in | im_floodfill_inv

	return im_out

 # Load an color image in grayscale
img = cv2.imread('C:/Users/sotao/Desktop/Data/Test/fname9.jpg',cv2.IMREAD_GRAYSCALE)

 # show image
cv2.imshow('image',img)
cv2.waitKey(0)
img = fillHole(img)
cv2.imshow('image',img)
cv2.waitKey(0)
