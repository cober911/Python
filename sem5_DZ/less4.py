'''  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.

aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff '''

res = ""
with open('txt1.txt', 'r',encoding='utf-8') as data:
    for line in data:
        res = res + line

print(res)

# шифратор:  1-ый символ признак: 0- не повторяющаяся/1- повторяющаяся  последовательность.
# 2-ой длина для неповт. последовательности и количество символов для повторяющейся  

def shifr(txt):
    count = 1   # счетчик дублей, ограничение 9
    res = '' 
    cnt = 0     # кол-во не совпадающих, ограничение 9
    tmp = ''    # буфер для несовпадающих элементов
    for i in range(len(txt) - 1):
        if txt[i] != txt[i+1]:
            if count != 1:
                res = res + '1' + str(count) + txt[i]
                count = 1
                i += 1
            else:
                tmp += txt[i]
                cnt += 1
                if cnt == 9:
                    res = res + '0' + str(cnt) + tmp
                    cnt = 0
                    tmp = ''
                

        else:
            if cnt != 0:
                res = res + '0' + str(cnt) + tmp
                cnt = 0
                tmp = ''
            
            if count == 9:
                res = res + '1' + str(count) + txt[i]
                count = 1
            else:
                count += 1


    # обработка последнего элемента     
    if txt[-2] != txt[-1]:
        if count != 1:      #провекрка количества повторяющихся элементов
            res = res + '1' + str(count) + txt[i]
        else:
            if cnt == 0:    #проверка длины неповторяющейся последовательности
                cnt += 1
                res = res + '0' + str(cnt) + txt[-1]
            else:
                cnt += 1
                tmp += txt[-1]
                res = res + '0' + str(cnt) + tmp
    else:
        if count != 1:
            res = res + '1' + str(count) + txt[i]
    return res
# дешифруем
def deshifr(txt):
    rs = ''
    count = len(txt)
    i = 0
    while count > 0:
        pr = int(txt[i])
        number = int(txt[i+1])
        if pr == 1:
            rs = rs + txt[i + 2] * number
            count -= 3
            i += 3
        else:
            j = i
            count -= number + 2
            i += number + 2
            while number > 0:
                rs = rs + txt[j + 2]
                number -= 1
                j += 1
    return rs

result = shifr(res)
print(result)
print(deshifr(result))

with open('shifr.txt', 'w',encoding='utf-8') as file:
    for i in range(len(result)):
        file.write(result[i])
finish = deshifr(result)

with open('deshifr.txt', 'w',encoding='utf-8') as file:
    for i in range(len(finish)):
        file.write(finish[i])