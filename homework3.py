# # # task1
#  def division(ar1, ar2):
#      res = ar1 / ar2
#      print(res)
#     except ZeroDivisionError:
#         return 'Нельзя делить на 0'
#
#
# a=int(input('введите первое число:'))
# b=int(input('введите второе число:'))
# c=res
# print(c)


# task2
#def summ(ar1, ar2, ar3, ar4, ar5, ar6):
#    res = ar1 + ar2 + ar3 + ar4 + ar5 + ar6
#    print(res)
#    return res


#a = str(input('Name:'))
#b = str(input('Surname:'))
#c = str(input('Year of birth:'))
#d = str(input('City:'))
#e = str(input('email:'))
#f = str(input('telefon number:'))
#g=a+b+c+d+e+f
#print(g)


#task3
#def my_func(a,b,c):
#    if a<b<c:
#        return(b+c)
#    if b<a<c:
#        return(a+c)
#    if c<a<b:
#        return(a+b)
#print(f'summ={my_func(int(input("введите первое число:")), int(input("введите второе число:")), int(input("введите третье число")))}')

# def my_func(arg1,arg2,arg3):
#     if arg1<arg2<arg3:
#         res=arg2+arg3
#         print(res)
#         return res
#     if arg2<arg1<arg3:
#         res=arg1+arg3
#         print(res)
#         return res
#     if arg3<arg1<arg2:
#         res=arg1+arg3
#         print(res)
#         return res
# a=int(input('введите первое число:'))
# b=int(input('введите второе число:'))
# c=int(input('введите третье число:'))
#print(f'summ={my_func(int(input("введите первое число:"))), (int(input("введите второе число:"))), (int(input("введите третье число:")))}')
#почему так не получается? TypeError: my_func() missing 2 required positional arguments: 'arg2' and 'arg3'

#task4
# def my_func(x,y):
#     res=x**y
#     print(res)
#
# a=2
# b=-3
# c=my_func(a,b)
# print(c) #откуда берется None при считывании?

# def my_func(x,y):
#     if x<0:
#         print('неверное число')
#     elif y>=0:
#         print('неверное число')
#     else y<0:     #invalid syntax???
#         print(1/x**y)
# a=int(input('введите целое число'))
# b=int(input('введите целое число'))
# d=my_func(a,b)
# print(c)


#task5
# def my_func (*args):
#     return args
# list=input('введите числа через пробел или Q для выхода:').split()
# print(my_func(list))
# a=0
# for el in range(len(list)):
#     if int(list[el])>0 or int(list[el])<0:
#      print(f'summ{a+int(list[el])}')
#     if list[el]=='Q':
#         break
# print(my_func)

# def my_sum ():
#     sum_res = 0
#     ex = False
#     while ex == False:
#         number = input('Input numbers or Q for quit: ').split()
#         res = 0
#         for el in range(len(number)):
#             if number[el] == 'q' or number[el] == 'Q':
#                 ex = True
#                 break
#             else:
#                 res = res + int(number[el])
#         sum_res = sum_res + res
#         print(f'Current sum is {sum_res}')
#     print(f'Your final sum is {sum_res}')
# my_sum()



