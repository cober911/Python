'''  Вычислить число π c заданной точностью d
*Пример:* 
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$ '''


from math import pi

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def checkNumber(d):
    if d <= 0.1:
        a = str(d)
        a = len(a) - 2
        print(f'число Пи с заданной точностью {d} равно {round(pi, a)}')
    else:
        print("Введите число в правильном формате.")


d = InputNumbers("Введите число для заданной точности числа Пи в формате 0.0...01:\n")
checkNumber(d)