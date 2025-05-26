__all__ = ['shuffle_pass']

from collections import defaultdict
from .types import *
import random


_last_generation: passwords_t = []

def _shuffle_pass(password: str, aggressive: bool = False) -> str:
    if not password: return password

    chars: list[str] = list(password)

    random.shuffle(chars)

    if aggressive:
        groups: defaultdict = defaultdict(list)
        for char in chars:
            if char.isupper():
                groups['upper'].append(char)
            elif char.islower():
                groups['lower'].append(char)
            elif char.isdigit():
                groups['digit'].append(char)
            else:
                groups['special'].append(char)

        for group in groups.values(): random.shuffle(group)

        shuffled: list[str] = []
        group_keys: list[str] = list(groups.keys())
        random.shuffle(group_keys)

        for key in group_keys: shuffled.extend(groups[key])

        return ''.join(shuffled)

    return ''.join(chars)

def shuffle_pass(password: str, aggressive: bool = False) -> str:
    global _last_generation
    password: str = _shuffle_pass(password, aggressive=aggressive)
    _last_generation = [password]
    return password
