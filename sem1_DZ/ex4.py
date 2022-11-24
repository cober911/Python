""" Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y). """

quarternumber = int(input('введите номер четверти: '))
if(quarternumber == 1):
    print('x > 0 and y > 0')
elif(quarternumber == 2):
    print('x < 0 and x > 0')
elif(quarternumber == 3):
    print('x < 0 and y < 0')
elif(quarternumber == 4):
    print('x > 0 and y < 0')
