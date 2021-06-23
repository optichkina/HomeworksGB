#task1
#list=[1, 1.5, 'hello', 2, 2.5, 'qaz']
#print(list)
#print(type(list[0])) #тип 0 элемента
#print(list[1]) #вывести первый элемент (отсчет с 0)
#print(type(list[2])) #тип 2 элемента
#print(len(list[0:6])) # вывести количество элементов в списке
#print(type(list[4]))
#for el in list:
#    print(f"{el} имеет тип: {type(el)}") #f-строки



#task2
#l1=input("введите данные через пробел:").split()
#print(type(l1))
#print(l1[0:-1])
#print(len(l1))
#for el in range(0,len(l1),2):
#    l1[el-1],l1[el]=l1[el],l1[el-1]
#print(l1)
#я не поняла эту задачу

#task3
#list= ['winter', [12,1,2]], ['spring',[3,4,5]], ['summer', [6,7,8]], ['fall',[9,10,11]]
#di={'winter':[1,12,2], 'spring':[3,4,5], 'summer':[6,7,8], 'fall':[9.10,11]}
#a=input('введите номер месяца:')
#if a==12 or a==1 or a==2:
#    print(di.setdefault(key(1))
#elif a==3 or a==4 or a==5:
#    print(di.setdefault(key(2))
#elif a==6 or a==7 or a==8:
#    print(di.setdefault(key(3))
#elif a==9 or a==10 or a==11:
#    print(di.setdefault(key(4))
#else:
#    print('неверный номер')

#task4
#a=(input('введите данные:'))
#print(a.title())
#print(a.split())
#word=a.split()
#for i,word in enumerate(a,1):
#    print(i,word[:10]) #разделяет по буквам.не могу понять ошибку

#test_str = input("введите строку: ")
#word = []
#num = 1
#for el in range(test_str.count(' ') + 1):
#    word = test_str.split()
#    if len(str(word)) <= 10:
#        print(f" {num} {word [el]}")
#        num += 1
#    else:
#        print(f" {num} {word [el] [0:10]}")
#        num += 1

#task5
list=[1,5,3,2,4,8,7]
a=int(input('введите число:'))
for el in range(len(list)):
    if list[el]==a:
        list.insert(el+1,a)
    elif list[-1]<a:
        list.append(a)
print(list)




