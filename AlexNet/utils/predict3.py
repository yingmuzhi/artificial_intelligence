# add path
import os, sys
root_path = os.path.dirname(os.path.dirname(__file__))
project_path = os.path.dirname(__file__)
sys.path.append(project_path)
# add module
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
import json
import torch
import numpy as np
from model import AlexNet


def convert_image(image_path:str = ""):
    """transform png to jpg"""
    img=Image.open(image_path)
    name = "daisy.png"
    name=name.split(".")
    if name[-1] == "png":
        name[-1] = "jpg"
        name = str.join(".", name)
        r,g,b,a=img.split()              
        img=Image.merge("RGB",(r,g,b))   
        to_save_path = project_path + "/" + name
        img.save(to_save_path)
        print(to_save_path, "------conut：")

def main():
    # 路径
    root_path       = os.path.dirname(os.path.dirname(__file__))
    project_path    = os.path.dirname(__file__)
    weight_path     = os.path.join(root_path, "weight", "AlexNet_2.pth")
    # png_path        = "/home/yingmuzhi/AlexNet/daisy.png"
    image_path      = "/home/yingmuzhi/AlexNet/daisy.jpg"
    # # 将png转为jpg
    # convert_image(png_path)
    # 加载预测图片
    img             = None
    data_transform  = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    img = Image.open(image_path)
    print(np.array(img).shape)
    # plt.imshow(img)
    # [N, C, H, W]
    img = data_transform(img)   # 只接受[height, width, channel=3]的图片, 即RGB的jpg
    # expand batch dimension
    img = torch.unsqueeze(img, dim = 0) # 传入网络需要[batch, channel, height, width]
    print(img.shape)
    # 加载json文件
    try:
        json_file = open(project_path + "/class_indices.json","r")
        class_indict = json.load(json_file)
    except Exception as e:
        print(e)
        exit(-1)
    # 测试参数
    net = AlexNet(num_classes=2)
    # 加载网络参数
    net.load_state_dict(torch.load(weight_path))
    net.eval()    # 关闭dropout层并且不会梯度回传
    with torch.no_grad():
        # predict class
        output = net(img)
        # print(output.shape)
        output = torch.squeeze(output)
        # print(output.shape)
        predict = torch.softmax(output, dim = 0)
        # print(predict.shape)
        predict_cla = torch.argmax(predict).numpy()
    print(class_indict[str(predict_cla)], predict[predict_cla].item())
    # plt.show()

if __name__ == "__main__":
    main()


