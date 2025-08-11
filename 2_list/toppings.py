available_toppings = ['mushroom', 'extra cheese', 'bacon', 'green peppers']
requested_toppings = ['mushroom', 'extra cheese', 'french fries']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')

    else:
        print(f"sorry, we don't have {requested_topping}." )