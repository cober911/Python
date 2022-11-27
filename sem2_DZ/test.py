''' Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
Позиции вводятся с клавиатуры. '''

num = int(input("Введите размер списка: "))
spisok = list(range(-num, num +1)) 
print(spisok) 
count =1
for i in range(-num, num):
    count*=i
print(count)
