total = 0
count = 0
user_input = input("请输入数字(完成所有输入后,请输入q终止程序):")
while user_input != "q":
    num = float(user_input)
    total += num
    count += 1
    user_input = input("请输入数字(完成所有输入后,请输入q终止程序):")
if count == 0:
    result = 0
else:
    result = total / count
print(f"您输入数字的平均值为:{result}")