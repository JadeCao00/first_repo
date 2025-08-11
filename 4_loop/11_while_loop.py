print("你好，我是一个求平均值的程序。")
total = 0
count = 0
use_input = input("请输入数字（完成所有输入后，请输入q终止程序）：")
while use_input != "q":
    num = float(use_input)
    total += num
    count += 1
    use_input = input("请输入数字（完成所有输入后，请输入q终止程序）：")
if count == 0:
    result = 0
else:
    result = total / count
print("您输入的数字平均值为" + str(result))