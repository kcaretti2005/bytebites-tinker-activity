# ByteBites models
# Customer: a person who uses ByteBites.
# Stores name and purchase_history.
# MenuItem: one food item for sale. Stores name, price, category, popularity_rating.
# Menu: the collection of all MenuItems. Filters items by category.
# Transaction: one purchase. Stores the selected items and computes the total cost.


class MenuItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self, items: list[MenuItem] | None = None):
        self.items = items if items is not None else []


class Transaction:
    def __init__(self, items: list[MenuItem]):
        self.items = items


class Customer:
    def __init__(self, name: str, purchase_history: list[Transaction] | None = None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

if __name__ == "__main__":
    burger = MenuItem("Spicy Burger", 10.0, "Mains", 4.5)
    soda = MenuItem("Large Soda", 5.0, "Drinks", 4.0)
    menu = Menu([burger, soda])
    order = Transaction([burger, soda])
    ana = Customer("Ana", [order])
    print(ana.name, len(ana.purchase_history), len(order.items), len(menu.items))