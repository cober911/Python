''' Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10 '''

number = int(input("Введите десятичное число: "))

def out(n):
    num = ''
    while n > 0:
        num = str(n % 2) + num
        n//=2
    return num

print(f"Двоичное число: {out(number)}")