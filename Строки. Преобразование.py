# C:\Users\Game\AppData\Local\Programs\Python\Python37\python.exe -i "$ (FULL_CURRENT_PATH)"

String_1 = "Hello 10!"
print(String_1)
print(String_1[0], '\n')

print(len(String_1), '- Длина строки "String_1"\n  - String Length "String_1"')

print('\nПоследовательная печать элементов строки "String_1":\nSequential Printing of line items "String_1":')
LIST_1 = []
i = 0
while i < len(String_1):
    print(String_1[i], end='\t')              # Последовательная печать элементов строки "String_1"
    print(String_1[i])
    LIST_1.insert(i, String_1[i])    # Последовательная сборка списка
    #print(i)
    i+=1
print('\n    Собранный список\n    Collected list')
print(LIST_1)

String_2 = ''.join(map(str,(LIST_1)))    # Преобразование списка "LIST_1" в строку
print(String_2, ' - Преобразование списка "LIST_1" в строку\n           - Convert list "LIST_1" to string')

LIST_MIXED = [10, "text", 10.5]
print('\n    Список смешанного содержания: int, string, float\n    Mixed Content List: int, string, float')
print(LIST_MIXED)

print('\n    Преобразование списка "LIST_MIXED" в строку\n    Converting the list "LIST_MIXED" to a string')
String_4 = str(LIST_MIXED)     # Преобразование списка "LIST_MIXED" в строку
print(String_4)
#String_2 = ','.join(str_3)

print('\nПреобразование списка в строку, разделитель - пробел\nConversion of the list into a string, separator - space')
String_5 = ' '.join(map(str,[10,"text",10.5]))    # Преобразование списка [10,"text",10.5] в строку
print(String_5)

y = LIST_MIXED.reverse()
print(y)