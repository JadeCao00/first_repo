import json

numbers = [1, 3, 6, 9, 7]

filename = 'number.json'
with open(filename, 'w') as f:
# 函数json.dump()接受两个实参：要存储的数据，以及可用于存储数据的文件对象。
    json.dump(numbers, f)