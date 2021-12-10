from os import stat
from flask import Flask, request
from flask.wrappers import Response
from entities import MockRouteConfig, MockResponse
import yaml


app = Flask(__name__)
SITE_NAME='http://localhost:8000'


@app.route('/')
def root():
    return 'monkey-do poc running'


@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'])
def mock_point(path: str):
    # here we can call a function based on path and http method
    # that function should read a yaml file and generate a response based on the provided information
    # it will likely be broken out into a module but for poc we will use method generate_response
    response = MockResponse(**generate_response(path, request.method))
    return Response(response.body, status=response.status, mimetype='application/json')


def generate_response(path: str, method: str):
    route_config_file = open('mock_routes/routes.mnkc.yaml')
    route_configs = yaml.safe_load(route_config_file.read())['routes']
    hello_world_route_config = list(filter(lambda x: x['id'] == 'hello_world', route_configs))[0]
    hello_world = MockRouteConfig(**hello_world_route_config)
    return hello_world.response 


if __name__ == '__main__':
    app.run(debug=True, port=5100)