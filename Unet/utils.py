import imp


import numpy as np
from PIL import Image

#---------------------------------------------------------#
#   将图像转换成RGB图像，防止灰度图在预测时报错。
#   代码仅仅支持RGB图像的预测，所有其它类型的图像都会转化成RGB
#---------------------------------------------------------#

def cvtColor(image):
    try:
        if len(np.shape(image)) == 3 and np.shape(image)[2] == 3:
            return image
        else:
            image = image.convert('RGB')
            return image
    except:
        return image
#---------------------------------------------------#
#   对输入图像进行resize
#---------------------------------------------------#

def resize_image(image,size):
    input_w,input_h = image.size
    w,h = size

    scale = min(w/input_w,h/input_h)
    new_w = int(input_w*scale)
    new_h = int(input_h*scale)
    # BICUBIC：立方卷积插值放大
    image = image.resize((new_w,new_h),Image.BICUBIC)
    new_image = Image.new('RGB',size,(128,128,128))
    new_image.paste(image,((w-new_w)//2,(h-new_h)//2))

    return new_image,new_w,new_h
