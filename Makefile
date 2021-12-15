help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

requirements:	## makes a requirements.txt for pip in docker
	pipenv lock -r > requirements.txt

docker-build:	## makes requirements and builds the docker image
docker-build: requirements
	@docker build --tag monkey-do-docker .

docker-rm:	## deletes the docker container (must be stopped first) and deletes the image. use this between builds
	docker container prune
	docker rmi monkey-do-docker

docker-run:	## run monkey-do as a docker container
	docker run -p 8484:8484 \
	-v $$HOME/.config/monkey-do:/app/config \
	monkey-do-docker

config-link:    ## make a symbolic link to the config directory in the workspace, for initial linking of config directory
	mkdir -p $$HOME/.config/monkey-do
	ln -s $$HOME/.config/monkey-do ./config
	cp -r ./sample_config/. ./config

sample-config:	## copy config files from $HOME/.config/monkey-do, for updating sample configs in repository
	cp -r $$HOME/.config/monkey-do ./sample_config

monkey-do:	## run docker-build and docker-run
monkey-do: docker-build
monkey-do: docker-run