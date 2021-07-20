#task1
# f = open('test.txt', 'w')
# line = input('Введите текст:\n')
# while line:
#     f.writelines(line)
#     line = input('Введите текст:\n')
#     if not line:
#         break
#
# f.close()
# f = open('test.txt', 'r')
# content = f.readlines()
# print(content)      #не переводит строки, хотя \n есть. в чем может быть проблема?
# f.close()

#task2
# file = open(r'C:\Users\optic\Desktop\GB\HomeworksGB\test_file.txt', 'r')
# content = file.read()
# print(content)
# file = open('test_file.txt', 'r')
# content = file.readlines()
# print(f'Количество строк в файле - {len(content)}')
# file = open('test_file.txt', 'r')
# content = file.readlines()
# for i in range(len(content)):
#     print(f'Количество символов в {i + 1} строке {len(content[i])}')
# file = open('test_file.txt', 'r')
# content = file.read()
# content = content.split()
# print(f'Общее количество слов - {len(content)}')
# file.close()

#task3
# file = open(r'C:\Users\optic\Desktop\GB\HomeworksGB\task3.txt', 'r')
# # for line in file:
# #     print(line)
# a = [] #более 20т
# b = [] #менее 20т
# list = file.read().split('\n')
# print(list)
# # dict = dict(file.read().split('\n'))
# # print(dict)
# # a = dict.keys()
# # print(a)                   #можно ли превратить список в словарь?у меня не получилось
#      for el in list:
#          el = el.split(' ', 1)
#          print(el)
#
#
# file.close()

#task4
# dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# file = []
# with open('task4.txt', 'r') as file_obj:
#     #content = file_obj.read().split('\n')
#     for i in file_obj:
#         i = i.split(' ', 1)
#         print(i)
#         file.append(dict[i[0]] + '  ' + i[1]) #отображается знак "'вЂ”
#     print(file)
#
# # with open('task4_new.txt', 'w') as file_obj_2:
# #     file_obj_2.writelines(file)


#task5
# def summary():
#         with open('task5.txt', 'w+') as file:
#             line = input('Введите цифры через пробел \n')
#             file.writelines(line)
#             numb = line.split()
#
#             print(sum(map(int, numb)))
#
# summary()

#task6

dict = {}
with open('task6.txt', 'r') as file:
    text=file.readlines()
    for line in file:
        line = line.split(':',3) #с шагом 3(3 параметра у предмета
#не поняла как сделать эту задачу
