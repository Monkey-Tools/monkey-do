"""Main executor for monkey-do"""
from click import command, argument
from flask import Flask, request
from flask.wrappers import Response
import yaml

from entities import MonkeyResponse, MonkeySeeConfig
from utilities import routes_match


app = Flask('monkey_do_server')
mnkc_yaml = yaml.safe_load(open('config.mnkc').read())
MNKC: MonkeySeeConfig = MonkeySeeConfig(**mnkc_yaml)


@app.route('/')
def root():
    return 'monkey-do running'


@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'])
def mock_point(path: str) -> Response:
    """The proxy endpoint"""
    response = generate_response(path, request.method)
    return Response(response.body, status=response.status, mimetype='application/json')


def generate_response(route: str, method: str) -> MonkeyResponse:
    """Generate a MonkeyResponse from the mnkc"""
    handler_matches = list(filter(lambda handler: routes_match(handler.route, route), MNKC.handlers))
    for handler in handler_matches:
        if handler.method == method:
            return handler.response
    return MonkeyResponse(404, f'Mokey see no {method} defined for {route}, monkey do 404.')


@command()
@argument('file')
def start_server(file):
    """Start the flask server"""
    app.run(debug=True, port=MNKC.port)


if __name__ == '__main__':
    start_server()
