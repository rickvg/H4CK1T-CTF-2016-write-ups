from PIL import Image
import random

# Open image file and convert to RGB-format
img = Image.open('encrypted.png')
img_pix = img.convert('RGB')

# Get flag length and coordinates of next pixel with data
flaglen = (img_pix.getpixel((0,0)))[0]
print("Flag length: " + str(flaglen))
x = img_pix.getpixel((0,0))[1]
y = img_pix.getpixel((0,0))[2]

string = ""

# Get character from first next pixel
string += chr(img_pix.getpixel((x,y))[0])
x1 = img_pix.getpixel((x,y))[1]
y1 = img_pix.getpixel((x,y))[2]

# For loop to get all characters from the pixels
for i in range(0,flaglen):
	string += chr(img_pix.getpixel((x1,y1))[0])
	result = img_pix.getpixel((x1,y1))
	x1 = result[1]
	y1 = result[2]

# Print pixeldata
print("Data found: " + string)
	

