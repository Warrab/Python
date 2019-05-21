# Input_1 = int(input('Input: ')) + 10
# print('Result:', Input_1)
# aaa = list( range( 5 ) )
# print( aaa )
# print( aaa.reverse() )
# print( aaa )
# print( aaa.count( 2 ), aaa.count( 4 ), aaa.count( 7 ), sep='', end='\n' )
# aaa.insert( 2, -1 )
# print( aaa )
# aaa.append( 333 )
# print( aaa )
# aaa.index( 333 )
# print( aaa )
# aaa.remove( 333 )
# print( aaa )
# aaa.reverse()
# print( aaa )
# aaa.sort()
# print( aaa )

File = open('New_file.txt', 'w+')
File.write('Первая запись в файл\n')
File.write('Вторая запись')
File.close()
File = open('New_file.txt', 'a')
File.write('\n12345')
File.close()
File = open('New_file.txt', 'r')
print(File.read())
File.close()


def sum(x):
    res = 0
    for i in range(x):
        res += i
    print('The sum of all numbers from 0 to', x, '= ', res)


# Ввод числа, преобразование в целое число и вызов функции sum,
# которая выводит сумму чисел от 0 до введенного значения
aaa = int(input('Enter value: '))
sum(aaa)

sum(int(input()))

print(1.01 ** 365)
input()


def num(x):
    for i in range(x):
        print(i, end='')
    # return


num(aaa)
