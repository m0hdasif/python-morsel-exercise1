import math

class FloatRange:

    def __init__(self, *args):
        if not len(args) or len(args) > 3:
            raise TypeError()
        try:
            self.start, self.stop, self.step = args
        except:
            try:
                self.start, self.stop = args
            except:
                self.stop, *d = args
                self.start = 0
            self.step = 1

    def __iter__(self):
        yield from self.float_range_gen(self.start, self.stop, 
self.step)

    def __len__(self):
        return max(self.get_distance(self.start, self.stop, self.step), 
0)

    def __reversed__(self):
        range_length = len(self)
        self.stop = self.start - self.step
        self.start += (range_length - 1) * self.step
        self.step *= -1
        yield from self.float_range_gen(self.start, self.stop, 
self.step)

    def __eq__(self, other):
        try:
            return other == self
        except:
            if (self.start, other.start) == (self.stop, other.stop):
                return True
            elif (self.start, self.step, len(self)) == (other.start, 
other.step, len(other)):
                return True
            return (self.start, self.stop, self.step) == (other.start, 
other.stop, other.step)

    @staticmethod
    def get_distance(start, stop, step):
        return math.ceil((stop - start) / step)

    def float_range_gen(self, start, stop, step):
        if start > stop and step > 0 or start < stop and step < 0:
            yield []
        else:
            while self.get_distance(start, stop, step):
                yield start
                start += step

def float_range(*args):
    return FloatRange(*args)
