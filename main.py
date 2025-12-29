from _Classes import products, store


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
        item.show()
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
    products = store_obj.get_all_products()
    while True:
        list_products(store_obj)
        print("When you want to finish order, enter empty text.")
        user_choice = input("Which product # do you want? ")
        amount = input("What amount do you want? ")
        if not user_choice and not amount:
            total_price = store_obj.order(shopping_list)
            break
        try:
            amount = int(amount)
            if amount < 0:
                raise Exception
            product_choice = products[int(user_choice)-1]
            product_quantity = product_choice.get_quantity()
            if amount > product_quantity:
                print(f"Error: Only {product_quantity} Items left in stock.")
                continue
            shopping_list.append((product_choice, amount))
            product_choice.set_quantity(product_quantity - amount)
            print(f"Added {product_choice.get_name()} {amount} times.")
        except Exception:
            print("Error adding product!")
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
    quit()



def main():
    """ Setup initial stock of inventory and start() the store_menu """
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    # Enter store-menu of Store-class-object
    start(best_buy)


if __name__=="__main__":
    main()
