# add path
import os
project_path = os.path.dirname(os.path.dirname(__file__))
# add packages
import torchvision.datasets
import torchvision.transforms

transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])


class LeNetDataSet(object):
    """_summary_

    Args:
        object (_type_): _description_
    """

    def __init__(self, path) -> None:
        self.train_set = torchvision.datasets.CIFAR10(path, train=True, download=False, transform=transform)
        self.test_set  = torchvision.datasets.CIFAR10(path, train=False, download=False, transform=transform)


if __name__ == "__main__":
    my_dataset = LeNetDataSet()
    