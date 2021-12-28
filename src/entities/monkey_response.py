"""Entity for the mock response"""
from dataclasses import dataclass
from typing import Union

@dataclass
class MonkeyResponse():
    """Object representation of an monkey http response"""
    status: int
    body: Union[str, dict]
    mime_type: str = 'text/plain'
