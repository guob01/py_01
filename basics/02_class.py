# class CuteCat:
#     def __init__(self, cat_name, cat_age, cat_color):
#         self.name = cat_name
#         self.age = cat_age
#         self.color = cat_color
#
#     def speak(self):
#         print("喵" * self.age)
#
#     def think(self, content):
#         print(f"小猫{self.name}在思考{content}...")
#
# cat1 = CuteCat("Jojo",2,"black")
# print(f"小猫{cat1.name}的年龄是{cat1.age},花色是{cat1.color}")
# cat1.speak()
# cat1.think("现在去抓沙发还是抓窗帘")

# 定义一个学生类
# 要求
# 1.属性包括学生姓名,学号,以及语数英三科成绩
# 2.能够设置学生某个科目的成绩
# 3.能够打印出该学生的所有科目的成绩

# class Student:
#     def __init__(self,stu_name,stu_id):
#         self.name = stu_name
#         self.id = stu_id
#         self.grades = {"语文": 0, "数学": 0, "英语": 0}
#
#     def set_grade(self,course,grade):
#         if course in self.grades:
#             self.grades[course] = grade
#
#     def print_grades(self):
#         print(f"学生{self.name}(学号:{self.id})的成绩为:")
#         for course in self.grades:
#             print(f"{course}:{self.grades[course]}分")
#
# chen = Student("小陈",1)
# # zeng = Student("小张",2)
#
# chen.set_grade("数学",95)
# chen.set_grade("语文",80)
# chen.set_grade("英语",92)
# print(chen.print_grades())


# 继承(类继承练习:人力系统)
# 员工分为两类:全职员工 FullTimeEmployee ,兼职员工 PartTimeEmployee
# 全职和兼职都有"姓名 name","工号 id"属性
# 都具有"打印信息 print_info"(打印姓名,工号)方法
# 全职有"月薪 monthly_salary"属性
# 兼职有"日新 daily_salary","每月工作天数 work_days"属性
# 全职和兼职都有"计算月薪 calculate_salary"的方法,但具体计算过程不一样
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工姓名:{self.name},员工工号:{self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)  # 引用父类
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_salary(self):
        return self.daily_salary * self.work_days


zhang = FullTimeEmployee("小张", "z01", 8000)
li = PartTimeEmployee("小李", "l01", 200, 20)

zhang.print_info()
li.print_info()

print(zhang.calculate_salary())
print(li.calculate_salary())
