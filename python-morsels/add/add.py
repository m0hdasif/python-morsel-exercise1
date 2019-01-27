from operator import itemgetter

def add(*args):
    # validate inputs
    if len(set(map(len, args))) != 1 or any(len(set(map(len, args[i]))) != 1 for i in range(len(args))):
        raise ValueError('Lists are of different sizes.')
    result = []
    for row in zip(*args):
        result.append([sum(list(map(itemgetter(i), row))) for i in range(len(row[0]))])
    return result
