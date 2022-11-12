# U-Net(Convolutional Networks for Biomedical Image Segmentation)

## 该项目主要参考以下开源仓库
* [https://github.com/milesial/Pytorch-UNet](https://github.com/milesial/Pytorch-UNet)
* [https://github.com/pytorch/vision](https://github.com/pytorch/vision)
* [https://github.com/WZMIAOMIAO/deep-learning-for-image-processing](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing)

## 环境配置：
* Python3.9
* Pytorch1.10
* Ubuntu或Centos(Windows暂不支持多GPU训练)
* 使用单GPU训练
* 详细环境配置见`requirements.txt`

## 文件结构：
```
  ├── src: 搭建U-Net模型代码
  ├── train_utils: 训练、验证以及多GPU训练相关模块
  ├── my_dataset.py: 自定义dataset用于读取DRIVE数据集(视网膜血管分割)
  ├── train.py: 以单GPU为例进行训练
  ├── train_multi_GPU.py: 针对使用多GPU的用户使用
  ├── predict.py: 简易的预测脚本，使用训练好的权重进行预测测试
  └── compute_mean_std.py: 统计数据集各通道的均值和标准差
```

## DRIVE数据集下载地址：
* 官网地址： [https://drive.grand-challenge.org/](https://drive.grand-challenge.org/)
* 百度云链接： [https://pan.baidu.com/s/1Tjkrx2B9FgoJk0KviA-rDw](https://pan.baidu.com/s/1Tjkrx2B9FgoJk0KviA-rDw)  密码: 8no8




## 使用U-Net在DRIVE数据集上训练得到的权重(仅供测试使用)
- 链接: https://pan.baidu.com/s/1BOqkEpgt1XRqziyc941Hcw  密码: p50a

## 如果对U-Net网络不了解的可参考bilibili
* [https://www.bilibili.com/video/BV1Vq4y127fB/](https://www.bilibili.com/video/BV1Vq4y127fB/)


## 进一步了解该项目，以及对U-Net代码的分析可参考bilibili
* [https://b23.tv/PCJJmqN](https://b23.tv/PCJJmqN)

## 本项目U-Net默认使用双线性插值做为上采样，结构图如下
![u-net](unet.png)
