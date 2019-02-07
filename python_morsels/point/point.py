class Point:

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.x, self.y, self.z) == (other.x, other.y, other.z)
        return False

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(
                x=self.x + other.x,
                y=self.y + other.y,
                z=self.z + other.z
            )
        raise ValueError('Incompatible types.')

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(
                x=self.x - other.x,
                y=self.y - other.y,
                z=self.z - other.z
            )
        raise ValueError('Incompatible types.')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                x=self.x * other,
                y=self.y * other,
                z=self.z * other
            )

    # make sure scaling works providing the scalar first
    __rmul__ = __mul__

    def __iter__(self):
        for axis, coordinate in self.__dict__.items():
            yield coordinate
