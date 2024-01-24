# ASR

## how to build (and push) the Dockerfile
$ docker buildx build --platform linux/amd64,linux/arm64 -t chanhookum/asr:latest . --push
you can omit "--push" for only build 
