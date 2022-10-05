'''
make the dimension transform in  tensor
'''
from math import prod
import torch

# view和reshape will lost dim information, the sequence of data is important
a = torch.rand(4, 1, 28, 28)
print(a.shape)
b = a.view(4, 784)
print(b.shape)
print(b.view(4, 1, 28, 28))
print(prod(b.shape))

# squeeze and unsqueeze to delete or add a dimension
a = torch.rand(2, 2, 2, 2)
print(a.unsqueeze(0).shape)
print(a.unsqueeze(-1).shape)
b = torch.rand(32)
b = b.unsqueeze(1).unsqueeze(2).unsqueeze(0)
print(b.shape)
print(b.squeeze().shape)
print(b.squeeze(0).shape)

# expand and repeat
print(b.expand(2, 32, 2, 2).shape)

# transpose and permute
a = torch.rand(4, 3, 28, 28)
print(a.transpose(1, 3).shape)
print(a.permute(0, 3, 2, 1).shape)

#%%
import torch
# broadcast = unsqueeze + expand
a = torch.rand(4, 32, 14, 14)
b = torch.rand(1, 32, 1, 1)

print((a + b).shape)

# %%
print("down")