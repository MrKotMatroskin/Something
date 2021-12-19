import math

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iadd__(self, other):
        if isinstance(other, Vector2d):
            self.x += other.x
            self.y += other.y
            return self
        else:
            raise TypeError("Only vector can be added to vector")

    def __add__(self, other):
        if isinstance(other, Vector2d):
            s = Vector2d(self.x, self.y)
            s.x += other.x
            s.y += other.y
            return s
        else:
            raise TypeError("Only vector can be added to vector")

    def __mul__(self, other):
        s = Vector2d(self.x, self.y)
        s.x *= other
        s.y *= other
        return s

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __isub__(self, other):
        if isinstance(other, Vector2d):
            self.x -= other.x
            self.y -= other.y
            return self
        else:
            raise TypeError("Only vector can be added to vector")

    def __sub__(self, other):
        if isinstance(other, Vector2d):
            s = Vector2d(self.x, self.y)
            s.x -= other.x
            s.y -= other.y
            return s
        else:
            raise TypeError("Only vector can be added to vector")

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)