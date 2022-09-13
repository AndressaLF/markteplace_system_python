from hashlib import new
from time import sleep
from typing import Dict, List

from models.product import Product
from utils.helper import format_price_float_str

products: List[Product] = []  # product list
# list of dictionary  [key = Product, quantity = int]
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=====================================')
    print('============== Welcome ==============')
    print('============ Marketplace ============')
    print('=====================================')

    print('Choose an option below:')
    print('1 - Register a product')
    print('2 - Product List')
    print('3 - Buy a product')
    print('4 - Show cart')
    print('5 - End Order')
    print('6 - Exit System')

    option: int = int(input())

    if option == 1:
        register_product()
    elif option == 2:
        list_product()
    elif option == 3:
        buy_product()
    elif option == 4:
        show_cart()
    elif option == 5:
        end_order()
    elif option == 6:
        print('Come back soon! :-)')
        sleep(2)  # await 2s to exit the system
        exit(0)
    else:
        print('Invalid Option.')
        menu()


def register_product() -> None:
    print('Register Products')
    print('=================')

    name: str = input('Name of the product: ')
    price: float = float(input('Price of the product: '))

    product: Product = Product(name, price)
    products.append(product)

    print(f'{product.name} has been registered successfully!')
    sleep(2)
    menu()


def list_product() -> None:
    if len(products) > 0:
        print('Product List')
        print('----------------------------------')

        for product in products:
            print(product)
            print('-------------------------------')
            sleep(1)
    else:
        print('There are no registered products!')
    sleep(2)
    menu()


def buy_product() -> None:
    if len(products) > 0:
        print('Choose product code:')
        print('------------------------------------')

        for item in products:
            print(item)
            print('--------------------------------')
            sleep(1)

        cod: int = int(input())

        product: Product = get_product_from_code(
            cod)  # getting the product by code

        if product:  # If the product exists. It's different from None
            if len(cart) > 0:
                is_in_cart: bool = False
                for item in cart:
                    qtd: int = item.get(product)
                    if qtd:
                        item[product] = qtd + 1
                        print(
                            f'The product, {product.name} has {qtd + 1} units in the cart.')
                        is_in_cart = True
                        sleep(2)
                        menu()
                if not is_in_cart:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'The product, {product.name} was added to cart.')
                    sleep(2)
                    menu()
            else:
                new_product = {product: 1}  # product catch by the code passed
                cart.append(new_product)
                print(f' The product {product.name} was added to the cart.')
                sleep(2)
                menu()
        else:
            print(f'The product with the past code ({cod}) was not found.')
            sleep(2)
            menu()
    else:
        print('There is no product in the system to sell.')
        sleep(2)
        menu()


def show_cart() -> None:
    if len(cart) > 0:
        print('Product in the cart:')

        for item in cart:
            for data in item.items():
                print(data[0])  # Quantity -> int
                print(f'Quantity: {data[1]}')
                print('------------------------------')
                sleep(1)
    else:
        print('There are no products in the cart yet.')
    sleep(2)
    menu()


def end_order() -> None:
    if len(cart) > 0:
        total_price: float = 0

        print('Product in the cart:')
        for item in cart:  # item = Dict[Product, quantity]
            for data in item.items():
                print(data[0])  # Product -> object
                print(f'Quantity: {data[1]}')  # Quantity -> int
                total_price += data[0].price * data[1]
                print('---------------')
                sleep(1)
        print(f'Total: {format_price_float_str(total_price)}')
        print('Come back soon! :-)')
        cart.clear()
        sleep(2)
    else:
        print('There is no product in the cart!')
    sleep(2)
    menu()


def get_product_from_code(cod: int) -> Product:
    p: Product = None  # Product object empty

    for product in products:
        if product.cod == cod:
            p = product
    return p


if __name__ == '__main__':
    main()
