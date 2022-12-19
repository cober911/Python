# Задайте строку из набора чисел. Напишите программу, 
# которая покажет больше и меньшее число.
# В качестве символа-разделителя используйте пробел.

# str_= '43 25 56 54 121'.split()
# for index in range(len(str_)):
#     str_[index]= int(str_[index])
# print(*str_)
# print(max(str_),min(str_), sep = ' ')  

str_ = '43 25 56 54 121'
print(max(list(map(int, str_.split()))), min(list(map(int, str_.split())))) # --- map ---