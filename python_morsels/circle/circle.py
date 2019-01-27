import math

class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f'Circle({self.radius})'

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = value

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError('Diameter cannot be negative')
        self.radius = value / 2

    @area.setter
    def area(self, value):
        raise AttributeError('Cannot set the area')
