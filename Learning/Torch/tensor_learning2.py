
'''
how to create a tensor
'''
import  numpy as np
import  torch

# import from numpy
a = np.array([2, 3.3])
print(torch.from_numpy(a))
a = np.ones([2, 3])
print(torch.from_numpy(a))

# import from List
a = torch.tensor([2., 3.2])
print(a)
a = torch.FloatTensor(2, 2, 2)
print(a)

# uninitialized data
a = torch.empty([2, 2])
print(a)
a = torch.Tensor(2, 3)
print(a)

# get tensor's type
a = torch.tensor([1., 3])
print(a)
print(a.type())
print(a.size())
print(len(a.size()))
print(a.dim())

# create rand tensor
a = torch.rand(2, 2)
print(a)
b = torch.rand_like(a)
print(b)
a = torch.randint(1, 10, [2, 2])
print(a)

# create randn tensor
a = torch.randn(3, 3)
print(a)

# create full tensor
a = torch.full([2, 3], 7)
print(a)
print(torch.full([], 7.))
print(torch.full([1], 7.))

# arange
a = torch.arange(0, 10, 2)
print(a)

# matrix
print(torch.ones(2, 2))
print(torch.zeros(2, 2))
print(torch.eye(2, 2))
a = torch.eye(2)
print(torch.ones_like(a))