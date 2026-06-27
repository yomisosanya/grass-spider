include .env

APP_NAME = spider-app
FILE_DIR = $(shell pwd)
APP_DIR ?= $(FILE_DIR)/$(APP_NAME)


.PHONY: build run clean

build:
	docker build \
	    --build-arg APP_DIR=$(APP_DIR)/$(APP_NAME) \
		--build-arg FILE_DIR=$(FILE_DIR) \
		--build-arg APP_NAME=$(APP_NAME) \
		-t $(APP_NAME) .


run:
	docker run \
	    --env-file .env \
		$(APP_NAME)


clean:
	docker rmi $(APP_NAME)

