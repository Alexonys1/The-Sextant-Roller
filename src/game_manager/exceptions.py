class InventoryCellIsEmpty (Exception):
    def __init__(self, cell_number: int):
        self.cell_number = cell_number

    def __repr__(self) -> str:
        return f"Клетка инвентаря №{self.cell_number} пуста!"


class IncorrectInventoryCellNumber (Exception):
    def __init__(self, cell_number: int):
        self.cell_number = cell_number

    def __repr__(self) -> str:
        return f"Ячейки №{self.cell_number} нет в инвентаре! В нём есть только ячейки от 1 до 60."
