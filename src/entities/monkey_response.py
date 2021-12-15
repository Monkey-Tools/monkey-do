"""Entity for the mock response"""
from dataclasses import dataclass
from typing import Union

@dataclass
class MonkeyResponse():
    status: int
    body: Union[str, dict]
    mime_type: str = 'text/plain'
