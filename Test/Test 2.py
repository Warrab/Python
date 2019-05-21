i = 1
n = 1
while n < 6:
    i = (i+1)*n
    n=n+1
    print(i)

2
6
21
88
445

21/6

print(
   '''Это
многострочная
строка.
'''
)
print("O'word " 'Another "word" Last word.', 1,2)

# инициализируем список

numbers = [0] * 5
print(numbers)

# изменяем один элемент

numbers[2] = 100
print(numbers)              # [0, 0, 100, 0, 0]
some_numbers = numbers[1:3]
print(some_numbers)         # [0, 100]

# получаем размер

print(len(numbers))         # 5

# инициализируем другой список

scores = []                 # Пустой список
print(scores)

scores.append(1.1)          # Добавляем в список элемент
print(scores)               # [1.1]

scores[0] = 2.2
print(scores)               # [2.2]

        # Словари

elements = {}
elements["H"] = 1
print(elements)
print(elements["H"])        # 1

# удалить по ключу

elements["O"] = 8
elements.pop("O")

# проверка наличия ключа

if "O" in elements:
    print(elements["O"])
if "H" in elements:
    print(elements["H"])