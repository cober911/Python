'''
 Создайте программу для игры в "Крестики-нолики".

Вариант интерфейса:

 1  |  2 | 3
--------------
 4  |  5 | 6
--------------
 7  |  8 | 9 
'''

from random import randint

list = ['__','__','__',
        '__','__','__',
        '__','__','__']
n = 0
#playerX = 0
#playerO = 0
turn = randint(1, 2) 
while n < 9:
     n +=1 

     if turn == 1:
        i = int(-1)
        turn =2
        while not(i >= 0 and list[i] =='__'):
            i = int(input(f'игрок 1 введите позицию X = > '))
            if i < 0 or  i > 8 :
                print ('выход за диапазон')
                i = -1
            if list [i] !='__' :
                print ('эта клетка уже занята')  
        list[i] = 'X'       
            #for i in range (0, len(list), 3):
             
            #print (list[i], list[i+1], list[i+2])
     else:  
         
            i = -1
            turn = 1
            while not(i >= 0 and list[i] =='__'):
               i = int(input(f'игрок 2 введите позицию 0 = > '))
               if i < 0 or  i > 8 :
                   print ('выход за диапазон')
                   i = -1
               elif list [i] !='__' :
                   print ('эта клетка уже занята')
                   
            list[i] = '0'  
     for i in range (0, len(list), 3):   
         print (list[i], list[i+1], list[i+2])