from PIL import Image
import random

# Open image and convert to RGB
img = Image.open('planet.png')
img_pix = img.convert('RGB')

# Initiate variables
arrPixels = []
y = 0

# There are 64 squares: As 1512/24+1 = 64 (Last one must be counted)
# 1512 = Width of dots & Height of pixels (dots)
# 24 = Distance between start of next pixel

# For matrix 64x64: Get pixel data per dot with distance 24
for i in range(0,64):
	x = 0
	y = i * 24
	for j in range(0,64):
		x = j * 24
		arrPixels.append(img_pix.getpixel((x,y)))

# Create new image in RGB format with size 64x64
im = Image.new('RGB', (64,64), "white")

# Put all the pixeldata from previous image into new image
count = 0
for i in range(0,64):
	for j in range(0,64):
		im.putpixel((j,i), arrPixels[count])
		count += 1

# Write image to file
im.save('output.png')		

