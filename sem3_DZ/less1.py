''' Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 '''

lst = input("Задайте список: ")
input_lst = lst.replace(" ", "").split(",")

def summa(lst):
    print(lst)
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0:
          sum += int(lst[i])
    return sum

print(f'Сумма элементов: {summa(input_lst)}')
