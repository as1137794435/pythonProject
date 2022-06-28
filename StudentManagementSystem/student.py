
class Student(object):
    def __init__(self, student_id, name, age):

        self.student_id = student_id
        self.name = name
        self.age = age

    def __str__(self):
        return f'name:{self.name}, ID:{self.student_id}, age:{self.age}'
