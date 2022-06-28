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
            self.show_student_info()
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


    def delete_student_info(self):
        print('delete student')

    def modify_student_info(self):
        print('modify student')

    def search_student_info(self):
        print('search student')

    def show_student_info(self):
        print('show all student')

    def save_student_info(self):
        print('save student')

    def exit_program(self):
        print('exit program')
