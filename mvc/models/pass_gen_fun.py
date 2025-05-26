__all__ = ['pass_gen', 'pass_gen_from_phrase', 'last_result_is_empty', 'copy_to_clipboard']

from .types import *
import pyperclip
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

def last_result_is_empty() -> bool:
    global _last_generation
    return len(_last_generation) == 0

def copy_to_clipboard() -> None:
    global _last_generation

    text_to_copy: str = '\n'.join(_last_generation)
    pyperclip.copy(text_to_copy)  # info! может быть исключение `pyperclip.PyperclipException`

