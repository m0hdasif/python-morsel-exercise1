def deep_add(to_add, start=0):
    try:
        return sum((deep_add(items) for items in to_add), start)
    except:
        if not to_add:
            raise TypeError()
        try:
            return sum(to_add, start)
        except:
            return to_add + start
