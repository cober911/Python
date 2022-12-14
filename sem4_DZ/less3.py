'''  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9] '''

def search_repetitions(old_list):
    _list = []
    for i in range(len(old_list)):
        if (old_list[i] not in old_list[i+1:]) and (old_list[i] not in old_list[:i]):
            _list.append(old_list[i])
    return _list


new_list = [8, 7, 6, 1, 2, 4, 1, 5, 6, 7, 9, 8, 1, 3, 4]
list = search_repetitions(new_list)
print(f'{new_list} -> {list}')