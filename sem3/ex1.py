# s = set() # создаем множество и картежи--------------

# lst = [22, 22, 22]
# tup_lst = tuple(lst) # создаем картеж из списка
# s.add(tup_lst)

# s.add('222') # добавляем элемент во множество
# print(hash('222')) # выводим хеш элемент
# print('222' in s) # проверяем есть ли такой элемент во множестве
# print(hash(tup_lst))
# print(tup_lst in s)

# Создаем словари ------------------
# def f():
#     print(3333)

# dct = dict()

# dct[33]= [f]
# dct[33].append('444')
# print(dct)
''' Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайныйх чисел '''
# from time import time


# def gener():
#     randomNum = int(time() * 1000 % 100)
#     return randomNum


# restart = ''
# while restart == '':
#     randomNum = gener()
#     print(randomNum)
#     restart = input('Restart ?')

'''Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
    ['22', '33', '123', 'dfs', 'trt', '55', ] 
    f(n) '''

# lst = ['22', '33', '123', 'dfs', 'trt', '55']
# u = 55
# print(lst)
# # for i in range(len(lst)):
# #     if lst[i].isdigit() and int(lst[i]) == u:
# for i in lst: #---------------
#     if i.isdigit() and int(i) == u:
#         print(f'В списке присутствует искомое значение. \n На позиции {i}')

# list_a = ['22', '33', '123', 'dfs', 'trt', '55'] # Только для цифр -----------------------
# def f(l_1, n):
#     for item in l_1:
#         if item.isdigit() and int(item) == n:
#             return True
#     return False

# print(f(list_a, 55))        

''' Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет. '''

lst = ['qwe', '33', '123', 'dsafs', 'qwe', 'trt', '55']
u = "qwe"
count = 0
print(lst)
for i in range(len(lst)):
    if lst[i] == u:
        count += 1
        if count == 2:
            break
print(f'Второе вхождение строки в список на позиции {i}.')
