# 按比例缩小图片尺寸
from PIL import Image
im = Image.open('/Users/xuguoxiang/Desktop/feedforword neural network/yuan.jpg')
(x, y) = im.size  # 读取图片尺寸（像素）
x_s = 28  # 定义缩小后的标准宽度
#y_s = int(y * x_s / x)  # 基于标准宽度计算缩小后的高度
y_s = 28  # 基于标准宽度计算缩小后的高度
out = im.resize((x_s, y_s))  # 改变尺寸，保持图片高品质
out.save('pictures_new3.png')
