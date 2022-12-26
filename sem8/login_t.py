def enter_t():
    global personal_data_teacher
    personal_data_teacher = {"gus_1" : "1234", "newt_2": "3213", "shmid_3": "2312", "urt_4": "312"}
    
    while True:
        ent_1 = input("Введите логин: ") 
        if ent_1 in personal_data_teacher:
            #print("Логин верный")
            break
        else:
            print("Вы ввели неправильный логин. ")
        
    while True:
        ent_2 = input("Введите пароль: ")
        if ent_2 in personal_data_teacher.values():
            print("Все верно")
            break
        else:
            print("Вы ввели неправильный пароль. ") 
