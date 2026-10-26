# ByteBites models
# Customer: a person who uses ByteBites.
# Stores name and purchase_history.
# MenuItem: one food item for sale. Stores name, price, category, popularity_rating.
# Menu: the collection of all MenuItems. Filters items by category and sorts them by price or popularity.
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

    def filter_by_category(self, category: str) -> list[MenuItem]:
        return [item for item in self.items if item.category == category]

    def sort_by_price(self) -> list[MenuItem]:
        return sorted(self.items, key=lambda item: item.price)

    def sort_by_popularity(self) -> list[MenuItem]:
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    def __init__(self, items: list[MenuItem]):
        self.items = items

    def compute_total(self) -> float:
        return sum(item.price for item in self.items)


class Customer:
    def __init__(self, name: str, purchase_history: list[Transaction] | None = None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

if __name__ == "__main__":
    burger = MenuItem("Spicy Burger", 10.0, "Mains", 4.5)
    soda = MenuItem("Large Soda", 5.0, "Drinks", 4.0)
    cake = MenuItem("Cake", 6.0, "Desserts", 3.5)
    menu = Menu([burger, soda, cake])
    print([i.name for i in menu.filter_by_category("Drinks")])
    print([i.name for i in menu.sort_by_price()])
    print([i.name for i in menu.sort_by_popularity()])
    print(Transaction([burger, soda]).compute_total())
    print(Transaction([]).compute_total())