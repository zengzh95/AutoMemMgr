
import torch
import torch.nn as nn

from colossalai.utils.model.colo_init_context import ColoInitContext

from mem_offload_optimize import memory_optimization

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(512, 1024, bias=False)
        self.fc2 = nn.Linear(1024, 1024, bias=False)
        self.fc3 = nn.Linear(1024, 2048, bias=False)
        self.fc4 = nn.Linear(2048, 512, bias=False)
        self.fc5 = nn.Linear(512, 512, bias=False)

    def forward(self, x):
        out = self.fc1(x)
        out = self.fc2(out)
        out = self.fc3(out)
        out = self.fc4(out)
        out = self.fc5(out)
        return out


model = MyModel()
data_dict = {"x" : torch.rand((1, 512))}

model = memory_optimization(model, data_dict, 1024*1024*4.0*5)
loss = torch.sum(model(**data_dict))
loss.backward()