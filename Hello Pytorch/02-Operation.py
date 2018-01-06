from __future__ import print_function
import torch
x = torch.rand(5, 3)
y = torch.rand(5, 3)
print(x + y)
#y = torch.rand(5, 3)
#print(x + y)

#result = torch.Tensor(5, 3)
#torch.add(x, y, out=result)
#print(result)

# adds x to y
y.add_(x)
print(y)