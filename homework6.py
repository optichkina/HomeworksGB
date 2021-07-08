#task1
#
# from time import sleep
#
#
# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         i = 0
#         while i < 3:
#             print(f'Светофор переключается: \n '
#                   f'{TrafficLight.__color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(7)
#             i += 1
#
#
# TrafficLight = TrafficLight()
# TrafficLight.running()
#

#task2
#
# class Road:
#     def __init__(self, _length, _width):
#         self._length = _length
#         self._width = _width
#
#
#
# class MassCount(Road):
#     def __init__(self, _length, _width, mass, thickness):
#         super().__init__(_length, _width)
#         self.mass = mass
#         self.thickness = thickness
#         # totalmass = _length * _width * mass * thickness
#         # return totalmass
#
#
# totalmass = MassCount(20, 5000, 25, 0.05)
# print(totalmass)
# # <__main__.MassCount object at 0x000002DF1DC61FA0> при запуске выдает такую строку. понимаю, что где-то ошибка.
# #можно было бы сделать задания через переменные, но это не соответствует теме занятия

#task3
# class Worker:
#
#     def __init__(self, name, surname, position, _income):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def get_total_income(self):
#         return self._income.get('wage') + self._income.get('bonus')
#
#
#
# a = Position('Ivan', 'Ivanov', 'Surgery', 3000, 1500)
# print(a.get_full_name())
# print(a.position)
# print(a.get_total_income())

#task4

# class Car:
#     # атрибуты
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     # методы
#     def go(self):
#         return f'{self.name} is started'
#
#     def stop(self):
#         return f'{self.name} is stopped'
#
#     def turn_right(self):
#         return f'{self.name} is turned right'
#
#     def turn_left(self):
#         return f'{self.name} is turned left'
#
#     def show_speed(self):
#         return f'Current speed {self.name} is {self.speed}'
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'Current speed of town car {self.name} is {self.speed}')
#
#         if self.speed > 40:
#             return f'Speed of {self.name} is higher than allow for town car'
#         else:
#             return f'Speed of {self.name} is normal for town car'
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'speed of work car {self.name} is {self.speed}')
#
#         if self.speed > 60:
#             return f'Speed of {self.name} is height'
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def police(self):
#         if self.is_police:
#             return f'{self.name} is from police department'
#         else:
#             return f'{self.name} is not from police department'
#
#
# audi = SportCar(100, 'Red', 'Opel', False)
# oka = TownCar(60, 'Black', 'Mazda', False)
# lada = WorkCar(80, 'Blue', 'Gazel', True)
# ford = PoliceCar(110, 'Blue',  'Lada', True)
# print(opel.turn_left())
# print(f'When {mazda.turn_right()}, then {opel.stop()}')
# print(f'{gazel.go()} with speed exactly {gazel.show_speed()}')
# print(f'{gazel.name} is {gazel.color}')
# print(f'Is {audi.name} a police car? {audi.is_police}')
# print(f'Is {lada.name}  a police car? {lada.is_police}')
# print(audi.show_speed())
# print(mazda.show_speed())
# print(lada.police())
# print(lada.show_speed())

#task5
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())