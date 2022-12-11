''' Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
*Пример*
- при N=236     ->        [2, 2, 59] '''

def prime_factors(n):
    list = []
    for i in range(2, n+1):
        while n % i == 0:
            n = n / i
            list.append(i)
    return list


number = int(input('Введите число, составлю простые множители числа: '))
list = prime_factors(number)
print(list)
