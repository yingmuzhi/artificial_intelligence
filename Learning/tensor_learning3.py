'''
how to find a tensor, means indexing.
the same as list
'''
import torch

a = torch.rand(4, 3, 28, 28)
print(a.shape)
print(a[0].shape)
print(a[0, 0].shape)
print(a[0, 0, 2, 3])
print(a[:2].shape)
print(a[:2, :1, :, :].shape)  
print(a[:2, -1:, :, :].shape)
print(a[:, :, 0:28:2, ::2].shape)

