"""Entity for the route configurations"""
from dataclasses import dataclass
from uuid import UUID

from entities.monkey_response import MonkeyResponse


class MonkeyHandler():
    id: str
    method: str
    route: str
    response: MonkeyResponse

    def __init__(self, id: str, method: str, route: str, response: dict):
        self.id = id
        self.method = method
        self.route = route
        response = MonkeyResponse(**response)
