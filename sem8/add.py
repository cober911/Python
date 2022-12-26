# Добавление нового предмета с дз
def add_subject_with_hw():  
    with open("homework_base.txt", "r", encoding="utf-8") as file:
        onstring = file.read().split("\n")        
        di = {}
        for item in onstring:
            key = item.split(" ")[0]
            value = item.split(" ")[1:]
            di[key] = value   

        sub = input("Добавьте новый предмет: ")        
        if sub in di:
            print("Этот предмет уже в списке") 
        else:
            hw = input("Добавьте домашнее задание ")
            hw = hw.split(" ")             
            addon = {sub : hw}                                                   
            di.update(addon)                        

    with open('homework_base.txt','w', encoding='utf-8') as f_1:
        for k,v in di.items():
            v = ' '.join(v)           
            s = (k) + " " + (v)            
            f_1.write(s +'\n')
 
# add_subject_with_hw()



# Добавление домашнего задания к уже существующему
def add_hw():    
    with open("homework_base.txt", "r", encoding="utf-8") as file:
        onstring = file.read().split("\n")        
        di = {}
        for item in onstring:
            key = item.split(" ")[0]
            value = item.split(" ")[1:]
            di[key] = value   
                                        
        sub = input("Выберите предмет: ")
        if sub not in di:
            print("Этого предмета нет в списке") 
        else:
            hw = input("Добавьте домашнее задание ")              
            di[sub] = di.get(f"{sub}", []) + [f"{hw}"]            
            
        with open('homework_base.txt','w', encoding='utf-8') as f_1:
            for k,v in di.items():
                v = ' '.join(v)           
                s = (k) + " " + (v)
                print(s)
                f_1.write(s +'\n')
# add_hw()

# Добавление нового предмета и преподавателя

def add_subject_with_teacher(): 

    with open("teacher_base.txt", "r", encoding="utf-8") as file:
        onstring = file.read().split("\n")        
        di = {}
        for item in onstring:
            key = item.split(" ")[0]
            value = item.split(" ")[1:]
            di[key] = value   
          
        sub = input("Добавьте новый предмет: ")
        if sub in di:
            print("Этот предмет есть в списке") 
        else:
            hw = input("Введите имя преподавателя ")
            hw = hw.split(" ")             
            addon = {sub : hw}                                                   
            di.update(addon)             

        with open('teacher_base.txt','w', encoding='utf-8') as f_1:
            for k,v in di.items():
                v = ' '.join(v)           
                s = str(k) + " " + str(v)
                print(s)
                f_1.write(s +'\n')
        

# add_subject_with_teacher()

# Добавление учителя к существующему предмету
def add_teacher(): 
    with open("teacher_base.txt", "r", encoding="utf-8") as file:
        onstring = file.read().split("\n")        
        di = {}
        for item in onstring:
            key = item.split(" ")[0]
            value = item.split(" ")[1:]
            di[key] = value                               
        sub = input("Выберите предмет: ")
        if sub not in di:
            print("Этот предмета нет в списке") 
        else:
            fio = input("Напишите ФИО нового преподавателя ")              
            di[sub] = di.get(f"{sub}", []) + [f"{fio}"]            
            
        with open('teacher_base.txt','w', encoding='utf-8') as f_1:
            for k,v in di.items():
                v = ' '.join(v)           
                s = (k) + " " + (v)
                print(s)
                f_1.write(s +'\n')

# add_teacher()

# Добавление нового ученика

def add_student(): 

    with open("student_base.txt", "r", encoding="utf-8") as file:
        onstring = file.read().split("\n")        
        di = {}
        for item in onstring:
            key = item.split(" ")[0]
            value = item.split(" ")[1:]
            di[key] = value           
         
        num = input("Введите порядковый номер нового ученика ")
        if num in di:
            print("Этот номер уже занят") 
        else:
            hw = input("Добавьте ФИО студента ")              
            di[num] = di.get(f"{num}", []) + [f"{hw}"]
            print("".join(di[num]))
            
        with open('student_base.txt','w', encoding='utf-8') as f_1:
            for k,v in di.items():
                v = ' '.join(v)           
                s = (k) + " " + (v)
                print(s)
                f_1.write(s.strip() +'\n')