''' Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом" '''

from random import randint
n = int(2021)
player1 = 0
player2 = 0
turn = randint(1, 2) 
limit = 28

while n > 0 :
  a = 0
  
  while not (a > 0 and a <= n and a <= limit):
    a = int(input(f'игрок {turn} введите количество конфет '))
    if a > limit :
        print('можно взять не больше 28 конфет')  
    if a > n :  
        print(f'нельзя взять больше конфет,чем {n}')   
  n = n - a
  print(f'осталось {n} конфет')
  if turn == 1 :
    player1 = player1 + a
    
    turn = 2
  else :
    player2 = player2 + a
    turn = 1
if turn == 1:
    turn = 2
else:
    turn = 1     
print(f'победил игрок {turn}')