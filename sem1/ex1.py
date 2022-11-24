# Ввести два числа и проверить является ли одно число квадратом второго.-------------
# num1 = int(input("Введите первое число "))
# num2 = int(input("Введите второе число "))
# if num1**2 == num2 or num2**2 == num1:
#     print("Является квадратом")
# else:
#     print("Не является квадратом")

#  Напишите программу которая на вход принимает 5 чисел и находит максимальное из них.---------------
# num1 = int(input("Введите первое число "))
# num2 = int(input("Введите второе число "))
# num3 = int(input("Введите третье число "))
# num4 = int(input("Введите четвертое число "))
# num5 = int(input("Введите пятое число "))
# print(max(num1, num2, num3, num4, num5))

# count = 1
# list_numbers = []
# for i in range(1, 6):
#     number = int(input(f'Введите число{i}: '))
#     list_numbers.append(number)
# print(max(list_numbers))

# max_number = float('-inf')
# for i in range(1,6):
#     number = int(input(f'Введите число {i}: '))
#     if number>max_number:
#         max_number = number
# print(max_number)

# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N-------------------------
# num = int(input("Введите число N "))
# for i  in range(-num, num +1):
#     print(i, end= ", ") # end для вывода в строку с разделителем sep-разделяет элементы внутри функции print

# num = int(input())
# print([i for i in range(-num, num +1)]) # генерирует список

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.--------------

numb = float(input("Введите дробь "))
num_new = numb * 10 % 10
if num_new / 10 !=0:
    print(int(num_new))
else:
    print("нет")    


