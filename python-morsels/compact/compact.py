def compact(seq):
    for i, val in enumerate(seq):
        if i == 0 or val != last:
            yield val
        last = val
