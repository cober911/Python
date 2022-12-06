''' Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] '''

number = int(input("Введите число: "))

def febonachi(n):
    mass = [0]
    j = 1
    for i in range(1,n+1):
        if i%2 == 0:
            mass.insert(0,-j)
        else:
            mass.insert(0,j)
        mass.append(j)
        j += mass[-2]
    return mass

print(febonachi(number))