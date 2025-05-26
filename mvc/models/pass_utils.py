__all__ = ['MAX_SCORE_PASS', 'check_pass_strength']

import string


MAX_SCORE_PASS: int = 100

def check_pass_strength(password: str) -> int:
    length_ok: bool   = len(password) >= 8
    has_upper: bool   = any(c.isupper() for c in password)
    has_lower: bool   = any(c.islower() for c in password)
    has_digit: bool   = any(c.isdigit() for c in password)
    has_special: bool = any(c in string.punctuation for c in password)
    score: int = 0

    # info! максимальное значение score должно равняться MAX_SCORE_PASS
    if length_ok: score   += 50
    if has_upper: score   += 10
    if has_lower: score   += 10
    if has_digit: score   += 10
    if has_special: score += 20

    return score
