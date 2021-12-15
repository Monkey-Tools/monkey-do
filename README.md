# monkey-do
Tool to set up mock http apis quickly
#
### Prerequisites:
- python 3.9 installed
- pipenv installed
- docker installed
### Hello world set up steps:
1. To build and run the docker image first run ```make config-link``` to create a local config for monkey-do in ~/.config/monkey-do
2. Run ```make monkey-do``` to build and run the service
3. run ```curl localhost:8484/hello/world.json``` to get a json response
4. open http://localhost:8484/hello/world in your browser
#
## Makefle:

```make config-link``` - sets up a config directory for monkey-do, copies the sample config and makes a symlink in the workspace

```make requirements``` - makes a requirements.txt for pip in docker

```make monkey-do``` - build and run monkey-do

```make docker-build``` - makes requirements and builds the docker image

```make docker-run``` - run monkey-do as a docker container

```make docker-rm``` - deletes the docker container (must be stopped first) and deletes the image. use this between builds

```make help``` - show this stuff
