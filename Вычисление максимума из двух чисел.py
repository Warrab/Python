a = int(input("Введите первое число:\n"))
b = int(input("Введите второе число:\n"))

if a > b:
    Max = a
elif a < b:
    Max = b
else:
    Max = 'a=b'
print()
print('Максимльное значение =', Max)
