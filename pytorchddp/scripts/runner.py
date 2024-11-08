import logging
import torch
import torch.multiprocessing as mp

from pytorchddp.ToyModel import demo_basic, demo_checkpoint
from pytorchddp.ToyMpModel import demo_model_parallel

logger = logging.getLogger()

def run_demo(demo_fn, world_size):
    mp.spawn(demo_fn,
             args=(world_size,),
             nprocs=world_size,
             join=True)


def main():
    n_gpus = torch.cuda.device_count()
    assert n_gpus >= 2, f"Requires at least 2 GPUs to run this example but got {n_gpus}"
    logger.info(f"got {n_gpus} GPUs")
    world_size = n_gpus
    run_demo(demo_basic, world_size)
    run_demo(demo_checkpoint, world_size)
    world_size = n_gpus // 2
    run_demo(demo_model_parallel, world_size)
    logger.info("Done running demos")
