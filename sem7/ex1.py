''' Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования. '''

# def Calc(var_1, sign, var_2, ):
#     if sign == '*':
#         result = var_1 * var_2
#     elif sign == '/':
#         result = var_1 / var_2
#     elif sign == '+':
#         result = var_1 + var_2
#     elif sign == '-':
#         result = var_1 - var_2
#     return result


# operations = {'+': lambda x, y: x + y,
#               '-': lambda x, y: x - y,
#               '*': lambda x, y: x * y,
#               '/': lambda x, y: x / y}

# op = '+'
# n1, n2 = 25, 6

# print(operations[op](n1, n2))

#----------------------------

# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, 
#    добавив в неё систему логирования.

# В рамках этого обсуждения студентам надо нарисовать “архитектуру” 
#      (например, в виде блок-схемы) для работы данного приложения.
# b = complex('12+6j') * complex('5+3j')

# print(b)  # (42+66j)

# b = complex('12.5+6j') + 66

# print(b)  # (78+6j)
import Calcul


def vvod_dannih():
    var_1 = complex(input('Введите первое число: '))
    sign = input('Введите знак желаемого действия: ')
    var_2 = complex(input('Введите второе число: '))

def log_vvoda():
    data = [var_1, sign, var_2]

print(result)