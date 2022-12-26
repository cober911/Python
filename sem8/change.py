# Замена доманего задания
def change_homework(): 

    with open("homework_base.txt", "r", encoding="utf-8") as file:
        onstring = file.read().split("\n")        
        di = {}
        for item in onstring:
            key = item.split(" ")[0]
            value = item.split(" ")[1:]
            di[key] = value   

        sub = input("Ввведите предмет, по которому хотите изменить домашнее задание: ")
        if sub not in di:
            print("Такого предмета нет в списки")
        else:
            hw = input("Введите текст нового домашнего задания ")
            hw = hw.split(" ")                  
            addon = {sub : hw}
            di.update(addon)
            
    with open('homework_base.txt','w', encoding='utf-8') as f_1:
        for k,v in di.items():
            v = ' '.join(v)           
            s = (k) + " " + (v)
            print(s)
            f_1.write(s +'\n')

# change_homework()

# Замена преподавателя 

def teacher_change():          

    with open("teacher_base.txt", "r", encoding="utf-8") as file:
        onstring = file.read().split("\n")        
        di = {}
        for item in onstring:
            key = item.split(" ")[0]
            value = item.split(" ")[1:]
            di[key] = value   

        sub = input("Преподавателья какого предмета вы хотитее поменять в списке? ")
        if sub not in di:
            print("Этого предмета нет в списке") 
        else:
            hw = input("Введите ФИО нового преподавателя ")           
            hw = hw.split(" ")         
            addon = {sub: hw}
            di.update(addon)
                    
        with open('teacher_base.txt','w', encoding='utf-8') as f_1:
            for k,v in di.items():
                v = ' '.join(v)           
                s = str(k) + " " + str(v)
                print(s)
                f_1.write(s +'\n')

# teacher_change() 

#Замена ученика
def student_change(): 
    with open("student_base.txt", "r", encoding="utf-8") as file:
        onstring = file.read().split("\n")        
        di = {}
        for item in onstring:
            key = item.split(" ")[0]
            value = item.split(" ")[1:]
            di[key] = value   

        num = input("Введите порядковый номер ученика, ФИО которого хотите изменить ")
        if num not in di:
            print("Ученика под таким порядковым номером нет") 
        else:
            hw = input("Введите новое ФИО ") 
            hw = hw.split(" ")          
            addon = {num : hw}
            di.update(addon)
            
        with open('student_base.txt','w', encoding='utf-8') as f_1:
            for k,v in di.items():
                v = ' '.join(v)           
                s = (k) + " " + (v)
                print(s)
                f_1.write(s +'\n')