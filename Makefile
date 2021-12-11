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

docker-run:	 ##run monkey-do as a docker container
	docker run -p 8484:8484 -v /home/james/repos/monkey-do/config.mnkc:/app/config.mnkc monkey-do-docker
