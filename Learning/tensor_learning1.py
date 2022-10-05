import torch
import numpy as np

# data type
a = torch.randn(2, 3)
print(a)
print(a.type())
print(type(a))
print(isinstance(a, torch.FloatTensor))

# 0 dimension
print(torch.tensor(1.)) # dimension = 0, using to calculate loss
a = torch.tensor(2.2)
print(a.shape)
print(len(a.shape))
print(a.size())

# 1 dimension
print(torch.tensor([1, 1]))
print(torch.tensor([1.1, 2.2]))
print(torch.FloatTensor(2))
data = np.ones(2)   # numpy
print(data)
print(torch.from_numpy(data))
a = torch.ones(2)   # see its shape
print(a.size())

# 2 dimension
dim_2 = torch.randn(2, 3)
print(dim_2)
print(dim_2.size())
print(dim_2.size(0))

# 3 dimension
dim_3 = torch.rand(1, 2, 3)
print(dim_3)
print(dim_3.size())
print(dim_3[0])
print(list(dim_3.size()))

# 4 dimension
dim_4 = torch.rand(2, 3, 28, 28)
print(dim_4)
print(dim_4.size())
