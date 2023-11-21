from dataclasses import dataclass, field
from abc import ABC


@dataclass
class Item (ABC):
    amount: int
    stack_size: int

    def __post_init__(self) -> None:
        if self.amount > self.stack_size:
            raise ValueError(
                f"amount ({self.amount}) не должно быть больше stack_size ({self.stack_size})!"
            )

        elif self.amount < 0:
            raise ValueError(
                f"amount ({self.amount}) не может быть отрицательным!"
            )


@dataclass
class Sextant (Item):
    amount: int
    stack_size: int = field(default=10, init=False, repr=False)


@dataclass
class Compass (Item):
    amount: int
    stack_size: int = field(default=10, init=False, repr=False)


@dataclass
class ChargedCompass (Item):
    amount: int
    stack_size: int = field(default=1, init=False, repr=False)


if __name__ == '__main__':
    sextant = Sextant(amount=10)
    print(sextant)
