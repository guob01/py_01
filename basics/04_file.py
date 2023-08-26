# 读取文件
# f = open("D:/Users/12828/Desktop/hi.txt", "r", encoding='utf-8')
# print(f.read())
# f.close()

# with open("D:/Users/12828/Desktop/hi.txt", "r", encoding='utf-8') as f:
#     print(f.read())

# 写文件 w
with open("D:/Users/12828/Desktop/hi.txt", "a", encoding='utf-8') as f:
    f.write("hello\n")
    f.write("Yoooo!")
# 追加模式 a

