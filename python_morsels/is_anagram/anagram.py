from collections import Counter
import re
import unicodedata

def is_anagram(str_1, str_2):
    return get_counter(str_1) == get_counter(str_2)

def get_counter(text):
    return Counter(
        re.findall(
            r'\w',
            unicodedata.normalize('NFKD', text).lower()
        )
    )
