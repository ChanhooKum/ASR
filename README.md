# ASR

## how to build (and push) the Dockerfile
```bash
docker buildx build --platform linux/amd64,linux/arm64 -t chanhookum/asr:latest . --push
```
you can omit "--push" for only build 
