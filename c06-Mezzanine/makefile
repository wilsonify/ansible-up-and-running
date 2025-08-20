IMAGE_NAME = mezzanine
TAG = latest
CONTAINER_NAME = mezzanine_dev
PORT = 8000

.PHONY: all build run stop clean logs

all: build run

build:
	docker build -t $(IMAGE_NAME):$(TAG) .

run:
	docker run -d --name $(CONTAINER_NAME) -p $(PORT):8000 $(IMAGE_NAME):$(TAG)

stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

clean: stop
	docker rmi $(IMAGE_NAME):$(TAG) || true

logs:
	docker logs -f $(CONTAINER_NAME)
