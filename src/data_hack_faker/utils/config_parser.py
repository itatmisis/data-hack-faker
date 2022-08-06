import os

import ujson as json


def parse_config(path: os.PathLike) -> dict:
    with open(path, "r") as f:
        config = json.load(f)
    return config


class JSONConfigParser:
    def __init__(self, parsed_config: dict):
        self.config = parsed_config
        self.dataclass = self.config["dataclass"]
        self.rows = self.config["rows"]
        self.fields = self.config.keys() - ["class", "rows"]
