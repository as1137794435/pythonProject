# 主程序入口
from StudentManagementSystem.student_manager import StudentManager


def main():

    while True:

        StudentManager.show_info()
        num = int(input('please enter the number:'))
        s1 = StudentManager()
        s1.choose_option(num)
        input()
main()

