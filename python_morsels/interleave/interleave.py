def interleave(*args):
    for values in zip(*args):
        yield from values
