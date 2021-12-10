"""Entity for the route configurations"""
from dataclasses import dataclass
from uuid import UUID
from typing import Union

@dataclass
class MockRouteConfig():
    id: UUID
    method: str
    route: str
    response: dict
        