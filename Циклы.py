L10 = list(range(11))
print(L10)
L10 = [3, 5, 'a', '1', 'Help', 3, 11, '12ed', 773]
print(L10[4:-2])
print(L10[::2])
print(L10[2::3])
print(L10[3:8:])
print(L10[3:8:2])


i = 0
# while i < len(L)
    
# import Test
print('    Creating a list of even numbers')
LL = [i for i in range(21) if i % 2 == 0]
print(LL)
LL = [int(i) for i in range(0, 11, 2)]
print(LL)
LL = [i * 2 for i in range(10) if not i > 5 and i > 0]
print(LL)

print('    Formation of a list of odd numbers')
L = [i * 2 - 1 for i in range(10) if i >= 1]
print(L)
L = [i for i in range(11) if not i % 2 == 0]
print(L)

my_tuple = 'one', 'thoo'
print(my_tuple[0])
print(my_tuple)

words = 'spam', 'eggs', 'sausages'
words = 1, 2, 3, 4, 5
# words[1] = "cheese"
print(words[1:3])

for a in L:
    print(a + 100)
for i in range(2):
    print('hello!')

for i in 'hello world':
    print(i * 2, end='\n')

print('\n')

for i in range(0, 101):
    print(' ', i, '', end='', sep='')
    if i % 10 == 9:
        print()

print('\n', '\n')

print(' ', 1, 2, 3, 4, sep='00    ', end='0000\n')
print(7)
print('\n', 5, 6, 7, 8)

for i in range(1, 20):
    if i % 10 == 0:
        print(i, end="\n")
    else:
        print(i, end="\t")

for i in range(0, 20):
    print('%+3s' % i, end='', sep='')
    if i % 10 == 9:
        print()

for i in range(20):
    print(f'{i:>5}', end='') if not i % 4 == 0 else print(f'{i:>5}')

print('\n', '\n', '\n')



L = range(11)
print(L)

L = list(range(11))
print(L)
S = str(list(range(11)))
print(S)
A = str(L)