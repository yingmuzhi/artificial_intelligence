# ---add path
import sys, os
from turtle import forward
project_dir = os.path.dirname(__file__)
sys.path.append(project_dir)
# ---
import torch
import torch.nn as nn

class AlexNet(nn.Module):
    def __init__(self, num_classes = 1000, init_weights = False) -> None:
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(in_channel = 3, out_channel = 48, kernel_size=11, stride=4, padding = 2),    # in_channel = input matrix channel(也即上一层的output_channel) = kernel channel;   out_channel = output matrix channel = kernels;
            nn.ReLU(inplace = True),
            nn.MaxPool2d(kernel_size = 3, stride = 2),
            nn.Conv2d(48, 128, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(128, 192, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 192, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )
        self.classifier = nn.Sequential(
            nn.Dropout(p = 0.5),
            nn.Linear(128 * 6 * 6, 2048),
            nn.ReLU(inplace=True),
            nn.Dropout(p = 0.5),
            nn.Linear(2048, 2048),
            nn.ReLU(inplace=True),
            nn.Linear(2048, num_classes),
        )
        if init_weights:
            self._initialize_weights()

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, start_dim=1)   # make it flatten to go to the Linear layer
        x = self.classifier(x)
        return x

    def _initialize_weight():
        pass