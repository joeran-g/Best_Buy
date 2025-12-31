import sys

from Best_Buy.Classes import promotions, products, store


def show_menu(menu):
    """ Pint a Menu, based on a dictionary"""
    print("\n\tStore Menu\n\t----------")
    for num, choice in menu.items():
        print(f"{num}. {choice[0]}")
    print()


def list_products(store_obj):
    """
    Prints name, price and quantity
    of each product from th store_obj
    """
    counter = 1
    inventory = store_obj.get_all_products()
    print("----------")
    for item in inventory:
        print(counter, end=". ")
        if item.is_active():
            print(item)
        else:
            print("--Out of Stock!--")
        counter += 1
    print("----------")


def show_amount(store_obj):
    """ Print out the sum of all available product.quantities"""
    if not store_obj:
        print("Nothing to show")
    else:
        total_amount = store_obj.get_total_quantity()
        print(f"Total of {total_amount} items in store")


def make_order(store_obj):
    """
    Show Products name, price, quantity.
    Ask for a number from the menu and an amount to buy,
    if the user inputs 2 empty strings, the order is made.
    prints out the total_price of the order.
    """
    shopping_list = []
    all_products = store_obj.get_all_products()
    while True:
        list_products(store_obj)
        print("When you want to finish order, enter empty text.")
        user_choice = input("Which product # do you want? ")
        amount = input("What amount do you want? ")
        product_quantity = None
        product_choice = None
        if not user_choice and not amount:
            total_price = store_obj.order(shopping_list)
            break
        try:
            user_choice = int(user_choice)
            amount = int(amount)
            if amount < 1:
                raise Exception
            product_choice = all_products[int(user_choice) - 1]
            if not isinstance(product_choice, products.NonStockedProduct):
                product_quantity = product_choice.get_quantity()
                if amount > product_quantity:
                    print(f"Error: Only {product_quantity} Items left in stock.")
                    continue
                elif isinstance(product_choice, products.LimitedProduct) and amount > product_choice.get_max():
                    print(f"Error: Can't choose more than {product_choice.get_max()} of this Product per purchase.")
                    continue
                product_choice.set_quantity(product_quantity - amount)
            shopping_list.append((product_choice, amount))
            print(f"Added {product_choice.get_name()} {amount} times.")
        except Exception:
            print("Error adding product!")
            if product_quantity:
                product_choice.set_quantity(product_quantity)
            continue
    print(f"Order made! Total payment: ${total_price}")


def start(store_obj):
    """
    Show a store-menu and let the user choose one option.
    Execute the function from the chosen menu_choice,
    until the user quits the menu.
    """
    menu = {
        1: ("List all products in store", list_products),
        2: ("Show total amount in store", show_amount),
        3: ("Make an order", make_order),
        4: ("Quit", quit)
        }
    print("\n\n-------Welcome to the Store!-------\n")
    user_choice = None
    while not user_choice == len(menu):
        show_menu(menu)
        try:
            user_choice = int(input("Please choose a number: "))
            if 1 <= user_choice < len(menu):
                menu[user_choice][1](store_obj)
            else:
                raise Exception
        except Exception:
            print("Error with your choice! Try again!")
    print("\nBye!")
    sys.exit()



def main():
    """ Setup initial stock of inventory and start() the store_menu """
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    # Enter store-menu of Store-class-object
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__=="__main__":
    main()
