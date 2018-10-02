import numpy as np
import os
from PIL import Image

	#将图片转换成txt文件
def i2t(picpath,txtpath,filename):
	img = Image.open(picpath +filename).convert('L')
	txtName = txtpath + filename.split('.')[0] + ".txt"
	num = np.zeros((img.size[0],img.size[1]))
	numStr = ""
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			if img.getpixel((x,y))<128:
				num[x,y] = 0
			else:
				num[x,y] = 1
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			if num[j,i] == 1 :
				numStr = numStr + '1'
			else :
				numStr = numStr + '0'
		numStr = numStr +  '\n'
	#print(numStr)
	with open(txtName, 'w') as txt_file:
		txt_file.write(numStr)
