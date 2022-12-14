# --- add path
import os, sys
project_path = os.path.dirname(__file__)
root_path = os.path.dirname(project_path)
sys.path.append(project_path)
# ---
import torch
import torch.nn as nn
from torchvision import transforms, datasets, utils
import torch.optim as optim
from model import AlexNet
import json, time
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np


def generate_json(train_dataset:object=None):
    """generate class indices"""
    flower_list = train_dataset.class_to_idx
    cla_dict = dict((val, key) for key, val in flower_list.items())
    # write dict into json file
    json_str = json.dumps(cla_dict, indent = 4) # 开头空四格，保持格式整洁
    with open(project_path + "/class_indices.json", "w") as json_file:
        json_file.write(json_str)

def see_pic(test_dataset, train_dataset):
    """to see pics"""
    test_data_loader = torch.utils.data.DataLoader(
        dataset=test_dataset, 
        batch_size=4, 
        shuffle=False,
        num_workers=0,
    )
    test_data_iter = iter(test_data_loader)
    test_input, test_label = test_data_iter.next()

    img = utils.make_grid(test_input)  
    img = img/2 + 0.5   # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.savefig(project_path+"/to_see_picture.jpg")
    plt.show()

    flower_list = train_dataset.class_to_idx
    cla_dict = dict((val, key) for key, val in flower_list.items())
    print(" ".join("%5s" % cla_dict[test_label[j].item()] for j in range(4)))

def main():
    # 路径
    project_path        = os.path.dirname(__file__)
    root_path           = os.path.dirname(project_path)
    weight_path         = os.path.join(root_path, "weight", "AlexNet_2.pth")
    # bach size
    batch_size          = 32
    # data_loader
    train_data_loader   = None
    test_data_loader    = None
    data_transform      = {
        "train": transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ]),
        "test": transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
    }
    train_dataset = datasets.ImageFolder(
        root=os.path.join(root_path, "data", "flower_data2", "train"), 
        transform=data_transform["train"],
    )
    train_data_loader = DataLoader(
        dataset=train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=0,
    )
    test_dataset = datasets.ImageFolder(
        root=os.path.join(root_path, "data", "flower_data2", "val"), 
        transform=data_transform["test"],
    )
    test_data_loader = torch.utils.data.DataLoader(
        dataset=test_dataset, 
        batch_size=batch_size, 
        shuffle=False,
        num_workers=0,
    )
    # 生成json文件
    generate_json(train_dataset=train_dataset)
    # 训练参数
    net                 = AlexNet(num_classes=2, init_weights=True) # 模型
    loss_function       = nn.CrossEntropyLoss()           # 损失函数
    device              = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    net.to(device)
    optimizer           = optim.Adam(net.parameters(), lr = 0.0002)
    # 迁移学习，加载预训练权重
    try:
        net.load_state_dict(torch.load(weight_path))
    except Exception as e:
        print("load weight failed")
        try:
            os.makedirs(os.path.join(root_path, "weight"))
        except:
            print("already has path:{}".format(os.path.join(root_path, "weight")))
        else:
            print("mkdir path")
    else:
        print("load weight successifully")
    # 开始训练
    best_acc = 0.0
    for epoch in range(1000):
        # train
        net.train()
        running_loss = 0.0
        t1 = time.perf_counter()
        for step, data in enumerate(train_data_loader, start=0):
            images, labels = data
            # 传入GPU
            images = images.to(device)
            labels = labels.to(device)
            optimizer.zero_grad()   # 梯度清零
            outputs = net(images)   # 进行训练，正向传播
            loss = loss_function(outputs, labels)   # 指定x，y
            loss.backward()         # 误差反向传播
            optimizer.step()        # 更新optimizer中的参数
            # print statistics
            running_loss += loss.item() # 更新损失
            # 一些花里胡哨的东西，打印进度条
            rate = (step + 1) / len(train_data_loader)    # len = len(dataset) / batch_size = 3306 / 32 = 104
            a = "*" * int(rate * 50)
            b = "*" * int((1 - rate) * 50)
            print("\rtrain loss: {:^3.0f}%[{}->{}]{:.3f}".format(int(rate * 100), a, b, loss), end="")
        print()
        print("train time used about {} s".format(time.perf_counter() - t1))

        # test
        net.eval()  # 指定为evaliation, 这个时候不会传递梯度
        acc = 0.0   # accumulate accurate number / epoch
        with torch.no_grad():
            for data_test in test_data_loader:
                test_images, test_labels = data_test
                outputs = net(test_images.to(device))
                predict_y = torch.max(outputs, dim = 1)[1]
                acc += (predict_y == test_labels.to(device)).sum().item()
            accurate_test = acc / len(test_dataset)
            if accurate_test > best_acc:
                best_acc = accurate_test
                torch.save(net.state_dict(), weight_path)
            print("[epoch %d] train_loss: %.3f test_accuracy: %.3f" %
                    (epoch + 1, running_loss / step, acc / len(test_dataset)))

if __name__ == "__main__":
    main()