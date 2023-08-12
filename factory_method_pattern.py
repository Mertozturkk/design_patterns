# factory method pattern example


from abc import ABCMeta, abstractmethod


class Coffee(metaclass=ABCMeta):
    @abstractmethod
    def get_coffee(self):
        pass

    @abstractmethod
    def add_milk(self):
        pass

    @abstractmethod
    def add_sugar(self):
        pass


class Latte(Coffee):
    def get_coffee(self):
        print("Get a latte")

    def add_milk(self):
        print("Add milk")

    def add_sugar(self):
        print("Add sugar")


class Cappuccino(Coffee):
    def get_coffee(self):
        print("Get a cappuccino")

    def add_milk(self):
        print("Add milk")

    def add_sugar(self):
        print("Add sugar")


class CoffeeStore(metaclass=ABCMeta):

    @abstractmethod
    def _create_coffee(self, coffee_type):
        pass

    def order(self, coffee_type):
        coffee = self._create_coffee(coffee_type)
        coffee.get_coffee()
        coffee.add_milk()
        coffee.add_sugar()
        return coffee


class Starbucks(CoffeeStore):
    def _create_coffee(self, coffee_type):
        if coffee_type == "latte":
            return Latte()
        elif coffee_type == "cappuccino":
            return Cappuccino()
        else:
            raise ValueError("Invalid coffee type")


class Petra(CoffeeStore):
    def _create_coffee(self, coffee_type):
        if coffee_type == "latte":
            return Latte()
        elif coffee_type == "cappuccino":
            return Cappuccino()
        else:
            raise ValueError("Invalid coffee type")


if __name__ == "__main__":
    starbucks = Starbucks()
    petra = Petra()
    latte = starbucks.order("latte")
    cappuccino = petra.order("cappuccino")
