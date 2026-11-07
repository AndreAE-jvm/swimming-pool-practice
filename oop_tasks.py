from time import sleep


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)   # Vector(4, 6)
print(v1 * 3)    # Vector(3, 6)


class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def position(self):
        return (self.x, self.y)

    def __repr__(self):
        return f"Robot({self.x}, {self.y})"
r = Robot()
r.move_up()
r.move_right()

print(r.position())  # (1, 1)
print(r)             # Robot(1, 1)
