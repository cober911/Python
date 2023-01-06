def enter_st():
    global personal_data_student
    personal_data_student = {"ivan_1" : "123", "petr_2": "321", "ibra_3": "231", "dor_4": "312"}
    
    while True:
        ent_1 = input("Введите логин: ") 
        if ent_1 in personal_data_student:
            #print("Логин верный")
            break
        else:
            print("Вы ввели неправильный логин. ")
        
    while True:
        ent_2 = input("Введите пароль: ")
        if ent_2 in personal_data_student.values():
            print("Всё верно")
            break
        else:
            print("Вы ввели неправильный пароль. ") 



#enter_st()