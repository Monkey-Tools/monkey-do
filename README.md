# monkey-do
Tool to set up mock http apis quickly
#
## Makefle:

```make requirements``` - makes a requirements.txt for pip in docker

```make docker-build``` - makes requirements and builds the docker image

```make docker-rm``` - deletes the docker container (must be stopped first) and deletes the image. use this between builds

```make docker-run``` - run monkey-do as a docker container

```make help``` - show this stuff
