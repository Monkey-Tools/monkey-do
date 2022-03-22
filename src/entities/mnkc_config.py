"""Entity type for the config.mnkc"""
from typing import List
from entities import MonkeyHandler


class MonkeySeeConfig():
    """Object representation of the mnkc config file"""
    port: int
    handlers: List[MonkeyHandler]

    def __init__(self, port: int, handlers: List[dict]) -> None:
        self.port = port
        self.handlers = list(map(lambda handler_dict: MonkeyHandler(**handler_dict), handlers))
