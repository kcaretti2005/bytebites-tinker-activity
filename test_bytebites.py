from models import MenuItem, Menu, Transaction


def make_menu():
    return Menu([
        MenuItem("Spicy Burger", 10.0, "Mains", 4.5),
        MenuItem("Large Soda", 5.0, "Drinks", 4.0),
    ])


def test_calculate_total_with_multiple_items():
    menu = make_menu()
    assert Transaction(menu.items).compute_total() == 15.0


def test_calculate_total_with_empty_order():
    assert Transaction([]).compute_total() == 0


def test_filter_by_category_returns_only_matching_items():
    drinks = make_menu().filter_by_category("Drinks")
    assert [i.name for i in drinks] == ["Large Soda"]