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
    weight_path         = os.path.join(root_path, "weight", "AlexNet.pth")
    # 选择训练硬件
    device              = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # print(device)
    # bach size
    batch_size          = 32
    # data_loader
    train_data_loader   = None
    test_data_loader    = None
    data_transform = {
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
        root=os.path.join(root_path, "data", "flower_data", "train"), 
        transform=data_transform["train"],
    )
    train_data_loader = DataLoader(
        dataset=train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=0,
    )
    # test
    test_dataset = datasets.ImageFolder(
        root=os.path.join(root_path, "data", "flower_data"), 
        transform=data_transform["test"],
    )
    # val_num = len(validate_dataset)
    test_data_loader = torch.utils.data.DataLoader(
        dataset=test_dataset, 
        batch_size=batch_size, 
        shuffle=False,
        num_workers=0,
    )
    # print(test_dataset[0])
    # # see train number and test number
    # print("the train number is {}, and the test number is {}".format(len(train_dataset), len(test_dataset)))
    # # see pics in test set
    # see_pic(
    #     test_dataset=test_dataset,
    #     train_dataset=train_dataset,
    # )
    # 训练参数
    net = AlexNet(num_classes=5, init_weights=True) # 模型
    loss_function = nn.CrossEntropyLoss()           # 损失函数
    net.to(device)   
    # 迁移学习，加载预训练权重
    try:
        net.load_state_dict(torch.load(weight_path))
    except Exception as e:
        print("load weight unsuccessfully")
    else:
        os.makedirs(os.path.join(root_path, "weight"))
    # 训练参数
    
    flower_list = train_dataset.class_to_idx
    cla_dict = dict((val, key) for key, val in flower_list.items())
    # # write json
    # json_str = json.dumps(cla_dict, indent=4)   # indent指每个(key: value)前的空格数量，一般指定为4
    # # print(json_str)
    # with open(project_path + "/class_indices.json", "w") as json_file:
    #     json_file.write(json_str)
    # train the net
    
   
    
    # pata = list(net.parameters())
    # print(pata)
    optimizer = optim.Adam(net.parameters(), lr = 0.0002)

    # print(len(train_data_loader))
    # print(len(train_dataset))
    best_acc = 0.0
    for epoch in range(1):
        # train
        net.train()
        running_loss = 0.0
        t1 = time.perf_counter()
        for step, data in enumerate(train_data_loader, start=0):
            images, labels = data
            optimizer.zero_grad()
            outputs = net(images.to(device))
            loss = loss_function(outputs, labels.to(device))
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            # print train process
            rate = (step + 1) / len(train_data_loader)    # len = len(dataset) / batch_size = 3306 / 32 = 104
            a = "*" * int(rate * 50)
            b = "*" * int((1 - rate) * 50)
            print("\rtrain loss: {:^3.0f}%[{}->{}]{:.3f}".format(int(rate * 100), a, b, loss), end="")
        print()
        print(time.perf_counter() - t1)

        # test
        net.eval()
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