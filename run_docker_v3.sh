nvidia-docker run -it --rm --net=host --runtime=nvidia --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 --gpus '"device=1,2"' -v "$(pwd):/home/devel/workspace" nvidia-cuda:20210509_01 bash

