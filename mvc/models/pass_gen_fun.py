__all__ = ['last_result_is_empty', 'copy_to_clipboard']

from .types import *
import pyperclip


_last_generation: passwords_t = []

def last_result_is_empty() -> bool:
    global _last_generation
    return len(_last_generation) == 0

def copy_to_clipboard() -> None:
    global _last_generation

    text_to_copy: str = '\n'.join(_last_generation)
    pyperclip.copy(text_to_copy)  # info! может быть исключение `pyperclip.PyperclipException`
