import torch
import numpy as np

x = torch.ones(5, requires_grad=True)
y = torch.zeros(5)
z = x + y
print(x)
print(y)
print(z)