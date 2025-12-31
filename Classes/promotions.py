from abc import ABC

class Promotion(ABC):
    def __init__(self, name):
        self._name = name

    def apply_promotion(self, product, quantity):
        pass

    def get_name(self):
        return self._name

class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        price = product.get_price() * quantity
        reduced_articles = quantity // 2
        reduced_price = (reduced_articles * product.get_price()) / 2
        return round(price - reduced_price, 2)

class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        price = product.get_price() * quantity
        reduced_articles = quantity // 3
        reduced_price = reduced_articles * product.get_price()
        return round(price - reduced_price, 2)

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.__percent = percent

    def get_percent(self):
        return self.__percent

    def apply_promotion(self, product, quantity):
        price = product.get_price() * quantity
        promotion = product.get_promotion()
        reduced_price = (promotion.get_percent() / 100) * price
        return round(price - reduced_price, 2)