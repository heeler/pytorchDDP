#!/bin/sh
set -e
python3.12 -m venv env
. env/bin/activate
python3.12 -m pip install --upgrade pip
pip3.12 install git+https://github.com/heeler/pytochDDP.git
printf "install done\n running"
sleep 5
ddp_launch
echo "done"