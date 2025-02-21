import math
import sdl2


class Rectangle:
    def __init__(self, x, y, width, height, color, side, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.side = side  # 'left' or 'right'
        self.value = value  # Constant or variable
        self.is_dragging = False

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def contains(self, x, y):
        return (self.x <= x <= self.x + self.width and
                self.y <= y <= self.y + self.height)



class Rectangle_ops:
    def __init__(self, x, y, width, height, color, side, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.side = side  # 'left' or 'right'
        self.value = value  # Constant or variable
        self.is_dragging = False

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def contains(self, x, y):
        return (self.x <= x <= self.x + self.width and
                self.y <= y <= self.y + self.height)