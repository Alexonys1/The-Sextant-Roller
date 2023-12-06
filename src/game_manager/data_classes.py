from typing import NamedTuple
from random import randint


class Point (NamedTuple):
    x: int
    y: int

    def create_new_point_with_dispersion(self, dispersion: int) -> 'Point':
        """
        Создать новую точку со случайным указанным разбросом в координатах.

        :param dispersion: Разброс в координатах (px).
        :type dispersion: int
        :rtype: None
        """
        new_x = self.x + randint(-dispersion, dispersion)
        new_y = self.x + randint(-dispersion, dispersion)
        return Point(new_x, new_y)


class Region (NamedTuple):
    x_of_left_top_corner: int
    y_of_left_top_corner: int
    width: int
    height: int
