#task1
# class Data:
#     def __init__(self, day_month_year):
#         self.day = day
#         self.month = month
#         self.year = year
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def extract(cls, day_month_year):
#         my_date = []
#
#         for i in day_month_year.split():
#             if i != '-': my_date.append(i)
#
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#     @staticmethod
#     def valid(day, month, year):
#
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2019 >= year >= 0:
#                     return f'Данные верны'
#                 else:
#                     return f'Неправильный год'
#             else:
#                 return f'Неправильный месяц'
#         else:
#             return f'Неправильный день'
#
#     def __str__(self):
#         return f'Текущая дата {Data.extract(self.day_month_year)}'
#
#
# today = Data('20 - 7 - 2020')
# print(today)
# print(Data.valid(11, 11, 2022))
# print(today.valid(11, 13, 2011))
# print(Data.extract('11 - 11 - 2011'))
# print(today.extract('21 - 7 - 2021'))
# print(Data.valid(1, 11, 2000))


#task2
# class DivisionByNull:
#     def __init__(self, divider, denominator):
#         self.divider = divider
#         self.denominator = denominator
#
#     @staticmethod
#     def divide_by_null(divider, denominator):
#         try:
#             return (divider / denominator)
#         except:
#             return (f"Деление на ноль недопустимо")
#
#
# div = DivisionByNull(10, 100)
# print(DivisionByNull.divide_by_null(10, 0))
# print(DivisionByNull.divide_by_null(10, 2))

#task3
# class Error:
#     def __init__(self, *args):
#         self.my_list = []
#
#     def my_input(self):
#
#         # self.my_list = [int(i) for i in input('Введите значения через пробел ').split()]
#         # val = int(input('Введите значения: '))
#         # self.my_list.append(val)
#         while True:
#             try:
#                 val = int(input('Введите значения: '))
#                 self.my_list.append(val)
#                 print(f'Текущий список - {self.my_list} \n ')
#             except:
#                 print(f"Недопустимое значение - строка и булево")
#                 y_or_n = input(f'Попробовать еще раз? Yes/No ')
#
#                 if y_or_n == 'Yes' or y_or_n == 'yes':
#                     print(try_except.my_input())
#                 elif y_or_n == 'No' or y_or_n == 'no':
#                     return f'Выход'
#                 else:
#                     return f'Выход'
#
# try_except = Error(1)
# print(try_except.my_input())

#task4,5
class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель:': self.name, 'Цена 1 единицу:': self.price, 'Количество единиц:': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        # print(f'Для выхода - Q, продолжение - Enter')
        # while True:
        try:
            unit = input(f'Введите наименование: ')
            unit_p = int(input(f'Введите цену за 1 единицу: '))
            unit_q = int(input(f'Введите количество единиц: '))
            unique = {'Модель: ': unit, 'Цена за 1 единицу:': unit_p, 'Количество единиц:': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список техники:\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода нажмите Q, для продолжения нажмите Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад: \n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('Canon', 3000, 3, 12)
unit_2 = Scanner('HP', 1500, 5, 7)
unit_3 = Copier('Xerox', 1200, 2, 10)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())

