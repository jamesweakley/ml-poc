# ml-poc

`docker build -f ray.dockerfile -t ray_dev .`

`docker run -it ray_dev:latest ray start --head --redis-port=6379`