""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 
Пример: - 6 -> да - 7 -> да - 1 -> нет  """


a = int(input('введите день недели от 1 до 7: '))
if a == 6 or a == 7:
    print(f' день {a}  являается выходным')
elif a>0 and a<5:
    print(f' день {a}  являается рабочим')
else:
    print('такого дня недели не существует')
