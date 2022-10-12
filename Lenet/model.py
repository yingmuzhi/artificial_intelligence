import torch.nn as nn
import torch.nn.functional as F


class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=(5, 5))    # (in_channels, out_channels, kernel_size)
        self.pool1 = nn.MaxPool2d(kernel_size=(2, 2), stride=2)     # (kernel_size, stride)
        self.conv2 = nn.Conv2d(16, 32, 5)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(32*5*5, 120)   # full connect to 1 dimension
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):                   # x is [batch, channel, height, width]
        x = F.relu(self.conv1(x))           # input[batch, 3, 32, 32]   output[batch, 16, 28, 28]   tensor in pytorch is [batch, channel, height, width]
        x = self.pool1(x)                   # height and width become 1/2   output(16, 14, 14)
        x = F.relu(self.conv2(x))           # output[batch, 32, 10, 10]
        x = self.pool2(x)                   # output[batch, 32, 5, 5]
        x = x.view(-1, 32*5*5)              # output(32*5*5)    # -1 means Automated reasoning
        x = F.relu(self.fc1(x))             # output(120)
        x = F.relu(self.fc2(x))             # output(84)
        x = self.fc3(x)                     # output(10)
        return x


# debug
import torch
input1 = torch.rand([32, 3, 32, 32])
model = LeNet()
print(model)
output = model(input1)

# if __name__ == "__main__":
#     print("h")
#     print("x")