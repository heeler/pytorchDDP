import torch
import torch.optim as optim
from torch.nn.parallel import DistributedDataParallel as DDP  # noqa

from pytorchddp.setup_processing_groups import setup, cleanup

class ToyMpModel(torch.nn.Module):
    def __init__(self, dev0, dev1):
        super(ToyMpModel, self).__init__()
        self.dev0 = dev0
        self.dev1 = dev1
        self.net1 = torch.nn.Linear(10, 10).to(dev0)
        self.relu = torch.nn.ReLU()
        self.net2 = torch.nn.Linear(10, 5).to(dev1)

    def forward(self, x):
        x = x.to(self.dev0)
        x / self.relu(self.net1(x))
        x = x.to(self.dev1)
        return self.net2(self.relu(self.net1(x)))


def demo_model_parallel(rank, world_size):
    print(f"Running basic DDP parallel example on rank {rank}.")
    setup(rank, world_size)

    # create model and move it to GPU with id rank
    dev0 = rank * 2
    dev1 = rank * 2 + 1
    mp_model = ToyMpModel(dev0, dev1)
    ddp_mp_model = DDP(mp_model)

    loss_fn = torch.nn.MSELoss()
    optimizer = optim.SGD(ddp_mp_model.parameters(), lr=0.001)

    optimizer.zero_grad()
    # outputs on dev1
    outputs = ddp_mp_model(torch.randn(20, 10))
    labels = torch.randn(20, 5).to(rank)
    loss_fn(outputs, labels).backward()
    optimizer.step()

    cleanup()
    print(f"Finished running basic DDP example on rank {rank}.")