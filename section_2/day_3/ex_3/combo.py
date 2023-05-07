from abc import ABC, abstractmethod
from menu_items import ItemFries, ItemHamburger, ItemIceCream


class Combo(ABC):
    def __init__(self):
        self.item_list = []
        self.create_combo()

    @abstractmethod
    def create_combo():
        pass

    def show_item_list(self):
        return self.item_list

    def add_item(self, item):
        self.item_list.append(item)


class EverythingCombo(Combo):
    def create_combo(self):
        self.add_item(ItemHamburger())
        self.add_item(ItemIceCream())
        self.add_item(ItemFries())


class HappyCombo(Combo):
    def create_combo(self):
        self.add_item(ItemHamburger())
        self.add_item(ItemFries())


class IceCombo(Combo):
    def create_combo(self):
        self.add_item(ItemHamburger())
        self.add_item(ItemIceCream())


class FriesCombo(Combo):
    def create_combo(self):
        self.add_item(ItemHamburger())
        self.add_item(ItemFries)


if __name__ == "__main__":
    selected_combo = input("What's your order: [EverythingCombo, HappyCombo, IceCombo]")

    combo = eval(selected_combo)()

    print(f"\nCreating {type(combo).__name__} combo.")
    print(f"Combo created with the following items: {combo.show_item_list()}")
