#1 Дан произвольный список. Представьте его в обратном порядке.
# lst = [1, 5, 3, 7, 4, 5, 8]
# lst.reverse()
# print(lst)


#2 Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует,
# замените его на 200. Обновите список только при первом вхождении числа 20.
# lst = [1, 5, 20, 7, 4, 5, 8]
# a = lst.index(20)
# lst[a] = 200
# print('New list: \n', lst)


#3 Список из 7 цифр. Если четных цифр в нем больше чем нечетных, то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1 3 и 6 элемента.
# lst = [1, 4, 5, 2, 8, 7, 6]
# chet = 0
# nechet = 0
# s = 0
# b = lst[0]
# n = lst[2]
# m = lst[5]
# for i in lst:
#     if i % 2 == 0:
#         chet = chet + 1
#     else:
#         nechet = nechet + 1
# if chet > nechet:
#     for g in lst:
#         s = g + s
#     print('Сумма всех цифр в списке', s)
# else:
#     p = b * n * m
#     print('произведение 1, 3, и 6 символа списка: ', p)


#4 Найти совпадающие элементы двух списков.
# a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
# Эти значения записать в новый список

# a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)


#5 Даны 2 списка:
# a = [4,6,'pу','tell',78]
# b = [44,'hello’,56,'exept’,3]
# Выполнить следующие операции:
# 1.Сложить два списка
# 2.Добавьте элемент 6 на 3 позицию.
# 3.Удалите все текстовые переменные
# 4.Посчитайте количество элементов списка

# a = [4,6,'pу',78,'tell']
# b = [44,'hello',56,'exept',3]
# c = a + b
# print(c)
# for i in c:
#     if type(i) is str:
#         c.remove(i)
# print(c)
# s = 0
# for j in c:
#     s += j
# print('Количество элемнтов: ', s)



