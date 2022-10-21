import torch.nn
import torch.nn.functional


class LeNet(torch.nn.Module):
    """model

    Args:
        torch (_type_): _description_
    """

    def __init__(self):
        """build model
        """
        super(LeNet, self).__init__()   # parent's init
        self.conv1 = torch.nn.Conv2d(3, 16, (5, 5))
        self.pool1 = torch.nn.MaxPool2d((2, 2), 2)
        self.conv2 = torch.nn.Conv2d(16, 32, 5)
        self.pool2 = torch.nn.MaxPool2d(2, 2)
        self.fc1   = torch.nn.Linear(32 * 5 * 5, 120)                           # full connect to 1 dimension
        self.fc2   = torch.nn.Linear(120, 84)
        self.fc3   = torch.nn.Linear(84, 10)

    def forward(self, x):                                   
        """forward propagation

        Args:
            x (Tensor): [batches, channels, height, width]
        """
        x = torch.nn.functional.relu(self.conv1.__call__(x))    # input[batch, 3, 32, 32]   output[batch, 16, 28, 28]    
        x = self.pool1(x)                                       # output(16, 14, 14)        height and width become 1/2   
        x = torch.nn.functional.relu(self.conv2.__call__(x))    # output[batch, 32, 10, 10]
        x = self.pool2(x)                                       # output[batch, 32, 5, 5]
        x = x.view(-1, 32 * 5 * 5)                              # output(32*5*5)    # -1 means Automated reasoning
        x = torch.nn.functional.relu(self.fc1(x))               # output(120)
        x = torch.nn.functional.relu(self.fc2(x))               # output(84)
        x = self.fc3(x)                                         # output(10)
        return x
        

if __name__ == "__main__":
    import torch
    my_model = LeNet()
    print(my_model)
    my_tensor = torch.randn(32, 3, 32, 32)
    my_model.forward(my_tensor)