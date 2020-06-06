from PIL import Image, ImageFilter

def pixelate(img, pixel_size=32):
	'''
	Given an image, return a pixelated version of the same size.
	'''

	# Resize smoothly down to pixel_size x pixel_size
	imgSmall = img.resize((pixel_size, pixel_size),resample=Image.BILINEAR)

	# Scale back up using NEAREST to original size
	result = imgSmall.resize(img.size,Image.NEAREST)

	return result

def contour(img):
	'''
	
	'''
	return img.filter(ImageFilter.CONTOUR)


def emboss(img):
	'''
	
	'''
	return img.filter(ImageFilter.EMBOSS)


def edges(img):
	'''
	
	'''
	return img.filter(ImageFilter.FIND_EDGES)

