import pygame
import random
from copy import deepcopy
from typing import Tuple


screen: pygame.Surface = None
size = None


def new_problem(count: int) -> list[Tuple[float, float]]:
    return [(random.random(), random.random()) for i in range(count)]

def route_neighbor(route: list[Tuple[float, float]]):
    n = len(route)
    new = deepcopy(route)
    i1 = random.randint(0, n-1)
    i2 = random.randint(0, n-1)

    new[i1], new[i2] = new[i2], new[i1]

    return new

def _tuple_dist(a: tuple, b: tuple) -> float :
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def _zip_pairs(route):
        for i in range(len(route)):
            yield route[i-1], route[i]

def route_dist(route: list[Tuple[float, float]]) -> float:
    total = 0
    for a, b in _zip_pairs(route):
        total += _tuple_dist(a, b)

    return total


def init_display(size):
    pygame.init()

    globals()['size'] = size
    globals()['screen'] = pygame.display.set_mode(size)

def _tuple_to_screen_point(t):
    x, y = t
    sx, sy = size

    return int(x * sx), int(y*sy)

def draw_clear():
    screen.fill((255, 255, 255))

def draw_problem(route, line_color=(0, 0, 0)):
    l = list(map(_tuple_to_screen_point, route))
    pygame.draw.lines(screen, line_color, True, l, 2)

    for point in route:
        pygame.draw.circle(screen, (250, 0, 0), _tuple_to_screen_point(point), 5)

def refresh():
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()