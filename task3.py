#3. Написать программу, которая генерирует в указанных пользователем границах:
#a. случайное целое число,
#b. случайное вещественное число,
#c. случайный символ.

from random import randint, uniform


data_type = input("Введите тип данных i(integer)|f(float)|c(characters): ")
start = input("Введите начальное значение: ")
end = input("Введите конечное значение: ")

if data_type == 'i':
    r = randint(int(start), int(end))
elif data_type == 'f':
    r = uniform(float(start), float(end))
elif data_type == 'c':
    r = chr(randint(ord(start), ord(end)))
else:
    r = f"Неизвестный тип данных '{data_type}'"

print(f"Случайное значение в диапазоне от {start} до {end} = {r}")
