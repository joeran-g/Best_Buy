from . import products


def test_creating_prod():
    assert products.Product("Bread", 2.30, 30)

def test_creating_prod_invalid_details():
    assert products.Product(5, 2.30, 30)
    assert products.Product("Bread", "funf", 30)
    assert products.Product("Bread", 2.30, "30")

def test_prod_becomes_inactive():
    prod = products.Product("Bread", 2.30, 30)
    prod.buy(30)
    assert prod.is_active() == False

def test_buy_modifies_quantity():
    quantity = 30
    prod = products.Product("Bread", 2.3, 30)
    prod.buy(20)
    assert prod.get_quantity() != quantity

def test_buy_too_much():
    prod = products.Product("Bread", 2.3, 30)
    assert prod.buy(50) == None