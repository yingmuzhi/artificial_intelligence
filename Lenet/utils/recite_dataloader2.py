from matplotlib import transforms
import torch.utils.data.dataset
import PIL.Image
import torchvision.transforms


class LeNetDataset(torch.utils.data.dataset.Dataset):
    def __init__(self, path) -> None:
        super(LeNetDataset, self).__init__()
        self.transforms = {
            "train" :   torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
            ]),
            "val"   :   torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
            ]),
        }
        self.path = path


