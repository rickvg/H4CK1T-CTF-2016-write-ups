from PIL import Image
import random

FLAG = "Unknown"

img = Image.open('encrypted.png')
img_pix = img.convert('RGB')

x = random.randint(1,255)
y = random.randint(1,255)

flaglen = (img_pix.getpixel((0,0)))[0]
print("Flag length: " + str(flaglen))
x = img_pix.getpixel((0,0))[1]
y = img_pix.getpixel((0,0))[2]

string = ""

string += chr(img_pix.getpixel((x,y))[0])
x1 = img_pix.getpixel((x,y))[1]
y1 = img_pix.getpixel((x,y))[2]

for i in range(0,flaglen):
	string += chr(img_pix.getpixel((x1,y1))[0])
	result = img_pix.getpixel((x1,y1))
	x1 = result[1]
	y1 = result[2]

print("Data found: " + string)
	

