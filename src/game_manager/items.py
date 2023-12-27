from dataclasses import dataclass, field
from abc import ABC
from loguru import logger


@dataclass
class Item (ABC):
    amount: int
    stack_size: int

    def __post_init__(self) -> None:
        logger.debug(f"Был создан {self.__class__.__name__}({self.amount})")
        if self.amount > self.stack_size:
            raise ValueError(
                f"amount({self.amount}) не должно быть больше stack_size({self.stack_size})!"
            )

        elif self.amount < 0:
            raise ValueError(
                f"amount({self.amount}) не может быть отрицательным!"
            )


@dataclass
class Sextant (Item):
    stack_size: int = field(default=10, init=False, repr=False)


@dataclass
class Compass (Item):
    stack_size: int = field(default=10, init=False, repr=False)


@dataclass
class ChargedCompass (Item):
    stack_size: int = field(default=1, init=False, repr=False)
