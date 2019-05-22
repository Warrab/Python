EndOfList = 10
for i in range(1,EndOfList):
    print(i, ' * (', i, ' + 2) = ', i*(i+2), sep='')
	print()

for i in range(1,EndOfList):
    print('2 * ', i, '+', i, ' ^ 2 = ', i*2+i**2, sep='')
print()

for i in range(1,EndOfList):
    print('2*', i, ' + ', i, '^2 = ', 2*i+i**2, sep='')
print()

for i in range(1,EndOfList):
    print(i*2+i**2, '= ', i, '*2', '+', i, '**2', sep='')