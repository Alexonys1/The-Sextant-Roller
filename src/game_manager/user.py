from game_manager.singleton import Singleton
from game_manager.inventory import Inventory
from game_manager.data_classes import Point, Region


class User (metaclass=Singleton):
    def __init__(self):
        self._inventory = Inventory()

    def take_item_in_inventory(self, cell_number: int) -> None:
        """
        Берёт предмет из указанной ячейки инвентаря левой кнопкой мыши.

        :param cell_number: Номер ячейки инвентаря (1-60).
        :type cell_number: int

        :raises InventoryCellIsEmpty: если ячейка пуста.

        :rtype: None
        """

    def use_item_in_inventory(self, cell_number: int) -> None:
        """
        Использует указанный предмет правой кнопкой мыши.

        :param cell_number: Номер ячейки инвентаря (1-60).
        :type cell_number: int

        :raises InventoryCellIsEmpty: если ячейка пуста.

        :rtype: None
        """

    def hold_down_shift(self) -> None:
        """Зажимает левый shift."""
        # Событие должно отслеживаться в классе.

    def release_shift(self) -> None:
        """Отжимает левый shift."""
        # Событие должно отслеживаться в классе.

    def move_to_point(self, point: Point, duration: float, dispersion: float = 0) -> None:
        """
        Передвигает курсор мыши в указанную точку. Нужно задать время,
        через которое курсор будет в нужной точке. Можно ввести разброс в координатах
        относительно пункта назначения.

        :param point: точка, куда будет двигаться курсор мыши. Задаётся классом Point.
        :type point: Point

        :param duration: время прохождения пути курсора, указывается в секундах.
        :type duration: float

        :param dispersion: создаёт квадратную область вокрут point, на которую наведётся курсор. Сторона квадрата: 2*dispersion.
        :type dispersion: float

        :raises UncorrectedPoint: если введены несуществующие координаты.

        :rtype: None
        """

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

    def move_to_top_stone_of_void(self) -> None:
        """
        Навести курсор мыши на место ролла секстантов, оно же -
        "Церемониальный камень пустоты", самый верхний камень из четырёх.

        :rtype: None
        """
        # TODO: Написать функции для каждого действия.

    def where_are_sextants_in_inventory(self) -> list[int]:
        pass

    def where_are_compasses_in_inventory(self) -> list[int]:
        pass

    def where_are_charged_compasses_in_inventory(self) -> list[int]:
        pass
