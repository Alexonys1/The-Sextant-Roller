from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Region:
    x_of_left_top_corner: int
    y_of_left_top_corner: int
    width: int
    height: int
