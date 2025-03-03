# PyTorch DDP example

This runs on the AI2 cluster. 

Prerequisites:
- docker must be installed
- beaker must be installed

to create the image
1. edit the `build.sh` to update the image name
2. edit the `beaker_config.yaml`
3. execute the `build.sh` script in the AI2 folder 
4. execute the `beaker_experiment_runner.sh`

This repo simply implements the [pytorch ddp tutorial](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html).
