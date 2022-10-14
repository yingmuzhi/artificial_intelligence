'''
some learning about calculation
'''

#%%
import torch

# using matmul to reduce number of elements
a = torch.randn(4, 784)
x = torch.randn(4, 784)
w = torch.randn(512, 784)
y = torch.matmul(x, w.transpose(0, 1))
print(y.shape)
# %%
