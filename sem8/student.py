from read import *




def stud():
    while True:
        print("1. - Посмотреть предметы.")

        print("2. - Посмотреть список предметов со всеми домашними заданиями: ")

        print("3. - Узнать домашнее задание по выбранному предмету")

        print("4. - Узнать список преподавателей")

        print("5. - Узнать список учеников")

        print("6. - Выход.")
        number_1 = input("Выберете пункт меню: ")
        if number_1 == "1":
            read_subject_base()
        elif number_1 == "2":
            read_homework_base()
        elif number_1 == "3":
            find_homework()
        elif number_1 == "4":
            read_teacher_base()
        elif number_1 == "5":
            read_student_base()
        elif number_1 == "6":
            print("Всего доброго! ")
            break           
        else:
            print("Введите пункт из меню: ")    
