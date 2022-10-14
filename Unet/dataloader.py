import os
from torch.utils.data.dataset import Dataset
import numpy as np
import torch
from PIL import Image
from utils import cvtColor,resize_image
from torchvision import transforms
# from libtiff import TIFF

transforms=transforms.Compose([transforms.ToTensor()])

class VivoDataset(Dataset):
    def __init__(self,path):
        super().__init__()
        self.path = path
        self.name = os.listdir(os.path.join(path,'data/train/input'))

    def __len__(self):
        return len(self.name)

    def __getitem__(self,index):
        yield_name = self.name[index]
        # 返回label图片
        yield_label_name = yield_name.replace('_pad.tif','.tiff')
        label_path = os.path.join(self.path,'cleaned_data',yield_label_name)
        label_image = TIFF.open(label_path,mode='r').read_image()
        # label_image = TIFF.open(label_path,mode='r')
        # label_image = np.expand_dims(label_image,axis=0)
        label_image = Image.fromarray((label_image * 255).astype(np.uint8))
        label_image = cvtColor(label_image)
        label_image = resize_image(label_image,(512, 512))[0]

        # 返回训练图片
        # try:
        #     try:
        # yield_train_name = yield_name.replace('.tiff','_pad.tif')
        image_path = os.path.join(self.path,'data/train/input',yield_name)
        image = TIFF.open(image_path,mode='r').read_image()
        #     except:
        #         yield_train_name = yield_name.replace('.tiff','_pad.tiff')
        #         image_path = os.path.join(self.path,'data/train/input',yield_train_name)
        #         image = TIFF.open(image_path,mode='r').read_image()
        # except:
        #     yield_train_name = yield_name.replace('.tiff','_pad.tif')
        #     image_path = os.path.join(self.path,'data/val/input',yield_train_name)
        #     image = TIFF.open(image_path,mode='r').read_image()

        image = Image.fromarray((image * 255).astype(np.uint8))
        image = cvtColor(image)
        # image = Image.fromarray(image)
        image = resize_image(image,(512, 512))[0]
        
        return transforms(image),transforms(label_image) 

class UnetDataset(Dataset):
    def __init__(self,path) -> None:
        super().__init__()
        self.path = path
        self.name = os.listdir(os.path.join(path,'Labels'))

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        yield_name = self.name[index]
        # 返回label图片
        label_path = os.path.join(self.path,'Labels',yield_name)
        label_image = Image.open(label_path)
        label_image = cvtColor(label_image)
        label_image = resize_image(label_image,(512, 512))[0]
        # 返回训练图片
        image_path = os.path.join(self.path,'Images',yield_name)
        image = Image.open(image_path)
        image = cvtColor(image)
        image = resize_image(image,(512, 512))[0]
        
        return transforms(image),transforms(label_image)

if __name__ == '__main__':
    weight_path = 'params/vivo_unet.pth'
    data_path = r'C:\Users\Asaue\Desktop\u-net\data'
    save_path = r'C:\Users\Asaue\Desktop\u-net\vivo_result'
    VivoDataset(data_path).__getitem__(0)
    # UnetDataset(data_path).__getitem__(0)
    # data_path = r'C:\Users\Asaue\Desktop\u-net\Medical_Datasets'
