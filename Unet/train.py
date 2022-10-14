from cProfile import label
import os
from torch import nn,optim
import torch
from torch.utils.data import DataLoader
from torchvision.utils import save_image
from dataloader import UnetDataset
from UNet import UNet


device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 细胞数据集
save_path = r'./'
weight_path = 'params/unet.pth'
data_path = r'./Medical_Datasets'
save_path = os.path.join(save_path,'result')

batch_size = 1

if __name__ == '__main__':
    data_loader = DataLoader(UnetDataset(data_path),batch_size=batch_size,shuffle=True)
    net = UNet().to(device)

    # 加载预训练权重
    if os.path.exists(weight_path):
        net.load_state_dict(torch.load(weight_path))
        print('successful load weight!')
    else:
        print('not successful load weight')
    
    opt = optim.Adam(net.parameters(),lr=1e-4)
    loss_fun = nn.MSELoss()

    epoch = 1
    while True:
        for index,(image,label_image) in enumerate(data_loader):
            image,label_image = image.to(device), label_image.to(device)

            print(label_image.size())

            out_image = net(image)

            train_loss = loss_fun(out_image,label_image)
            print(train_loss)

            opt.zero_grad()
            train_loss.backward()
            opt.step()

            if index%5==0:
                print(f'{epoch}-{index}-train_loss===>>{train_loss.item()}')

            if index%50==0:
                torch.save(net.state_dict(),weight_path)
            for j in range(batch_size):
            
                # _image=image[j]
                # _label_image=label_image[j]
                _out_image=out_image[j]
      
                #img=torch.stack([_image,_segment_image,_out_image],dim=0)
                img=torch.stack([_out_image],dim=0)
                
                save_image(img,f'./{save_path}/{index}_{j}.png')

        epoch+=1
