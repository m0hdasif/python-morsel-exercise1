from collections import deque

def tail(series, n):
    return list([] if n <= 0 else deque(series, maxlen=n))
