from student import stud
from teacher import teach
from login_st import enter_st
from login_t import enter_t

def menu():
    while True:
        print("1. - Студент.")
        print("2. - Преподаватель.")
        print("3. - Выход.")
        number = input("Выберете пункт меню: ")
        if number == "1":
            enter_st()             #логин и пароль
            stud()                   # меню студента
        elif number == "2":
            enter_t()               #логин и пароль 
            teach()                  # меню преподаввателя
        elif number == "3":
            print("Всего доброго! ")
            break
        else:
            print("Введите пункт из меню: ")
# menu()                            