from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from enum import Enum


class Characters(Enum):
    btn_upper = ascii_uppercase
    btn_lower = ascii_lowercase
    btn_num = digits
    btn_special = punctuation

CHARACTER_NUMBER = {
        'btn_lower': len(Characters.btn_lower.value),
        'btn_upper': len(Characters.btn_upper.value),
        'btn_num': len(Characters.btn_num.value),
        'btn_special': len(Characters.btn_special.value)
    }

GENERATE_PASSWORD = (
    'btn_lower', 'btn_upper', 'btn_num', 'btn_special', 'btn_refresh'
)