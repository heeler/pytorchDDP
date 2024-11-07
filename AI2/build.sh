#~/bin/sh

# build from project root (project/AI2)
rm -rf ./artifacts/*
cp entrypoint.sh ./artifacts

beaker image create --name cell_tools_benchmark_1 $(docker build -q --file Dockerfile ./artifacts --platform linux/amd64)
