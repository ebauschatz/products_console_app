from itertools import product
from turtle import title
from urllib import request
import console_display
import json
import requests

def display_menu():
    base_url = 'http://127.0.0.1:8000/api/products/'
    console_display.clear_console()
    user_quit = False
    while user_quit is False:
        console_display.display_menu_options()
        user_option = int(input('Please enter the number of your selection: '))
        if user_option == 0:
            user_quit = True
            break
        elif user_option == 1:
            get_all_products(base_url)
        elif user_option == 2:
            get_product_by_id(base_url)
        elif user_option == 3:
            update_product_by_id(base_url)
        elif user_option == 4:
            delete_product_by_id(base_url)
        elif user_option == 5:
            add_new_product(base_url)

def get_all_products(base_url):
    response = requests.get(base_url)
    products = response.json()
    for product in products:
        console_display.display_all_product_details(product)

def get_product_by_id(base_url):
    product_id = console_display.get_product_id('view')
    api_url = base_url + product_id + '/'
    response = requests.get(api_url)
    product = json.loads(response.content)
    console_display.display_all_product_details(product)

def update_product_by_id(base_url):
    product_data = console_display.get_product_information_from_user()
    product_id = console_display.get_product_id('update')
    api_url = base_url + product_id + '/'

    response = requests.put(api_url, json=product_data)
    new_product = json.loads(response.content)
    console_display.display_all_product_details(new_product)

def delete_product_by_id(base_url):
    product_id = console_display.get_product_id('delete')
    api_url = base_url + product_id + '/'
    response = requests.delete(api_url)
    if response.status_code == 204:
        print('\nProduct successfully deleted')
    else:
        print(f'\nSomething went wrong, the request returned status code {response.status_code}')

def add_new_product(base_url):
    product_data = console_display.get_product_information_from_user()

    response = requests.post(base_url, json=product_data)
    new_product = json.loads(response.content)
    console_display.display_all_product_details(new_product)
