from Best_Buy.Classes import promotions


class Product:
    def __init__(self, name, price, quantity):
        try:
            self._name = str(name)
            self._price = float(price)
            self._quantity = int(quantity)
            self.__promotion = None
        except TypeError:
            print("Missing inputs!")
        except ValueError:
            print("Wrong values!")

    def __str__(self):
        promotion = self.get_promotion()
        if self.__promotion:
            return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}\n ({promotion.get_name()})"
        else:
            return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}"

    def __lt__(self, other):
        return self._price < other._price

    def __gt__(self, other):
        return self._price > other._price

    def get_quantity(self):
        return self._quantity

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_promotion(self):
        return self.__promotion

    def set_promotion(self, promotion):
        if isinstance(promotion, promotions.Promotion):
            self.__promotion = promotion

    def set_quantity(self, quantity):
        try:
            if quantity < 0:
                raise ValueError
            self._quantity = quantity
            if self._quantity == 0:
                self.deactivate()
            if self._quantity > 0 and not self.is_active():
                self.activate()
        except ValueError:
            print("Valid Integer expected!")

    def set_price(self, price):
        try:
            if not price:
                raise ValueError
            self._price = float(price)
        except ValueError:
            print("Float expected!")

    def is_active(self):
        if not "Deactivated" in self._name:
            return True
        else:
            return False

    def deactivate(self):
        if self._quantity == 0:
            self._name = self._name + " (Deactivated)"
        else:
            print("Items left in the Inventory, please remove the items before deactivating!")

    def activate(self):
        if self._quantity > 0:
            self._name.replace(" (Deactivated)", "")
        else:
            print("No items in the Inventory. Please add to the inventory before activating!")

    def buy(self, quantity):
        try:
            if quantity < 1 or quantity > self._quantity:
                raise ValueError
            new_quantity = self._quantity - quantity
            self.set_quantity(new_quantity)
            promotion = self.get_promotion()
            if promotion:
                product = self
                discounted_price = promotion.apply_promotion(product=product, quantity=quantity)
                return discounted_price
            else:
                return round(self._price * quantity, 2)
        except ValueError or TypeError:
            print("Please enter a valid amount!")


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self._name = name

    def __str__(self):
        promotion = self.get_promotion()
        if promotion:
            return f"{self._name}, Price: {self._price}\n ({promotion.get_name()})"
        else:
            return f"{self._name}, Price: {self._price}"

    def get_quantity(self):
        return 0

    def set_quantity(self, quantity):
        return 0

    def buy(self, quantity):
        try:
            promotion = self.get_promotion()
            if promotion:
                product = self
                return promotion.apply_promotion(product=product, quantity=quantity)
            else:
                return round(self._price * quantity, 2)
        except ValueError or TypeError:
            print("Please enter a valid amount!")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.__maximum = maximum

    def __str__(self):
        promotion = self.get_promotion()
        if promotion:
            return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}, maximum: {self.__maximum}\n ({promotion.get_name()})"
        else:
            return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}, maximum: {self.__maximum}"

    def get_max(self):
        return self.__maximum

    def buy(self, quantity):
        if self.__maximum >= quantity > 1:
            return super().buy(quantity)
        else:
            print(f"Only {self.__maximum} allowed, per purchase!")
            return None

