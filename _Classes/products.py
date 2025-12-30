class Product:

    def __init__(self, name, price, quantity):
        try:
            self.name = str(name)
            self.price = float(price)
            self.quantity = int(quantity)
        except TypeError:
            print("Missing inputs!")
        except ValueError:
            print("Wrong values!")

    def get_quantity(self):
        return self.quantity

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_quantity(self, quantity):
        try:
            if not quantity or quantity < 0:
                raise ValueError
            self.quantity = quantity
        except ValueError:
            print("Valid Integer expected!")

    def set_price(self, price):
        try:
            if not price:
                raise ValueError
            self.price = float(price)
        except ValueError:
            print("Float expected!")

    def is_active(self):
        if not "Deactivated" in self.name:
            return True
        else:
            return False

    def deactivate(self):
        if self.quantity == 0:
            self.name = self.name + " (Deactivated)"
        else:
            print("Items left in the Inventory, please remove the items before deactivating!")

    def activate(self):
        if self.quantity > 0:
            self.name.replace(" (Deactivated)", "")
        else:
            print("No items in the Inventory. Please add to the inventory before activating!")

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if self.quantity >= quantity:
            try:
                if quantity < 1:
                    raise ValueError
                self.quantity -= quantity
                if self.quantity == 0:
                    self.deactivate()
                return round(self.price * quantity, 2)
            except ValueError or TypeError:
                print("Please enter a valid integer")
        else:
            print(f"Not enough left in stock. remaining: {self.quantity}")
            return None