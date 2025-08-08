shopping_list = []
shopping_list.append("键盘")
shopping_list.append("键帽")
shopping_list.remove("键盘")
shopping_list.append("音响")
shopping_list.append("耳机")
shopping_list[1] = "硬盘"

# print(shopping_list)
# print(len(shopping_list))
# print(shopping_list[0])

price = [599, 1299, 399, 899]
max_price = max(price)
min_price = min(price)
sorted_price = sorted(price)
print(max_price)
print(min_price)
print(sorted_price)