# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

num = int(input("Введите размер массива: "))
mass = []
for i in range(num):
    mass.append(random.randint(0, 10))
print(mass)
sum = 0

# for i in range(1, num, 2):
#     sum = sum + mass[i]

for i, count in enumerate(mass): # --- enumerate() ---
    if i % 2:
        sum += count 
print(f'Сумма элементов с нечётным индексом равна: ', sum)