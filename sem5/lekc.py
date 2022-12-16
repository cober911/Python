''' ---Ламбды--- '''
# def sum(x, y):
#     return x+y

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a,b)


# calc(lambda x, y: x + y, 4, 5)

''' --- --- '''
# list = [i for i in range(1, 21) if (i % 2 == 0)]
# print(list)

# list = [(i, i) for i in range(1, 21) if i % 2 == 0] # создаем картежи если хотим вывести пары чисел
# print(list)

# def f(x):
#     return x**2

# list = [(i, f(i)) for i in range(len(list)) if i % 2 == 0] # выводим чётные числа после чего возводим их в третью степень. i в начале выводит сначала обычное число
# print(list)

'''--- ---'''
# path = 'D:/GB/5.Python/vscode/file.txt'
# f = open(path, 'r')  # связывем переменную с нашим файлом на диске
# data = f.read() + ' '  # считываем всё что есть в строчке и добавляем пробел
# f.close()

# numbers = []

# while data != '':  # делаем проверку 'Пока моя строка нее пустая'
#     space_pos = data.index(' ')  # найти позицию первого пробела
#     # взять всё что находится до позиции первого пробела, превратить это в число и добавить список чисел
#     numbers.append(int(data[:space_pos]))
#     # обновляем нашу строку с учётом того что мы добавили выше
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e** 2))
# print(out)

#------ КАК РЕШИТЬ ПО ДРУГОМУ ------


# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 4 5 8 15 23 38'.split()

# res = select(int, data)  # преобразуем строки списка data в числа int
# # пробрасываем функци where где в качестве аргумента проверяем что число четное и передаем предыдущий результат
# res = where(lambda x: not x % 2, res)
# # передаем res(результат работы на предыдущем этапе) и создаём картеж из пары(число и квадрат этого числа)
# res = select(lambda x: (x, x**2), res)
# print(res)

#----КАК РЕШИТЬ ЕЩЁ ПО ДРУГОМУ----

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)  # преобразуем строки списка data в числа int
# # пробрасываем функци where где в качестве аргумента проверяем что число четное и передаем предыдущий результат
# res = list(filter(lambda x: not x % 2, res))
# # передаем res(результат работы на предыдущем этапе) и создаём картеж из пары(число и квадрат этого числа)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

''' map() - применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор  сновым объектом, нелья пройтись дважды'''

# li = [x for x in range(1,20)]
# li = list(map(lambda x:x+10, li)) # что бы map работала нужно преобразовать набор данных в list
# print(li)

''' filter() - применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с теми объектами для которых функция вернула True '''

# data = [x for x in range(10)]

# res = list(filter(lambda x: x%2==0, data))
# print(res)

''' zip() - применяется к набору итерируемых объектов и возвращает итератор с картежами из элементов входных джанных. '''

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# solary = [111, 222, 333]
# data = list(zip(users, ids, solary))
# print(data)

''' enumerate() - применяется к итерируемому объекту и возвращает новый итератор с картежами из индекса и элементов входных данных. '''

users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(users))
print(data)
