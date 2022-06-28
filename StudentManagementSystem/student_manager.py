from StudentManagementSystem.student import Student


class StudentManager(object):

    def __init__(self):
        self.students_list = []

    @staticmethod
    def show_info():
        print('Please select the following functions----------')
        print('1:Add student')
        print('2:Delete student')
        print('3:Modify student information')
        print('4:Query student information')
        print('5:Display all student information')
        print('6:Save student information')
        print('7:log out')

    def choose_option(self, num):
        if num == 1:
            self.add_student_info()
        elif num == 2:
            self.delete_student_info()
        elif num == 3:
            self.modify_student_info()
        elif num == 4:
            self.search_student_info()
        elif num == 5:
            self.show_all_student_info()
        elif num == 6:
            self.save_student_info()
        elif num == 7:
            self.exit_program()
        else:
            print('Input program error')

    def add_student_info(self):
        student_id = input('Please enter the ID of the student you want to add:')
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                print('The ID already exists and cannot be added')
                return

        else:
            name = input('Please enter the name of the student you want to add:')
            age = input('Please enter the age of the student you want to add:')
            s1 = Student(student_id, name, age)
            self.students_list.append(s1)
            print('Add successful')

    def delete_student_info(self):
        student_id = input('Please enter the ID of the student you want to delete:')
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                self.students_list.remove(student_info)
                print('Delete successful')
                return
        else:
            print('This student does not exist')

    def modify_student_info(self):
        student_id = input('Please enter the ID of the student you want to modify:')
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                name = input('new name:')
                age = input('new age:')
                student_info.name = name
                student_info.age = age
                print('modify successful')
                return
        else:
            print('No such student was found')

    def search_student_info(self):
        student_id = input('Please enter the ID of the student you want to search:')
        for student_info in self.students_list:
            if student_info.student_id == student_id:
                print(student_info)
                return
        else:
            print('No such student was found')

    def show_all_student_info(self):
        for student_info in self.students_list:
            print(student_info)

    def save_student_info(self):
        file = open('student_info.txt', 'a')
        for student_info in self.students_list:
            file.write(str(student_info.__dict__) + '\n')
        file.close()
        print('save successful')

    def load_student_info(self):
        file = open('student_info.txt', 'r')
        while True:
            content = file.readline()
            if content == '':
                break
#Dictionary type string is converted to dictionary
#The dictionary prefix +** can be converted to this type of keyword argument assignment for the key = value
            dict1 = eval(content)
            s1 = Student(**dict1)
            self.students_list.append(s1)
        file.close()

    def exit_program(self):
        self.save_student_info()
        exit()
