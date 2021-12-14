"""Entity for the route configurations"""
from entities.monkey_response import MonkeyResponse
from entities.exceptions import MonkeySeeConfigException


class MonkeyHandler():
    id: str
    method: str
    route: str
    response: MonkeyResponse

    def __init__(self, id: str, method: str, route: str, response: dict):
        self.id = id
        self.method = method
        self.route = route
        if 'body' in response.keys():
            self.response = MonkeyResponse(**response)
        elif 'body_file' in response.keys():
            with open(response['body_file']) as file:
                self.response = MonkeyResponse(response['status'], file.read())
        else:
            raise MonkeySeeConfigException(f'Monkey see error! The {method} {route} endpoint has no body or body_file.')
        