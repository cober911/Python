# print(dir(lst)) # вывод справки по lst
# lst =[]
# print(dir(lst))

# lst = []


# def add_to_lst(item):
#     if isinstance(item, int):
#         lst.append(item)


# add_to_lst(66)
# add_to_lst('ww')
# add_to_lst(65.5)
# add_to_lst(2)
# add_to_lst(None)
# print(lst)
# ------------------------------
def something_input(in_type, wellcome_text):
    input_str = input(f'{wellcome_text} : ')
    if in_type == 'int':
        result = int(input_str)
    elif in_type == 'float':
        result = float(input_str)
    else:
        result = input_str
    return result


def print_task_no(no):
    print('\n')
    print(f'task {no}')

'''1. Напишите программу, которая принимает на вход число N и выдаёт 
    последовательность из N членов.
    
    *Пример:*
    
    - Для N = 5: 1, -3, 9, -27, 81 '''

# n = int(input('Введите число: '))
# for i in range(1, n+1):
#     if i % 2:
#         print(3**(i-1), end=', ')
#     else:
#         print(-3**(i-1), end=', ')
# --------------
# N = int(input('Введите значение N:')) # работа через функцию
# def sequence(n):
#     for i in range(n):
#         print((-3) ** i, end=' ') #  сначала-3 возводим в степень ноль
# sequence(N)


'''2. Для натурального n создать список, 

   состоящий из элементов последовательности 3n + 1.
    
    *Пример:*
    
    - Для n = 4: [1, 4, 7, 10, 13]  '''
# n = int(input('Введите число: '))
# array = []
# for i in range(n + 1):
#     array.append(3*i+1)
# print(array)
#-----------------
# number = int(input("Введите число: "))
# d = {i : 3*i + 1 for i in range(1,number+1)}
# print(f"Итоговая последовательность: {d}")


''' 3. Напишите программу, в которой пользователь будет задавать две строки, 
   а программа - определять количество вхождений одной строки в другой. 

s1 = 'aa ab aba ewfwef'
s2 = 'aba'

print(s1.count(s2))
'''
# print_task_no(3)
# str1 = something_input('str', 'input number string 1')
# str2 = something_input('str', 'input number string 2')
# if len(str1) > len(str2):
#     str1, str2 = str2, str1
# length = len(str1) 
# count = 0
# for i in range(len(str2) - length):
#     tmp = []
#     for j in range(length):
#         tmp.append(str2[j + i])
#         print(tmp)
#         print(''.join(tmp))
#     if str1 == ''.join(tmp):
#         count += 1
# print(count)
#----------------------
str1 = something_input('str', 'input number string 1')
str2 = something_input('str', 'input number string 2')
count =0
for i in range(len(str1) - (len(str2) - 1)):
    if str2 == str1[i:i+len(str2)]:
        count +=1

print(f"Вторая строка входит в первую {count} раз.")