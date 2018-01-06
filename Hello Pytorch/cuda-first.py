from __future__ import print_function
import torch
x = torch.rand(5,3)
y = torch.rand(5,3)
# let us run this cell only i[f CUDA is available
if torch.cuda.is_available():
    x = x.cuda()
    y = y.cuda()
    result = x + y
    print(x)
    print(y)
    print(result)