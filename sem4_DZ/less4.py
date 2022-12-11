''' Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
 и записать в файл многочлен степени k.
*Пример:* 
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 '''

import random


def degree_polynomial(count, rnd_min, rnd_max):
    k = count
    func = 'k = ' + str(count) + ' --> '
    k_str = ''
    while count != 0:
        rnd = (random.randint(rnd_min, rnd_max))
        k_str = str(count)
        func += str(rnd) + '*' + 'x^' + k_str + ' + '
        if count == 1:
            rnd = (random.randint(rnd_min, rnd_max))
            func += str(rnd) + ' = 0'
        count -= 1
    return func


rnd_min1 = 0
rnd_max2 = 100
count1 = int(input('Введите натуральную степень числа к= '))
formula = degree_polynomial(count1, rnd_min1, rnd_max2)
print(f'{formula}')

path = 'D:/GB/5.Python/vscode/degree_polynomial.txt'
with open(path, 'a') as data:
    data.write(formula + '\n')
    data.close()
