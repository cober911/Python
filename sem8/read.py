# Просмотр списка домашнего задания с предметами
def read_homework_base():
    with open("homework_base.txt", "r", encoding="utf-8") as file:
        print (file.read())

# read_homework_base()

# Просмотр домашнего задания по выбранному предмету
def find_homework(): 
    sub = input("Ввведите предмет, по которому хотите просмотреть домашнее задание: ")  
    with open("homework_base.txt", "r", encoding="utf-8") as file:
        onstring = file.read().split("\n")        
        dict = {}
        for item in onstring:
            key = item.split(" ")[0]
            value = item.split(" ")[1:]
            dict[key] = value   
        if sub not in dict:
            print("Такого предмета нет")
        else:
            dict.get(sub)
            print(" ".join(dict[sub]))       


# find_homework()

#Вызов списка предметов    
def read_subject_base():    
        with open("homework_base.txt", "r", encoding="utf-8") as file:
            onstring = file.read().split("\n")        
            dict = {}
        for item in onstring:
            key = item.split(" ")[0]
            value = item.split(" ")[1:]
            dict[key] = value
        for key in dict:
            print(key)

# read_subject_base()  

# Вызов списка учителей
def read_teacher_base():      
    with open ("teacher_base.txt", "r", encoding="utf-8") as tb:        
        print(tb.read())

# read_teacher_base()


# Вызов списка студентов
def read_student_base():    
    with open ("student_base.txt", "r", encoding="utf-8") as stb:        
        print(stb.read())
        