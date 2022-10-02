import torch
import torchvision.transforms as transforms
from PIL import Image
from model import LeNet

transforms = transforms.Compose(
    [transforms.Resize((32, 32)),
    transforms.ToTensor(), 
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
)

classes = ("plane", "car", "bird", "cat",
            "deer", "dog", "frog", "horse", "ship", "truck")

net = LeNet()
net.load_state_dict(torch.load("Lenet.pth"))

im = Image.open("1.jpg")
im = transforms(im) # [C, H, W]
im = torch.unsqueeze(im, dim=0) # [N, C, H, W]

with torch.no_grad():
    outputs = net(im)
    predict = torch.softmax(outputs, dim = 1)
print(predict)
