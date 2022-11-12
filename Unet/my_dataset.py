import os
from PIL import Image
import numpy as np
from torch.utils.data import Dataset


class DriveDataset(Dataset):
    def __init__(self, root: str, train: bool, transforms: object=None):
        super(DriveDataset, self).__init__()
        self.flag = "training" if train else "test" # 由 train: bool 的布尔值来判断是取train还是test
        data_root = os.path.join(root, "DRIVE", self.flag)
        assert os.path.exists(data_root), f"path '{data_root}' does not exists."
        self.transforms = transforms
        img_names = [i for i in os.listdir(os.path.join(data_root, "images")) if i.endswith(".tif")]
        self.img_list = [os.path.join(data_root, "images", i) for i in img_names]               # 返回所有images地址的list
        self.manual = [os.path.join(data_root, "1st_manual", i.split("_")[0] + "_manual1.gif")  # 返回所有manuals地址的list
                       for i in img_names]
        # check manual files
        for i in self.manual:
            if os.path.exists(i) is False:
                raise FileNotFoundError(f"file {i} does not exists.")

        self.roi_mask = [os.path.join(data_root, "mask", i.split("_")[0] + f"_{self.flag}_mask.gif")    # 返回所有mask地址的list
                         for i in img_names]
        # check mask files
        for i in self.roi_mask:
            if os.path.exists(i) is False:
                raise FileNotFoundError(f"file {i} does not exists.")

    def __getitem__(self, idx):
        """将Image转为RGB, 将label转为L"""
        img = Image.open(self.img_list[idx]).convert('RGB')
        manual = Image.open(self.manual[idx])
        # # find the max number in manual
        # a = np.array(manual)
        # max = 0
        # for i in range(len(a)):
        #     for j in range(len(a[0])):
        #         if max < a[i][j]:
        #             max = a[i][j]
        manual = manual.convert('L')
        manual = np.array(manual) / 255
        roi_mask = Image.open(self.roi_mask[idx]).convert('L')
        roi_mask = 255 - np.array(roi_mask)
        # 将manual图片和Imae进行处理
        mask = np.clip(manual + roi_mask, a_min=0, a_max=255)

        # a = np.array(img)
        # b = mask
        # 这里转回PIL的原因是，transforms中是对PIL数据进行处理
        mask = Image.fromarray(mask)

        if self.transforms is not None:
            img, mask = self.transforms(img, mask)
            # img = self.transforms(img)
            # mask = self.transforms(mask)

        # print(mask.shape)
        return img, mask

    def __len__(self):
        return len(self.img_list)

    @staticmethod
    def collate_fn(batch):
        images, targets = list(zip(*batch))
        batched_imgs = cat_list(images, fill_value=0)
        batched_targets = cat_list(targets, fill_value=255)
        return batched_imgs, batched_targets


def cat_list(images, fill_value=0):
    max_size = tuple(max(s) for s in zip(*[img.shape for img in images]))
    batch_shape = (len(images),) + max_size
    batched_imgs = images[0].new(*batch_shape).fill_(fill_value)
    for img, pad_img in zip(images, batched_imgs):
        pad_img[..., :img.shape[-2], :img.shape[-1]].copy_(img)
    return batched_imgs


if __name__=="__main__":
    from torchvision import transforms
    train_dataset = DriveDataset("/home/yingmuzhi/_data",
                                 train=True,
                                 transforms=transforms.Compose([transforms.ToTensor()]))
    a = train_dataset[0]

    # val_dataset = DriveDataset("/home/yingmuzhi/_data",
    #                            train=False,
    #                            transforms=None)

