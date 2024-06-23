# Strategy Pattern

from abc import ABC, abstractmethod


class CoffeeStrategy(ABC):
    @abstractmethod
    def brew(self):
        pass


class Espresso(CoffeeStrategy):
    def brew(self):
        print("Brewing Espresso")


class Latte(CoffeeStrategy):
    def brew(self):
        print("Brewing Latte")


class Cappuccino(CoffeeStrategy):
    def brew(self):
        print("Brewing Cappuccino")


class CoffeeMachine:
    def __init__(self, strategy: CoffeeStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CoffeeStrategy):
        self.strategy = strategy

    def brew(self):
        self.strategy.brew()


espresso = Espresso()
latte = Latte()
cappuccino = Cappuccino()

machine = CoffeeMachine(espresso)
machine.brew()

machine.set_strategy(latte)
machine.brew()

machine.set_strategy(cappuccino)
machine.brew()
