#!/bin/python3.11

import os
#os.system('clear')

shoes = {'name': 'Fancy Shoes', 'price': 14900}

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

apply_discount(shoes, 0.25)

