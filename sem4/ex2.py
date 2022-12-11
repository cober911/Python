''' Задайте строку из набора чисел. Напишите программу, которая покажет больше и меньшее число.
В качестве символа-разделителя используйте пробел. '''

# str_= '43 25 56 54 121'.split()
# for index in range(len(str_)):
#     str_[index]= int(str_[index])
# print(*str_)
# print(max(str_),min(str_), sep = ' ')    

''' Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способамии: 
С помощью математических формул нахождения корней квадратного уравнения '''

# import math
 
# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
 
# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)
 
# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")

''' Задайте два числа. Напишите программу, которая найдёт НОК(наименьшее общее кратное) этих двух чисел. '''

a, b = 3, 7
maxx = max(a,b)
i = maxx
while True:
    if i % a == 0 and i % b ==0:
        print(i)
        break
    i += maxx