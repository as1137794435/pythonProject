# 定义学员类，创建对象 增加学员信息
class Student(object):
    def __init__(self, student_id, name, age):
        # 创建学院对象,传入信息
        self.student_id = student_id
        self.name = name
        self.age = age

    def __str__(self):
        return f'姓名{self.name}, ID{self.student_id}, 年龄{self.age}'
