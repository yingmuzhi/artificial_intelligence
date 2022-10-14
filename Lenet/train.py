# get project_dir
import os
import sys
project_dir = os.path.dirname(__file__)
sys.path.append(project_dir)
# ---
from random import shuffle
import torch
import torchvision
import torch.nn as nn
from model import LeNet
import torch.optim as optim
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np


# modify on dataset, 预处理
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
# train data --- download 50000 pics
trainset = torchvision.datasets.CIFAR10(root=project_dir + "/data", train=True, download=False, transform = transform)
# modify on dataset, get it into different batch
trainloader = torch.utils.data.DataLoader(trainset, batch_size=36, shuffle=True, num_workers=0) 
# test data --- dowenload 10000 pics
testset = torchvision.datasets.CIFAR10(root=project_dir + "/data", train=False, download=False, transform = transform)
testloader = torch.utils.data.DataLoader(testset, batch_size = 10000, shuffle = False, num_workers = 0)
test_data_iter = iter(testloader)
test_image, test_label = test_data_iter.next()
# different classes
classes = ("plane", "car", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck")

'''test show img
# show img
def imshow(img):
    img = img / 2 + 0.5 # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

# print labels
print("".join("%5s" % classes[test_label[j]] for j in range(4)))
# show images
imshow(torchvision.utils.make_grid(test_image))
'''

net = LeNet()
loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr = 0.001)

for epoch in range(2):  # loop
    running_loss = 0.0
    for step, data in enumerate(trainloader, start = 0):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data
        
        # zero the parameter gradients
        optimizer.zero_grad()                   # batch size is associated with hardware, while we can use zero_grad to get bigger batch size
        
        # forward + backward + optimize
        outputs = net(inputs)                   # forward propagation
        loss = loss_function(outputs, labels)   # calculate loss
        loss.backward()                         # back propagation
        optimizer.step()                        # update weight

        # print statistics
        running_loss += loss.item()
        if step % 500 == 499:
            with torch.no_grad():
                outputs = net(test_image)   # [batch, 10] 
                predict_y = torch.max(outputs, dim = 1)[1]
                accuracy = (predict_y == test_label).sum().item() / test_label.size(0)

                print("[%d, %5d] train_loss: %.3f test_accuracy: %.3f" %(epoch + 1, step + 1, running_loss / 500, accuracy))
                running_loss = 0.0


print("Finished Training")

save_path = "./Lenet.pth"
torch.save(net.state_dict(), save_path)

