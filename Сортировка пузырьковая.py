# def bubble_sort(NList):
#     for N in range(len(NList) - 1, 0, -1):
#         # print(N)
#         for j in range(N):
#             if NList[j] > NList[j + 1]:
#                 NList[j], NList[j + 1] = NList[j + 1], NList[j]
#             # print()


def bubble_sort_2(NList):
    for NN in range(len(NList) - 1, 0, -1):
        print('NN =', NN, '\n')
        for j in range(NN):
            if NList[j] > NList[j + 1]:
                NList[j], NList[j + 1] = NList[j + 1], NList[j]
            print('j  =', j)
            print(NList, '\n')

    print('\tСортированный список\n', NList)

# def bubble_sort_3(LLL):
#     N = len(LLL)  # Количество проходов цикла сортировки
#     t = True
#     while t == True:
#         t = False
#         j = 0
#         while j <= N - 2:
#             if LLL[j] > LLL[j + 1]:
#                 LLL[j], LLL[j + 1] = LLL[j + 1], LLL[j]
#                 t = True
#             j = j + 1
#     print('\tСортированный список 3\n', LLL)


# LLL = [8, 3, 1, 1, 4]
# LLL = [7, 8, 3, 4]
# LLL = [1, 2, 3, 4]
LLL = [4, 3, 2, 1]

# L = list(range(len(LLL) - 1, 0, -1))
# print('\tОбратный список\n', L)
# print()

# bubble_sort(LLL)
# print(LLL)
bubble_sort_2(LLL)
# print()
# bubble_sort_3(LLL)

# print('Hello')
