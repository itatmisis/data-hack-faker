from dataclasses import dataclass


@dataclass(frozen=True)
class BaseDataclass:
    id: int
