from typing import NamedTuple
from random import randint


class Point (NamedTuple):
    x: int
    y: int


class Region (NamedTuple):
    x_of_left_top_corner: int
    y_of_left_top_corner: int
    width: int
    height: int
