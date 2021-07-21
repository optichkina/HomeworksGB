# #task1
# class Matrix:
#     def __init__(self, list_1, list_2):
#         # self.matr = [list_1, list_2]
#         self.list_1 = list_1
#         self.list_2 = list_2
#
#     def __add__(self):
#         matr = [[0, 0, 0],
#                 [0, 0, 0],
#                 [0, 0, 0]]
#
#         for i in range(len(self.list_1)):
#
#             for j in range(len(self.list_2[i])):
#                 matr[i][j] = self.list_1[i][j] + self.list_2[i][j]
#
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))
#
#
#     def __str__(self):
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))
#
#
#
# my_matrix = Matrix([[5, 18, 11],
#                     [6, 17, 23],
#                     [41, 50, 9]],
#                    [[45, 8, 2],
#                     [6, 7, 93],
#                     [24, 5, 97]])
# # result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
#
# print(my_matrix.__add__())
#
# #task2
# class Clothes:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square_c(self):
#         return self.width / 6.5 + 0.5
#
#     def get_square_j(self):
#         return self.height * 2 + 0.3
#
#     @property
#     def get_sq_full(self):
#         return str(f'Общая площадь ткани \n'
#                    f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')
#
#
# class Coat(Clothes):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_c = round(self.width / 6.5 + 0.5)
#
#     def __str__(self):
#         return f'Площадь ткани для пальто {self.square_c}'
#
#
# class Jacket(Clothes):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_j = round(self.height * 2 + 0.3)
#
#     def __str__(self):
#         return f'Площадь ткани для костюма {self.square_j}'
#
# coat = Coat(4, 2)
# jacket = Jacket(4, 8)
# print(coat)
# print(jacket)
# print(coat.get_sq_full)
# print(jacket.get_sq_full)
# print(jacket.get_square_c())
# print(jacket.get_square_j())

#task3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
        #self.result = result

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        self.result = Cell(self.quantity + other.quantity)
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):

        if int(Cell(self.quantity - other.quantity)) > 0: #не выполняет операцию: int() argument must be a string, a bytes-like object or a number, not 'Cell'
            print(Cell(int(self.quantity - other.quantity)))
        else:
            return f'Операция вычитания невозможна'


    def __mul__(self, other):
        #self.result = Cell(int(self.quantity * other.quantity))
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        #self.result = Cell(round(self.quantity // other.quantity))
        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(33)
cells2 = Cell(9)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)
#нет разделения ячеек по рядам