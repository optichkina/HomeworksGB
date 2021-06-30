#task1
# from sys import argv
#
# name = argv[0]
# time = argv[1]           #IndexError: list index out of range?
# money = argv[2]
# bonus = argv[3]
# try:
#     time = float(input('time:'))
#     money = int(input('money:'))
#     bonus = int(input('bonus:'))
#     res = time * money + bonus
#     print(f'заработная плата сотрудника  {res}')
# except ValueError:
#     print('Not a number')
#

#task2
# list = [1, 8, 5, 3, 12, 6, 9, 7]
# new_list = [el for num, el in enumerate(list) if list[num - 1] < list[num]]
# print(f'Исходный список {list}')
# print(f'Новый список {new_list}')

# list=[1, 4, 6, 7, 5, 3, 8, 9]
# a = [int(i) for i in list]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])

#task3
#print(f'Числа от 20 до 240 кратные 20 и 21: {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

#task4
# list = [1, 2, 4, 7, 3, 2, 9, 1, 8, 5, 6, 3]
# new_list = [el for el in list if list.count(el) == 1]
# print(new_list)

#task4
# from functools import reduce
#
# def my_func(el_p, el):
#     return el_p * el
#
# print(f'Четные значения: {[el for el in range(99, 1001) if el % 2 == 0]}')
#Необходимо получить результат вычисления произведения всех элементов списка-т.е. первый элемент умножить на следующий и их произведение умножить на следующий элемент?

#task5
# from itertools import count
#
# for el in count(int(input('Введите стартовое число: '))):
#     print(el)
#     if el > 1000000000:
#         break

# from itertools import cycle
#
# list = [15, 'hi', 0.35, None]
# a=0
# for el in cycle(list):
#     if a>10:
#         break
#     print(el)
#     a+=1        #не очень поняла это задание, ответ взяла из методички. как работает счетчик "а=0" и "а+=1"?