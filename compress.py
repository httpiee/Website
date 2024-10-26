from PIL import Image
import os
files = os.listdir("/home/su/Desktop/test_1/Images")
for i in files:
	f =i.split('.')
	img = Image.open("/home/su/Desktop/test_1/Images/"+i)
	width,height=img.size
	if f[0] == "8":
		new_size=(width*2,height)	
	else:

		new_size=(width,height)
	resized_Image=img.resize(new_size)
	resized_Image.save("/home/su/Desktop/test_1/Images/"+str(f[0])+".jpg")
