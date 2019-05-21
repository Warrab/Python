def SumList(L):
    Sum = 0
    for i in L:
        Sum += i
    return Sum


x = 5
LLL = list(range(x))

print(LLL)
print(SumList(LLL))

y = 5
LL = [i for i in range(y)]

print(SumList(LL))


def bubble_sort_string(NString):
    for N in range(len(NString) - 1, 0, -1):
        # print(N)
        for j in range(N):
            if NString[j] > NString[j + 1]:
                NString[j], NString[j + 1] = NString[j + 1], NString[j]
            # print()
    return(LLL)


def bubble_sort_3(LLL):
    N = len(LLL)  # Количество проходов цикла сортировки
    t = True
    while t == True:
        t = False
        j = 0
        while j <= N - 2:
            if LLL[j] > LLL[j + 1]:
                LLL[j], LLL[j + 1] = LLL[j + 1], LLL[j]
                t = True
            j = j + 1
    print('\tСортированный список 3\n', LLL)


LLLL = [5, 9, 1, 4, 1, 9, 1]
bubble_sort_3(LLLL)
print(LLLL)

SS = 'Hello World!?! Heh'
print(SS)
# LSS = list(SS)
# bubble_sort_3(LSS)
# SSS =

x = 2
y = 1
if SS[x] < SS[y]:
    String_1 = SS[x] + SS[y]
else:
    String_1 = SS[y] + SS[x]
print(String_1)
