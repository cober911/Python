# a = int('1011', 2) # int принимает два параметра число и вторым аргументом систему счисления в кторую перевести.
# print(a)
''' map '''
# a, b, c = map(int, input().split()) 
# print(a, b, c) 
# item = list(map(int, input().split()))
# print(item)

''' filter() '''
# lst = [2, 33, 12, 34, 3, 13]

# a = filter(lambda x: x % 2 == 0 , lst) # фильтрует пропускает тольок чётные числа для списка
# a = filter(lambda x: not x % 2 , lst) # логическое представления строки сверху

# print(*a)

''' enumerate()  '''
# lst = [2, 33, 12, 34, 3, 13]
# print(list(enumerate(lst)))

#-----Пример
# lst = []
# for x in range(-2, 7):
#     if x % 2 == 0:
#         lst.append(x * x)
# print(lst)
# lst = [x * x for x in range(-2, 7) if x % 2 == 0] # пример как написать верхний пример
lst = [x * x if x % 2 == 0 else x * x * x for x in range(-2, 7)] # делаем x * x если x % 2 == 0 иначе x*x*x для x.and
print(lst)



