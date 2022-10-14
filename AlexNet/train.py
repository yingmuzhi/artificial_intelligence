# --- add path
import os, sys
project_path = os.path.dirname(__file__)
sys.path.append(project_path)
# ---
import torch
import torch.nn as nn
from torchvision import transforms, datasets, utils
import torch.optim as optim
from model import AlexNet
import os, json, time

device = torch.device("cuda: 0" if torch.cuda.is_available() else "cpu")
print(device)

data_transform = {
    "train": transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ]),
    "val": transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
}

# data_root = os.path.abspath(os.path.join(os.getcwd(), "../..")) # get data root path
# image_path = data_root + "/data_set/flower_data/"               # flower data set path
train_dataset = datasets.ImageFolder(root=project_path + "/flower_data/train", transform=data_transform["train"])
train_num = len(train_dataset)

flower_list = train_dataset.class_to_idx
cla_dict = dict((val, key) for key, val in flower_list.items())
# write dict into json file
json_str = json.dumps(cla_dict, indent = 4)
with open("class_indices.json", "w") as json_file:
    json_file.write(json_str)

batch_size = 32






