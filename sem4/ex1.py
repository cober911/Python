# ДЗ------------ преобразуем в десятичное число
# n = [] # Создаем имеенно список
# number =125 # Задаем число для расчета фибоначи

# while number>0:
#     n.append(str(number % 2)) # добавляем в строковом виде остаток от деления number в переменную n
#     number //=2 # number деленое на цело равно 2
# print(''.join(n[::-1])) # Делаем срез, переворачиваем список n От начала до конца с шагом -1. Затем склеиваем его через пустую строчку ''.

# ДЗ про фибоначи -----------------------

# mem = {1:0, 2:1} # смещаеем итоговый результат именением 0 и 1 

# def fib(n):
#     if n not in mem: # говорим что если n не разу не встречается в mem то выполнить:
#         mem[n] = fib(n-1)+fib(n-2)
#     return mem[n]

# print(fib(9))
# print(mem)

# семинар --------------------------
from time import time
from second import f

# file = open('qqq.dat') # 'rt' по умолчанию чтение в текстовом виде. 'w' перезапись 'a' дозапись

# file.write(f'{time()} wwwwwwwwww\n')
# print(file.read()) # выводит всё содержимое файла. print(1, file.readline()) выводит первую строку в файле. print(file.readдштуы()) всес троки в одну
print(f())

# file.close() 


