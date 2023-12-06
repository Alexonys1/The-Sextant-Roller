from random import randint

from game_manager.data_classes import Point, Region


def create_point_with_dispersion(point: Point, dispersion: int) -> Point:
    """
        Создать новую точку со случайным указанным разбросом в координатах.

        :param point: Точка с координатами. Задаётся именованным кортежем Point.
        :type point: Point

        :param dispersion: Разброс в координатах (px).
        :type dispersion: int

        :rtype: None
    """
    new_x = point.x + randint(-dispersion, dispersion)
    new_y = point.y + randint(-dispersion, dispersion)
    return Point(new_x, new_y)


def get_random_point_from_region(region: Region) -> Point:
    """
    Получить случайную точку из указанного региона.

    :param region: Регион, из которого возьмётся случайная точка. Задаётся именованным кортежем Region.
    :type region: Region

    :rtype: None
    """
    new_x = region.x_of_left_top_corner + randint(0, region.width)
    new_y = region.y_of_left_top_corner + randint(0, region.height)
    return Point(new_x, new_y)
