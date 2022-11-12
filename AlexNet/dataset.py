
from torchvision import transforms
from torch.utils.data.dataset import Dataset
from torch.utils.data.dataloader import DataLoader


class FlowerDataset(Dataset):
    """加载花数据集"""

    def __init__(self, path) -> None:
        super().__init__()
        self.transforms = {
            "train" :   transforms.Compose([
                transforms.RandomResizedCrop(224),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ]),
            "val"   :   transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))               
            ]) 
        }
        self.project_path = path

    def __len__(self):
        pass

    def __getitem__(self, index):
        pass

