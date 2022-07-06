import random
#1
# s1 = 5
# r1 = 5
# a = [[0] * r1 for i in range(s1)]
# print(len(a))
# for i in range(s1):
#     for j in range(r1):
#         a[i][j] = random.randint(0, 50)
#         print(a[i][j], end=' ')
#     print()
#
# l1 = []
# s = 0
# for i in range(len(a)):
#     l1.append(sum(a[i]))
#     if sum(a[i]) == max(l1):
#         s = i + 1
# print(f'Строка с максимальной суммой элементов: {s}')

#2

# while True:
#     a = input("Число №1: ")
#     b = input("Число №2: ")
#     try:
#         res = int(a)/int(b)
#     except ValueError:
#         print("Только числа")
#     except ZeroDivisionError:
#         print("Деление на 0 запрещено")
#     else:
#         print(res)
#         break