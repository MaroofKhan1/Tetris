import pygame
import random

color = [
    (0, 0, 153),
    (255, 0, 102),
    (255, 0, 255),
    (255, 0, 255),
    (255, 0, 255),
    (204, 51, 0),
    (204, 51, 1)
]

# An array for all the color

class Figure:
    x = 0
    y = 0

    figure = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]


def __init__(self, x, y):
    self.x = y
    self.y = y
    self.type = random.randint(0, len(self.figure) - 1)
    self.color = random.randint(1, len(colors) - 1)
    self.rotation = 0

def image(self):
    return self.figures[self.type][self.rotation]

def rotate(self):
    self.rotation = (self.rotation + 1) % len(self.figures(self.lengthS))