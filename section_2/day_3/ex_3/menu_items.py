from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def __repr__(self):
        pass


class ItemHamburger(Item):
    def __repr__(self):
        return "Hamburger"


class ItemIceCream(Item):
    def __repr__(self):
        return "Ice Cream"


class ItemFries(Item):
    def __repr__(self):
        return "Fries"
