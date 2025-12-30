class Product:
    def __init__(self, name, price, quantity):
        try:
            self._name = str(name)
            self._price = float(price)
            self._quantity = int(quantity)
        except TypeError:
            print("Missing inputs!")
        except ValueError:
            print("Wrong values!")

    def get_quantity(self):
        return self._quantity

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def set_quantity(self, quantity):
        try:
            if not quantity or quantity < 0:
                raise ValueError
            self._quantity = quantity
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

    def show(self):
        print(f"{self._name}, Price: {self._price}, Quantity: {self._quantity}")

    def buy(self, quantity):
        if self._quantity >= quantity:
            try:
                if quantity < 1:
                    raise ValueError
                self._quantity -= quantity
                if self._quantity == 0:
                    self.deactivate()
                return round(self._price * quantity, 2)
            except ValueError or TypeError:
                print("Please enter a valid integer")
        else:
            print(f"Not enough left in stock. remaining: {self._quantity}")
            return None


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self._name = name

    def show(self):
        print(f"{self._name}, Price: {self._price}")

    def get_quantity(self):
        return 0

    def set_quantity(self, quantity):
        return 0

    def buy(self, quantity):
        try:
            if quantity < 1:
                raise ValueError
            return self._price * int(quantity)
        except TypeError or ValueError:
            print("Error, No valid amount!")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.__maximum = maximum

    def show(self):
        print(f"{self._name}, Price: {self._price}, Quantity: {self._quantity}, maximum: {self.__maximum}")

    def get_max(self):
        return self.__maximum

    def buy(self, quantity):
        if self.__maximum >= quantity > 1:
            try:
                if quantity < 1:
                    raise ValueError
                new_quantity = self._quantity - quantity
                self.set_quantity(new_quantity)
                if self._quantity == 0:
                    self.deactivate()
                return round(self._price * quantity, 2)
            except ValueError or TypeError:
                print("Please enter a valid amount!")
        else:
            print(f"Only {self.__maximum} allowed, per purchase!")
            return None

