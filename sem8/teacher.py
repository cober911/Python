from read import *
from add import *
from change import *




def teach():
    while True:
        print()
        
        print("1. - Посмотреть предметы.")               

        print("2. - Посмотреть список предметов со всеми домашними заданиями: ")

        print("3. - Добавить новый предмет с домашним заданием ")

        print("4. - Добавление домашнего задания к уже существующему")

        print("5. - Замена доманего задания")

        print("6. - Узнать список преподавателей")

        print("7. - Добавить новый предмет и преподавателя")

        print("8. - Добавить преподавателя к существующему предмету")

        print("9. - Заменить преподавателя по выбранному предмету")

        print("10. - Посмотреть список учеников")

        print("11. - Добавить нового ученика")

        print("12. - Заменить ученика")

        print("13. - Выход.")
        number_1 = input("Выберете пункт меню: ")
        if number_1 == "1":
            read_subject_base()
        elif number_1 == "2":
            read_homework_base()
        elif number_1 == "3":
            add_subject_with_hw()
        elif number_1 == "4":
            add_hw()
        elif number_1 == "5":
            change_homework()
        elif number_1 == "6":
            read_teacher_base()
        elif number_1 == "7":
            add_subject_with_teacher()
        elif number_1 == "8":
            add_teacher()
        elif number_1 == "9":
            teacher_change()
        elif number_1 == "10":
            read_student_base()
        elif number_1 == "11":
            add_student()
        elif number_1 == "12":
            student_change()
        elif number_1 == "13":
            print("Всего доброго! ")
            break           
        else:
            print("Введите пункт из меню: ") 