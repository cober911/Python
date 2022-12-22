''' 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
*Пример:* 
 2+2 => 4; 
 1+2*3 => 7; 
 1-2*3 => -5; '''
 
def parse(s):
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        else:
            result.append(float(digit))
            digit = ""
            result.append(symbol)
    else:
        if digit:
            result.append(float(digit))
    return result

def calculate(lst):
    result = 0.0
    while '*' in lst:
        index = lst.index('*') #3
        result = lst[index - 1] * lst[index + 1] #30
        #[12, '+', 3, '*', 10, '+', 2.0]
        #[12, '+', 30, '+', 2.0]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result

s = "12+3*10+2/2"
result = parse(s)

print(result)
print(calculate(result))



print(f'Результат выражения {s}={result}')


