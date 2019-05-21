from colorama import init, Fore, Back, Style
init()
# from math import floor, ceil

import math
a = 5.32
c = math.floor(a)
d = math.ceil(a)
print(c, '\tОкругление в меньшую сторону')
print(d, '\tОкругление в большую сторону')

# Дебильный калькулятор v1

#  Конкатенация строковых данных
#  т.к. вводимые значения имеют тип данных "строка"

print(Back.CYAN)
print(Fore.BLACK)
what = input("Что делаем? (+, *, -): ")
print(Back.GREEN)
a = float(input("Введи первое число: "))
print(Back.BLUE)
b = float(input("Введи второе число: "))
print(Back.LIGHTYELLOW_EX)
if what == "+":
    c = a + b
    print("Результат: " + str(c))

elif what == "-":
    c = a - b
    print("Результат: " + str(c))

elif what == "*":
    c = int(a * b)
    print("Результат: " + str(c))

else:
    print("Введена недопустимая операция!")

input()
