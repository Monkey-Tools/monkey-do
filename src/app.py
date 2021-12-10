"""Main executor for monkey-do"""
from flask import Flask, request
from flask.wrappers import Response
import yaml

from entities import MonkeyResponse, MonkeySeeConfig


app = Flask(__name__)
PORT = 5000


@app.route('/')
def root():
    return 'monkey-do running'


@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'])
def mock_point(path: str):
    """The proxy endpoint"""
    response = generate_response(path, request.method)
    return Response(response.body, status=response.status, mimetype='application/json')


def generate_response(route: str, method: str):
    route_config_file = open('config.mnkc')
    config_yaml = yaml.safe_load(route_config_file.read())
    mnkc_config = MonkeySeeConfig(**config_yaml)

    # TODO: add a way to match parameterized routes
    handler_matches = list(filter(lambda handler: handler.route == route, mnkc_config.handlers))

    if len(handler_matches) == 0:
        return MonkeyResponse(500, f'No handler found matching route: {route}')
    elif len(handler_matches) > 1:
        return MonkeyResponse(500, f'Found multiple matches for route: {route}')
    handler = handler_matches[0]
    
    #TODO: Add logic to deal with response scripts and external response.json files
    # For now just return the response object
    return handler.response


if __name__ == '__main__':
    app.run(debug=True, port=PORT)