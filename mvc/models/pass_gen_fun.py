__all__ = ['pass_gen_from_phrase']

from .types import *
import random


_last_generation: passwords_t = []

def _pass_gen_from_phrase(phrase: str, amount_word: int = 6, amount_result: int = 1, separator: str = ' ') -> passwords_t:
    separator: str = separator[:1]
    if amount_word <= 0 or not phrase or not separator: return []

    words: list[str] = phrase.split(separator)
    result: passwords_t = []

    for _ in range(amount_result):
        password = separator.join(random.choice(words).strip() for _ in range(amount_word))
        result.append(password)

    return result


def pass_gen_from_phrase(phrase: str, amount_word: int = 6, amount_result: int = 1, separator: str = ' ') -> passwords_t:
    global _last_generation

    result: passwords_t = _pass_gen_from_phrase(phrase=phrase, amount_word=amount_word, amount_result=amount_result, separator=separator)
    _last_generation = result.copy()

    return result
