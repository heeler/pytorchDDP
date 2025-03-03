#~/bin/sh

# build an image and register it with beaker
# build from project root (project/AI2)

rm -rf ./artifacts/*
cp entrypoint.sh ./artifacts

docker build -t octo-test-pub --file Dockerfile --platform linux/amd64 .

