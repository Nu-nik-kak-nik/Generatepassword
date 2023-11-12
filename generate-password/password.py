import secrets
from math import log2
from enum import IntEnum


class StrengthToEntropy(IntEnum):
    Pathetic = 0
    Weak = 30
    Good = 60
    Strong = 80
    Excellent = 120


def create_new(length: int, characters: str) -> str:
    return "".join(secrets.choice(characters) for _ in range(length))


def get_entropy(length: int, number_char: int) -> float:
    try:
        entropy = round(length*log2(number_char), 2)
    except ValueError:
        return 0.0
    return entropy
