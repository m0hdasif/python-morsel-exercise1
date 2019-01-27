from itertools import groupby
from collections import defaultdict

def group_by(numbers, key_func=None):
    if not key_func:
        def key_func(num):
            return num
    grouped = defaultdict(list)
    for k, v in groupby(numbers, key_func):
        grouped[k].extend(list(v))
    return grouped
