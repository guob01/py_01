def calculate_BMI(weight, height):
    BMI = weight / (height ** 2)
    if BMI <= 18.5:
        print('您的体型偏瘦')
    elif BMI <= 25:
        print('您的体型正常')
    elif BMI <= 30:
        print('您的体型偏胖')
    else:
        print('您的体型肥胖')
    return BMI
result = calculate_BMI(63,1.72)
print(result)
