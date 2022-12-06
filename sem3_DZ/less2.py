''' Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] '''

lst = input("Задайте список чисел: ")
input_lst = [int(i) for i in lst.split(',')]

def proizv(lst):
    print(lst)
    sum = []
    b = len(lst)//2+1 if len(lst)%2 > 0  else len(lst)//2
    for i in range(b):
        sum.append(lst[i]*lst[-i-1])
    return sum

print(f"Произведениея чисел: {proizv(input_lst)}")

