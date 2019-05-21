# from i in range(0, 10, 3)
Num = 10

L = list(range(0, Num))
L3 = L[::3]
L5 = L[::5]
L3s = sum(L3)
L5s = sum(L5)
LSum = L3s + L5s
print('L', L, sep='\t\t')
print('L3', L3, sep='\t\t')
print('L5', L5, sep='\t\t')
print('L3s', L3s, sep='\t\t')
print('L5s', L5s, sep='\t\t')
print('LSum', LSum, sep='\t')
print()

Sum = 0
# i % 3 == 0 for i in range(11):
for i in range(10):
    # if i % 3 == 0:
    #     print(i)
    # if not i == 0 and (i % 3 == 0 or i % 5 == 0):
    if (i % 3 == 0 or i % 5 == 0) and i != 0:
        print(i)
        Sum = Sum + i
print(Sum)
print('\tФормирование списка чисел кратных 3 или 5\n')
L = [i for i in range(1, Num) if i % 3 == 0 or i % 5 == 0]
Sum = sum(L)

print('L', L, sep='\t\t')
print('Sum', Sum, sep='\t')
print('\n')
print(sum(L3) / len(L3))
print(sum(L5) / len(L5))
print(sum(L) / len(L))
print('\n')
print(198 * (990 + 5) / 2)
print('\n')
