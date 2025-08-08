def calculate_BMI (weight, height):
    BMI = weight / (height ** 2)
    if BMI <= 18.5:
        category = "偏瘦"
    elif 18.5 < BMI <= 25:
        category = "正常"
    elif 25 < BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"您的BMI分类是：{category}")
    return BMI

result = calculate_BMI(100,1.8)
print(result)