from typing import Type, Optional

from game_manager.singleton import Singleton
from game_manager.items import Item, Sextant, Compass, ChargedCompass


# TODO: Use loguru!!!
class Inventory (metaclass=Singleton):
    """
    Класс инвентаря, хранящий в себе информацию о ячейках в нём в виде:
    номер ячейки - содержимое. Всего есть 60 ячеек.
    В инвентаре 12 столбцов по 5 строк в каждом.
    """
    def __init__(self):
        self._inventory_cells = {num: None for num in range(1, 61)}

    def select_using_item(self, cell_number: int) -> None:
        """
        Запомнить предмет, который использует игрок правой кнопкой мыши.

        :param cell_number: Номер ячейки инвентаря (1-60).
        :type cell_number: int

        :raises InventoryCellIsEmpty: если ячейка пуста.
        :raises IncorrectInventoryCellNumber: если нет такой ячейки.

        :rtype: None
        """

    def unselect_using_item(self) -> None:
        """
        Забыть предмет, используемый игроком правой кнопкой мыши.

        :raises ItemIsNoSelected: если не было выделенного (запомненного) предмета.

        :rtype: None
        """

    def minus_one_using_item(self) -> None:
        """
        Отнимает один выделенный предмет. Если стак предметов уже не существует,
        то отнимается один следующий предмет (если он есть), затем ещё
        следующий и ещё, и ещё. Когда будет отнят предмет у последнего стака,
        предметы будут отниматься по единице, начиная с первого.

        :raises ItemsHaveRunOut: когда закончились предметы в инвентаре.

        :rtype: None
        """


    def put_sextant_stack(self, cell_number: Optional[int]) -> None:
        """
        Положить стак секстантов в ячейку инвентаря. Если не указать
        номер ячейки, то секстанты поместятся в инвентарь автоматически.

        :param cell_number: номер ячейки инвентаря.
        :type cell_number: Optional[int]

        :raises IncorrectInventoryCellNumber: если нет такой ячейки.

        :rtype: None
        """

    def put_compass_stack(self, cell_number: Optional[int]) -> None:
        """
        Положить компасы в ячейку инвентаря. Если не указать номер ячейки,
        то компасы поместятся в инвентарь автоматически.

        :param cell_number: номер ячейки инвентаря.
        :type cell_number: Optional[int]

        :raises IncorrectInventoryCellNumber: если нет такой ячейки.

        :rtype: None
        """


    def remove_sextant_stack(self, cell_number: int) -> None:
        """
        Удалить весь стак секстантов в указанной ячейке.

        :param cell_number: номер ячейки инвентаря.
        :type cell_number: int

        :raises IncorrectInventoryCellNumber: если нет такой ячейки.

        :rtype: None
        """

    def remove_compass_stack(self, cell_number: int) -> None:
        """
        Удалить весь стак компасов в указанной ячейке.

        :param cell_number: номер ячейки инвентаря.
        :type cell_number: int

        :raises IncorrectInventoryCellNumber: если нет такой ячейки.

        :rtype: None
        """

    def remove_charged_compass_stack(self, cell_number: int) -> None:
        """
        Удалить весь стак заряженных компасов в указанной ячейке.

        :param cell_number: номер ячейки инвентаря.
        :type cell_number: int

        :raises IncorrectInventoryCellNumber: если нет такой ячейки.

        :rtype: None
        """


    def get_cell_numbers_of_sextants(self) -> list[int]:
        """
        Получить номера всех ячеек, где есть секстанты.

        :rtype: list[int]
        """
        return self._get_cell_numbers_of(Sextant)

    def get_cell_numbers_of_compasses(self) -> list[int]:
        """
        Получить номера всех ячеек, где есть компасы.

        :rtype: list[int]
        """
        return self._get_cell_numbers_of(Compass)

    def get_cell_numbers_of_charged_compasses(self) -> list[int]:
        """
        Получить номера всех ячеек, где есть заряженные компасы.

        :rtype: list[int]
        """
        return self._get_cell_numbers_of(ChargedCompass)


    def get_number_of_first_found_sextant(self) -> Optional[int]:
        """
        Получить номер первого найденного секстанта (если он есть).

        :rtype: Optional[int]
        """
        return self._get_cell_number_of_first_found(Sextant)

    def get_number_of_first_found_compass(self) -> Optional[int]:
        """
        Получить номер первого найденного компаса (если он есть).

        :rtype: Optional[int]
        """
        return self._get_cell_number_of_first_found(Compass)

    def get_number_of_first_found_charged_compass(self) -> Optional[int]:
        """
        Получить номер первого найденного заряженноо компаса (если он есть).

        :rtype: Optional[int]
        """
        return self._get_cell_number_of_first_found(ChargedCompass)


    def _get_cell_numbers_of(self, item_type: Type[Item]) -> list[int]:
        """
        Возвращает номера ячеек с указанным типом предмета.

        :param item_type: тип предмета, наследованный от Item.
        :type item_type: Type[Item]

        :rtype: list[int]
        """

    def _get_cell_number_of_first_found(self, item_type: Type[Item]) -> Optional[int]:
        """
        Возвращает номер первого найденного предмета.

        :param item_type: тип предмета, наследованный от Item.
        :type item_type: Type[Item]

        :rtype: Optional[int]
        """
        cell_numbers = self._get_cell_numbers_of(item_type)

        if cell_numbers:
            return min(cell_numbers)  # Минимальный, значит - первый.
        else:
            return None
