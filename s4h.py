# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в
# порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во
# элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы
# множеств. | 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12 | | --- | --- | |
#
# def fill(x):
#     if x == n:
#         order = 'первого'
#     else:
#         order = 'второго'
#     ll = []
#     i = int(1)
#     while i != x + 1:
#         ll.append(int(input(f'Введите значение для ячейки {i} {order} списка= ')))
#         i += 1
#     return ll
#
#
# n = int(input('Введите кол-во элементов первого множества: '))
# m = int(input('Введите кол-во элементов второго множества: '))
# l1 = fill(n)
# l2 = fill(m)
# result = sorted(list(set(l1) & set(l2)))
# print(result)
#
#
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти
# кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
# выросло A[i] ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно
# перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения
# максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

# def fill(x):
#     ll = []
#     i = int(1)
#     while i != x + 1:
#         ll.append(int(input(f'Введите кол-во ягод выросших на {i} кусте= ')))
#         i += 1
#     return ll
#
#
# def max_berries():
#     max_b: int = 0
#     for i in range(len(berries)):
#         if i == 1:
#             prev_b: int = berries[-1]
#             next_b: int = berries[i + 1]
#         elif i == len(berries) - 1:
#             prev_b: int = berries[i - 1]
#             next_b: int = berries[1]
#         else:
#             prev_b: int = berries[i - 1]
#             next_b: int = berries[i + 1]
#         temp_b = berries[i] + prev_b + next_b
#         if max_b <= temp_b:
#             max_b = temp_b
#     return max_b
#
#
# n = int(input('Введите кол-во кустов: '))
# berries = fill(n)
#
# print(max_berries())