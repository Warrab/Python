F1 =  open(r'p:\SkyDrive\00 Programming\Course\String.txt', 'r')

# Методы,  в данном случае .readlines(), изменяют  саму переменную,
# а потому после ее применения метод .read(), предназначенный для файлов, 
# работать не будет, т.к. в переменной F1_List уже находится список, 
# присвоенный строкой "F1_List = F1.readlines()"
# и переменной F1_String будет присвоен пустая строка
F1_List = F1.readlines()
F1_String = F1.read()
print(len(F1_List))
print(F1_List)
print()
for i in F1_List:
    print(i, end = '')
print()
print()

print([str(i) for i in F1_List])

print(F1_String)
F1.close()

# F1 =  open(r'p:\SkyDrive\00 Programming\Course\String.txt', 'r+')
# print(F1.read())
# F1.close()
