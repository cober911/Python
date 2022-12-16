'''
Используем map
1. В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, что бы выполнить условие A[i] - 1 = A[i - 1]. Найдите это число.
5 6 7 8 9 10 12 13
'''
# past_el = None
# with open('text.txt') as f:
#     for item in map(int, f.read().split()):
#         if past_el is None:
#             past_el = item
#         else:
#             if item != past_el + 1:
#                 print(past_el + 1)
#             past_el = item

# --- Используем enumerate() ---
# with open("text.txt", "r") as f:
#     lst = list(map(int, f.read().split()))
# res = 0
# for x, item in enumerate(lst):
#     if x + 1 < len(lst) and item + 1 !=lst[x + 1]:
#         res = item + 1
# print(res)

'''
Используем filter
2. Напишите программу удалющую из текста все слова, содержащие "абв"
'''
# a = "привет абв пока абвг"
# res = " ".join(list(filter(lambda x: not 'абв' in x, a.split())))
# print(res)
# print(" ".join(list(filter(lambda x : not 'абв' in x, "привет абв пока абвг".split()))))
'''
3. Дан список чисел. Создайте список, в который попадают числа, описываеющие возрастрную последовательность.
Порядок элементов менять нельзя. [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д
'''

lst = [1, 5, 2, 9, 3, 4, 6, 1, 7]
res = []
i = 0
k = 0
for j, item in enumerate(lst):
    res.append([item])
    print(res)
    for i in range(j, len(lst)):
        if lst[i] > res[j][k]:
            res[j].append(lst[i])
            k += 1
    k = 0
print(res)

