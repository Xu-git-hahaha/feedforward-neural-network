from PIL import Image
import numpy as np
#PIL的Image读取图片像素点颜色值到文件中

f = open("/Users/xuguoxiang/Desktop/feedforword neural network/testvalue5.txt", 'w+')

im = Image.open('/Users/xuguoxiang/Desktop/feedforword neural network/pictures_new3.png')
im = im.convert('L')  # 灰度化
#rgb_im = im.convert('RGB')
str1 = ''
'''
for i in range(28):

	for j in range(28):
		ee1 = im.getpixel((i, j))
		x = ee1[2]
		#r, g, b = rgb_im.getpixel((i, j))
		str1 = str1 + str(x) + ','
f.write(str1)'''
img_array = np.array(im)
for i in range(28):
    for j in range(28):
        if j != 27 or i != 27 :
            x = 255 - img_array[i][j]
            str1 = str1 + str(x) + ','
        else:
            x = 255 - img_array[i][j]
            str1 = str1 + str(x)
print(img_array)
print('\n')
print(str1)
f.write(str1)
f.close()