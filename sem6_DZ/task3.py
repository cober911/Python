# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# input = [1.1, 1.2, 3.1, 5, 10.01]

# def Min_Max(mass):
#     print(mass)
#     res = [mass[0] % 1,mass[0] % 1,0] # темп
#     for i in range(len(mass)):
#         res[2] = round(mass[i] % 1, 2)
#         if res[2] < res[0] and res[2] != 0:
#             res[0] = res[2]
#         elif res[2] > res[1]:
#             res[1] = res[2]
#     return round(res[1]-res[0],2)

# print(f"Разница между мин и макс значениями дробной части: {Min_Max(input)}")

input = [1.1, 1.2, 3.1, 5, 10.01]
b = [round(input[i] - int(input[i]) , 3)  for i in range(len(input)) if input[i] - int(input[i]) !=0]
max_ = max(b)
min_ = min(b)
print (f"Разница между мин и макс значениями дробной части: {max_ - min_}")