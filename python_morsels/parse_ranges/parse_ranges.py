import itertools
import re

def parse_ranges(ranges):
    range_list = []
    for num_range in ranges.split(','):
        num_range = list(filter(None, re.split(r'\D', num_range)))
        try:
            start, stop = map(int, num_range)
        except:
            start = stop = int(*num_range)
        stop += 1
        range_list.append(range(start, stop))
    return itertools.chain(*range_list)
