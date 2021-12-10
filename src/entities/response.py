"""Entity for the mock response"""
from dataclasses import dataclass
from typing import Union

@dataclass
class MockResponse():
    status: int
    body: Union[str, dict]
