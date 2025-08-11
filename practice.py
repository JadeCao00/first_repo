# car = 'saburu'
# print("Is car == 'saburu'? I predict True.")
# print(car == 'saburu')

# car = 'Saburu'
# if car.lower() == 'saburu':
#     print('True')

# available_toppings = ['mushroom', 'extra cheese', 'bacon', 'green peppers']
# requested_toppings = ['mushroom', 'extra cheese', 'french fries']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f'Adding {requested_topping}.')
#
#     else:
#         print(f"sorry, we don't have {requested_topping}." )

# current_usernames = ['Jason', 'Chole', 'Hailey', 'Peter', 'Fiona']
# new_usernames = ['Nicky', 'Ray', 'Lily', 'peter', 'jason']
#
# # 集合推导式 Set Comprehension
# current_lower = {name.lower() for name in current_usernames}
#
# for username in new_usernames:
#     if username.lower() in current_lower:
#         print(f"Sorry, '{username}' is used. Please type another name.")
#     else:
#         print(f"'{username}' is available")

# 方法get() 第一个参数用于指定键，第二个参数为指定键不存在时要返回的值
# alient_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alient_0.get('points', 'No point value assigned')
# print(point_value)

river_country = {
    'nile' :'egypt',
    'yellow river' : 'china',
    'mississippi': 'america',
}

for river_name, country_name in river_country.items():
    print(f'The {river_name.title()} runs through {country_name.title()}')