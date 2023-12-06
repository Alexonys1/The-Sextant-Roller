from random import randint

import pyautogui as pag

from loguru import logger
from pyclick import HumanClicker

from game_manager.coordinate_tools import create_point_with_dispersion, get_random_point_from_region
from game_manager.singleton import Singleton
from game_manager.inventory import Inventory
from game_manager.data_classes import Point, Region


class User (metaclass=Singleton):
    """
    Класс пользователя, отвечающий за взаимодействие с игрой путём
    совершения нажатий кнопок клавиатуры и мыши. Может быть создан
    только в единственном экземпляре (Singleton).
    """
    def __init__(self):
        self._inventory = Inventory()

    def take_item_in_inventory(self, cell_number: int) -> None:
        """
        Берёт предмет из указанной ячейки инвентаря левой кнопкой мыши.

        :param cell_number: Номер ячейки инвентаря (1-60).
        :type cell_number: int

        :raises InventoryCellIsEmpty: если ячейка пуста.
        :raises IncorrectInventoryCellNumber: если нет такой ячейки.

        :rtype: None
        """

    def use_item_in_inventory(self, cell_number: int) -> None:
        """
        Использует указанный предмет правой кнопкой мыши.

        :param cell_number: Номер ячейки инвентаря (1-60).
        :type cell_number: int

        :raises InventoryCellIsEmpty: если ячейка пуста.
        :raises IncorrectInventoryCellNumber: если нет такой ячейки.

        :rtype: None
        """

    def hold_down_shift(self) -> None:
        """Зажимает левый shift."""
        # Событие должно отслеживаться в классе.

    def release_shift(self) -> None:
        """Отжимает левый shift."""
        # Событие должно отслеживаться в классе.

    def make_left_mouse_click(self) -> None:
        """
        Нажать левую кнопку мыши.

        :rtype: None
        """
        pag.click(button="left")
        logger.debug("Нажата левая кнопка мыши.")

    def make_right_mouse_click(self) -> None:
        """
        Нажать правую кнопку мыши.

        :rtype: None
        """
        pag.click(button="right")
        logger.debug("Нажата правая кнопка мыши.")

    def move_to_point(self, point: Point, duration: float, dispersion: int = 0) -> None:
        """
        Передвигает курсор мыши в указанную точку. Нужно задать время,
        через которое курсор будет в нужной точке. Можно ввести разброс в координатах
        относительно пункта назначения.

        :param point: точка, куда будет двигаться курсор мыши. Задаётся классом Point.
        :type point: Point

        :param duration: время прохождения пути курсора, указывается в секундах.
        :type duration: float

        :param dispersion: создаёт квадратную область вокрут point, на которую наведётся курсор. Сторона квадрата: 2*dispersion.
        :type dispersion: int

        :raises UncorrectedPoint: если введены несуществующие координаты.

        :rtype: None
        """
        clicker = HumanClicker()
        point_with_dispersion = create_point_with_dispersion(point, dispersion)
        clicker.move(point_with_dispersion, duration=duration)
        logger.debug(f"Курсор мыши переведён на {point_with_dispersion}")

    def move_to_region(self, region: Region, duration: float) -> None:
        """
        Передвигает курсор мыши в указанный регион. Нужно задать время,
        через которое курсор будет в пункте назначения. Конкретное место в области
        выбирается случано.

        :param region: область, в которую наведётся курсор мыши. Задаётся классом Region.
        :type region: Region

        :param duration: время прохождения пути курсора, указывается в секундах.
        :type duration: float

        :raises UncorrectedPoint: если введены несуществующие координаты.

        :rtype: None
        """
        clicker = HumanClicker()
        point = get_random_point_from_region(region)
        clicker.move(point, duration=duration)
        logger.debug(f"Курсор мыши переведён на {point}")

    def move_to_top_stone_of_void(self) -> None:
        """
        Навести курсор мыши на место ролла секстантов, оно же -
        "Церемониальный камень пустоты", самый верхний камень из четырёх.

        :rtype: None
        """
        # TODO: Написать функции для каждого действия.

    def open_user_stash(self) -> None:
        """
        Открыть тайник игрока.

        :rtype: None
        """

    def where_are_sextants_in_inventory(self) -> list[int]:
        pass

    def where_are_compasses_in_inventory(self) -> list[int]:
        pass

    def where_are_charged_compasses_in_inventory(self) -> list[int]:
        pass
