import os

def display_menu_options():
    print('''\nBelow are the options for interacting with products:
    0 - Quit
    1 - View All Products
    2 - View A Product By ID
    3 - Update A Product By ID
    4 - Delete A Product By ID
    5 - Add A New Product''')

def display_all_product_details(product):
    print()
    for key, value in product.items():
        print(f'{key.replace("_", " ").title()}: {value}')

def get_product_information_from_user():
    product_data = {}
    product_data['title'] = input('Please enter the new product title: ')
    product_data['description'] = input('Please enter the new product description: ')
    product_data['price'] = input('Please enter the new product price: ')
    product_data['inventory_quantity'] = input('Please enter the new product inventory quantity: ')
    product_data['image_link'] = input('Please enter the new product image link: ')
    return product_data

def get_product_id(purpose):
    return input(f'Please enter the ID of the product to {purpose}: ')

def clear_console():
    os.system('cls' if os.name == 'nt' else "clear")