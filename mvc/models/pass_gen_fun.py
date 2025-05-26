__all__ = ['pass_gen']

from .types import *
import random
import string

DEFAULT_GENERATION_CHARS = string.ascii_lowercase + string.ascii_uppercase + '-_' + string.digits

_last_generation: passwords_t = []

def _pass_gen(length_pass: int = 8, by_chars: str = DEFAULT_GENERATION_CHARS, amount_result: int = 1) -> passwords_t:
    if length_pass <= 0 or len(by_chars) == 0: return []

    result: passwords_t = []

    for _ in range(amount_result):
        password: str = ''.join(random.choice(by_chars) for _ in range(length_pass))
        result.append(password)

    return result

def pass_gen(length_pass: int = 8, by_chars: str = DEFAULT_GENERATION_CHARS, amount_result: int = 1) -> passwords_t:
    global _last_generation

    result: passwords_t = _pass_gen(length_pass=length_pass, by_chars=by_chars, amount_result=amount_result)
    _last_generation = result.copy()

    return result
