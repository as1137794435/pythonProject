# 主程序入口
from StudentManagementSystem.student_manager import StudentManager


def main():
    s1 = StudentManager()
    while True:
        StudentManager.show_info()
        num = int(input('please enter the number:'))
        s1.choose_option(num)
        input()
main()

