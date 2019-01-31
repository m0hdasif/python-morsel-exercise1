from itertools import groupby

def multimax(values, key=None):
    if not values:
        return []
    max_score = None
    for score, group in groupby(values, key):
        if not max_score or max_score < score:
            max_score = score
            result = list(group)
        elif max_score == score:
            result.extend(list(group))
    return result
