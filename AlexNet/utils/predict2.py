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
from model import AlexNet

data_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# transform png to jpg
img=Image.open(project_path + "/tulip.png")
name = "tulip.png"
name=name.split(".")
if name[-1] == "png":
    name[-1] = "jpg"
    name = str.join(".", name)
    r,g,b,a=img.split()              
    img=Image.merge("RGB",(r,g,b))   
    to_save_path = project_path + "/" + name
    img.save(to_save_path)
    print(to_save_path, "------conut：")


# load image
img = Image.open(project_path + "/tulip.jpg")
plt.imshow(img)
# [N, C, H, W]
img = data_transform(img)
# expand batch dimension
img = torch.unsqueeze(img, dim = 0)
# read class_indict
try:
    json_file = open(project_path + "/class_indices.json","r")
    class_indict = json.load(json_file)
except Exception as e:
    print(e)
    exit(-1)
# create model
model = AlexNet(num_classes=5)
# load model weights
model_weight_path = project_path + "/AlexNet.pth"
model.load_state_dict(torch.load(model_weight_path))
model.eval()    # close dropout layer
with torch.no_grad():
    # predict class
    output = torch.squeeze(model(img))
    predict = torch.softmax(output, dim = 0)
    predict_cla = torch.argmax(predict).numpy()
print(class_indict[str(predict_cla)], predict[predict_cla].item())
plt.show()


