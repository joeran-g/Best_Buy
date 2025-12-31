class Store:
    def __init__(self, products=None):
        if products is None:
            products = []
        try:
            self.products = products
        except ValueError:
            print("Enter a valid Product!")

    def add_product(self, product):
        try:
            self.products.append(product)
        except ValueError or TypeError:
            print("Enter a product to append to the list")

    def remove_product(self, product):
        try:
            if product in self.products:
                self.products.remove(product)
        except ValueError or TypeError:
            print("Product not found. Please enter a product from the .products list")

    def get_total_quantity(self):
        """ return the total quantity(int) of Products from a Store """
        total_amount = 0
        if not self.products:
            return 0
        for product in self.products:
            total_amount += product.get_quantity()
        return total_amount

    def get_all_products(self):
        """ return a list of Products from a Store """
        if self.products:
            return [product for product in self.products]
        return []

    def order(self, shopping_list):
        total_price = 0.0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
                if product.get_quantity() == 0:
                    self.remove_product(product)
            except TypeError or ValueError:
                print(f"{product.get_name()} could not be found in store.")
        return total_price