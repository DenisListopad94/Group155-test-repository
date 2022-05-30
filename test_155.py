# # Функция bool()возвращает логическое значение указанного объекта.
# #
# # Объект всегда будет возвращать True, если только:
# #
# # Объект пустой, например [], (), {}
# # Объект имеет значение False
# # Объект равен 0
# # Объект равен None
# a = bool(int(input('0/1:')))
# b = bool(int(input('0/1:')))
# c = bool(int(input('0/1:')))
# print(a,b,c)
# T = a and not (b and not c)
# S = a and not b or a and c
# print(T)
# print(S)
# print(T == S)
# Height = int(input("Height: "))
# Up = int(input("Up: "))
# Down = int(input("Down: "))
# h_remain = Height - Up
# day = Up - Down
# days = (h_remain)/ day + 1
# print(days)

# n,k = map(int,input().split())
# print(n%2 == k%2)
# n = int(input())
# print(n % 1111 == 0)
# h, up, down = map(int, input().split())
# diff = h - up
# day = up - down
# days = (diff - 1) // day + 2
# print(days)
# Cтроки
# print(s[-1])
# # print(len(s)) #длинна строки
# s = "hello"
# s2 = 'world'
# s4 = ' '
# s3 = s+s4+s2
# print(s3)#конкатенация(склеивание)
# s = "wello 23"
# s2 = 'warld'
# print(s * 4)
# print(s < s2)
# slice (срез)
# s[start:stop:step]
#    012345678910
# s = 'hello world'
# print(int(s))
# numb = int(s[::-1])
# print(numb)
# print(s[::-1])#всё в обратном порядке
# print(s[-3:])
# print(s[:3]) #идём с начала
# #print(s[8:])  идём до конца
# print(s[1::2])
# print()
# s = input()
# # s[0] = '2'
# s = '2' + s[2:]
# s2 = s # так никогда не делаем
# s = s[:2]
# print(s)
# print(s2)
# s = "dsa dSDad"
# print(s.count('e',3,len(s))) # количество подстрок
# print(s.replace(' ','!')) # замена шаблона
# print(s.capitalize()) # переводит первый символ в верхний регистр остальное нижний
# print(s.title())#каждая первая буква слова большая
# print(s.find('e')) # первое появление или -1
# print(s.rfind('e'))# последнее появление или -1
# # print(s.index('e')) # тоже самое что find но с ошибкой
# # print(s.rindex('e'))
# print(s.lower())# переводит в нижний регистр
# print(s.islower()) # проверка что всё в нижнем регистре
# #s = s.upper()# переводит в верхний регистр
# print(s.isupper()) # проверка что всё в верхнем регистре
# print(s.isalpha()) # проверка что все буквы
# print(s.isdigit()) # проверка что все цифры
# print(s.isalnum())# состоит из букв или цифр
# print(s.isspace())# пробельная строка
# print(s.startswith('ds'))# начинается ли строка с шаблона
# print(s.swapcase())# меняет регистр букв
# s = s.split() # делает список строк
# print(s)
# s ="!".join(s) #объединение строки
# print(s)
# оператор включение включения in not in
# s = 'hello p'
# if 'p' not in s:
#     print("p not in s")
# форматирование(старый стиль) и f - строки(новый стиль)
# name = 'Vasya'
# age = 25
# a = b = 2
# print("name:",name,' age:',age)
# print("name: {} age: {}".format(name,age))
# print(f"name: {name.upper()} age: {age}")
# print(f"{a} + {b} = {a+b}")
# print(a,' + ',b,' = ',a+b)
# s = 'hjeddsa@poe'
# ind = s.find('@')
# print(ind)
# s2 = s[ind+1:] + s[ind] + s[:ind]
# print(s2)
# s = "100.200.2.6"
# print(s.replace('.',' '))
# s = s.split('.')
# summa = sum(map(int,s))
# summa1 = int(s[0]) +int(s[1]) + int(s[2]) +int(s[3])
# summa2 = int(s[:3])+int(s[4:7])+int(s[8])+int(s[10])
# print(summa2)
# print(summa)
# print(summa1)
# s = '12345'
# s = '2'+s[1:]
# print(s)
# name = 5
# print("my name is",name)
# x1, y1, x2, y2 = map(int, input().split())
# if (x1 - x2 == -1 and y1 - y2 == -2) or \
#         (x1 - x2 == -2 and y1 - y2 == -1) or \
#         (x1 - x2 == -2 and y1 - y2 == 1) or \
#         (x1 - x2 == -1 and y1 - y2 == 2) or \
#         (x1 - x2 == 1 and y1 - y2 == 2) or \
#         (x1 - x2 == 2 and y1 - y2 == 1) or \
#         (x1 - x2 == 2 and y1 - y2 == -1) or \
#         (x1 - x2 == 1 and y1 - y2 == -2):
#     print('Конь атакует')
# else:
#     print('Не атакует')
# Цикл For(c параметром) итерация(1 выполнение цикла)
# Цикл While(c условием)
# range - продолжение(отрезок) range(start,stop,step) stop не входит!
#                              range(stop) - start = 0
#                              range(start,stop)
# end = " " - не переходит на новую строку
# for i in range(1000,0,-1):
#     if i % 13 == 0 and i % 17 == 0:
#         print(i, end=" ")
# s = 0
# for i in range(11):
#     s += i
#     # s = s + i
# print(s)
# number  = int(input())
# count = 0
# for i in range(1,number+1):
#     if number % i ==0:
#         count+=1
# if count == 2:
#     print('Простое')
# else:
#     print('Составное')
# оператор break -  прерывает цикл досрочно
# оператор continue - пропускает все команды после себя переходя к новой итерации
# s = 0 #сумма
# for  i in range(1,6):
#     number = int(input('Enter number:'))
#     if number == 5:
#         continue
#     if number == 0:
#         break
#     print(i)
#     s += number
#    01234
# s = 'hello'
# s = input()
# # поэлементный вывод строки
# for elem in s:
#     print(elem)
# # вывод строки по индексам
# for i in range(len(s)):
#     print(i,')',s[i])
# вывести все буквы 'п' за которыми идёт буква 'а'
# i - индекс в цикле 0 1 2 3 4 len(s) - не включая
# s[i+1] - следующий элемент после s[i]
# s = input()
# for i in range(len(s)-1):
#     if s[i] == 'п' and s[i+1] == 'а':
#         print(i,s[i])
# Дана строка. Вывести все слова на новой строке
# s = "привет       я ваша       тётя"
# s += ' '
# s1 = "" # пустая строка
# # elif s1 проверка что строка не пустая
# for elem in s:
#     if elem != ' ' :
#         s1+=elem
#     elif s1:
#         print(s1)
#         s1= ""
# text = input('введите текст')
# text+=" "
# symbol = input('введите символ')
# word = 0  # количество слов
# n = ""  # строка для сборки слов
# for i in text:
#     if i!=" ":
#         n+=i
#     elif n.count(symbol)>0:
#         word+=1
#         n=""
# print(word)a
# a,b = map(int,input().split())
# for i in range(a,b+1):
#     print(i)
# for i in range(b,a+1):
#     print(i)
#
# number = 1 #начало
# s = 0
# while number <= 10: # пока True
#     print(number)
#     s = s + number
#     number += 1 # шаг
#
# print('s =',s)
# все 3-х значные числа сумма цифр  которых равна 10
# number = 100
# while number <= 999:
#     s = number // 100 + number % 10 + number // 10 % 10
#     if s == 25:
#         print(number,end=" ")
#     number += 1
# найти сумму 5 чисел введёных с клавиатуры с помощью while
# count = 1  # начало счётчика
# s = 0  # переменная для подсчёта суммы
# while count <= 5:  # проверка истинности условия
#     number = int(input("enter number:"))  # ввод числа
#     s += number  # прибавление к сумме числа number s += 1  s = s + 1
#     count += 1  # увеличение счётчика для дальнейшего завершения условия
# print(s)  # вывод суммы на экран
# # посчитать сумму чисел пока не введём число 0
# number = int(input('enter number:'))
# s = 0
# while number != 0:  # пока число не 0
#     s += number
#     number = int(input('enter number:'))
# print('s =',s)
# посчитать сумму чисел пока не введём число 0 используя бесконечный цикл
# s = 0
# while True:  # пока верно: выполняем
#     number = int(input('enter number:'))
#     if number % 5 == 0 and number != 0:  # проверка кратности 5
#         continue  # если кратно 5 не прибавляем к сумме
#     if number == 0:  # проверка для выхода из цикла
#         print('s =',s)
#         break
#     s += number

# number = int(input('enter number:'))
# s = 0
# while number != 0:  # пока число не 0
#     s += number
#     number = int(input('enter number:'))
#     if number == 5:
#         break
# else:
#     print('цикл не был прерван')
# # если цикл завершается по невыполнению условия то выводится команда else
# # ecли цикл был прерван блок else не срабатывает
# print('s =',s)
# сложить все цифры n - значного числа
# number = int(input("enter number:"))
# s = 0
# while number != 0:
#     s += number % 10 # находим последнюю цифру и прибавляем к s
#     number = number // 10 # отсекаем последнюю цифру
#     print(number)
# print(s)
# найти количество цифр 5 в n - значном числе
# number = int(input("enter number:"))
# count = 0
# while number != 0:
#     if number % 10 == 5:
#         count+=1
#     number //= 10
# print(count)
# вывести все делители числа 12: 1 2 3 4 6 12
# number = int(input("enter number:"))
# i = 1  # i - от 1 до числа number
# count = 0  # количество делителей
# while i <= number:
#     if number % i == 0:  # проверка делимости number на i
#         count += 1
#         print(i, end=' ')
#     i += 1
# print('count =', count)
# if count == 2: # проверка на простое число
#     print('число простое')
# дано 2 числа вывести их общие делители
# number1, number2 = map(int, input().split())
# i = 1
# while i <= number1 and i <= number2:
#     if number1 % i == 0 and number2 % i == 0:
#         print(i, end=' ')
#     i += 1
# найти нод чисел через алгоритм Евклида
# number1, number2 = map(int, input().split())
# while number1 != 0 and number2 != 0:
#     if number1 > number2:
#         number1 = number1 % number2  # можно отнимать
#     else:
#         number2 = number2 % number1  # можно отнимать
# nod = number1 + number2
# print('nod =',nod)

# int() -преобразует строку к целому числу
# float() - преобразует к веществ числу
# bool() - преобр к True/False
# str() - преобр к строке
# abs(x) - модуль числа |-5| = 5
# max() - находит максимум последовательности
# min() - находит минимум последовательности
# sum() - находит сумму последовател
# str - строковый объект
# print(id(m)) - адрес ячейки где
# print(type(x)) -тип переменной

# s = 'hello world hi Volodya'
# print(s.split(maxsplit=1)) #-разбитие строки по разделителю n раз
# len() - длина итерируемого(который можно перебрать циклом) объекта
# print(len([4,2,1,4]))
# a = int(input())
# print('чётное' if a%2==0 else 'нечётное')

# import random # подключение модуля
# print(random.random()) #число от 0 до 1 0.67
# print(random.randint(-100,100)) #числа от [a;b]
# print(random.choice([23,41,11,12])) # берёт случайный элемент последовательности


# #\t - табуляция(4 пробела) \n-переход на новую строку \r-перенос курсора \a - звуковой сигнал
# print('hello world')

# i = 1
# while i<=100:
#     number = random.randint(1,7)
#     print(number,end='\n')
#     i+=1

# for i in range(1,5):#внешний
#     print('i=',i)
#     for j in range(1,5):#внутренний
#         print(j,end=' ')
#     print()

# for i in range(1,7):
#     for j in range(1,4):
#         print(i,end=' ')
#     print()
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(i,end=" ")
#         break
#     print()

# проверить простое ли число
# number = int(input('enter number:'))
# count = 0 #для подсчёта количества делителей
# for i in range(2, number//2+1):#перебор всех чисел от 1 до n включительно
#     if number % i == 0:#проверка кратности
#         count += 1
#         print(i)
#         break
# if count == 0:
# вывести все простые числа от 2 100
#
# for j in range(2,100):
#     count = 0 #для подсчёта количества делителей
#     for i in range(2, j//2+1):#перебор всех чисел от 1 до n включительно
#         if j % i == 0:#проверка кратности
#             count += 1
#             break
#     if count == 0:
#         print(j,end=' ')

# вывести все простые числа от 2 100
# j = 2
# while j<=100:
#     count = 0 #для подсчёта количества делителей
#     for i in range(2, j//2+1):#перебор всех чисел от 1 до n включительно
#         if j % i == 0:#проверка кратности
#             count += 1
#             break
#     if count == 0:
#         print(j,end=' ')
#     j+=1

# s = 'hello world'
# поэлементный вывод строки
# for elem in s:
#     print(elem)
# по индексам вывод строки
# for i in range(len(s)):
#     print(s[i])
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

# коровы for
# n = int(input("Введите количество коров:"))
# for i in range(1, n + 1):
#     if i % 10 == 1 and i % 100 != 11:
#         print(f'на лугу {i} корова')
#     elif (i % 10 == 2 and i % 100 != 12) or\
#         (i % 10 == 3 and i % 100 != 13) or\
#         (i % 10 == 4 and i % 100 != 14):
#         print(f'на лугу {i} коровы')
#     else:
#         print(f'на лугу {i} коров')

# 1 1 2 3 5 8 13 21 34 55 89 ряд чисел фибоначи
# num1 = num2 = 1
# num1:1 1 2 3 5
# num2:1 2 3 5 8
# a = 3
# b = 2
# print(a,b)
# temp = b
# b = a
# a = temp
# buf temp - временная переменная
# a,b = b,a
# print(a,b)
# n = int(input('введите количество чисел:'))
# if n==1:
#     print(num1)
# elif n==2:
#     print(num1,num2)
# else:
#     print(num1, num2,end=' ')
#     for i in range(3, n + 1):
#         num2, num1 = num1 + num2, num2
#         print(num2,end=' ')
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(self.name,self.age)
#
# class Car:
#     def __init__(self, model, year_of_create):
#         self.model =model
#         self.year_of_create = year_of_create
#
#     def info(self):
#         print('model:',self.model, self.year_of_create)
#
#
# class Driver(Person,Car):
#     def __init__(self,name,age,model,year_of_create):
#         super().__init__(name,age)
#         Car.__init__(self, model, year_of_create)
#
#     def info_car(self):
#         super().info()
#     def info(self):
#         Car.info(self)
#
#
# # print(Driver.mro())
# Vasya = Driver('Vasya',22,'Lada',1980)
# Vasya.info()
# Vasya.info_car()
# class Weapon:
#     def shoot(self):
#         print('как-то используем')
#
# class Gun(Weapon):
#     def shoot(self):
#         print('bax')
#
# class Automat(Gun):
#     def shoot(self):
#         print('bax bax bax')
#
# class Bazuka(Weapon):
#     pass
#     # def shoot(self):
#     #     print("badabum")
#
# class Knife(Weapon):
#     def shoot(self):
#         print("Vjooox")
#
# class Player:
#     def shoot(self,Weapon):
#         Weapon.shoot()
#
# Tokarev = Gun()
# Ak_74 = Automat()
# bazuka = Bazuka()
# knife = Knife()
# #
# # knife.shoot()
# # Ak_74.shoot()
# # bazuka.shoot()
# # Tokarev.shoot()
#
# Vasya = Player()
# Vasya.shoot(bazuka)
# class Variable:
#     def summa(self, a, b=None):
#         if b is None:
#             print('bax')
#         else:
#             print('bax bax')
#
# Ab = Variable()
# Ab.summa(5)
# number = input('enter number:')
# mult = 1
# s = 0
# count1 = count2 = 0
# for i in range(len(number)):
#
#     if int(number[i]) % 2 == 0:
#         count1 += 1
#     else:
#         count2 += 1
#
#     s += int(number[i])
#
#     if i == 0 or i ==2 or i==5:
#         mult*=int(number[i])
#
# if count1 > count2:
#     print(s)
# else:
#     print(mult)
# Вводится строка, содержащая буквы, целые неотрицательные числа и иные символы.
# Требуется все числа, которые встречаются в строке отдельно вывести на экран. Строка
# может содержать пробелы.
# s = input()
# s += " "
# s1 = ""
# for i in s:
#     if i != " ":
#         s1 += i
#     elif s1:
#         if s1.isdigit():
#             print(s1)
#         s1=""
# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в
# веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а
# также сколько всего букв в слове, сколько гласных и согласных.
# s = input()
# pair_lower = pair_upper = 0
# for i in range(1, len(s)-1):
#     if s[i - 1].islower() and s[i].islower():
#         pair_lower += 1
#         i += 2
#     if s[i - 1].isupper() and s[i].isupper():
#         pair_upper += 1
#         i += 2
# print(pair_lower)
# print(pair_upper)
# a = [1, 2, 4, 5]
# # b = a.copy()
# b = a[:]
# a[0] = 6
# print(b)

# lst = [1, 2, 5, 1, 3]
# print(lst.count(1))
# if 1 in lst:
#     print(lst.index(1))
# else:
#     print('not in list')
#
# lst.clear()
# print(lst)

# lst.sort(reverse=True)

# print(lst[::-2])
# lst = [1, 2, 2, 5, 20, 1, 3]
# if 20 in lst:
#     ind = lst.index(20)
#     lst[ind] = 200
#
# print(lst)
# count1 = count2 = 0
# s = 0
# lst = [1, 2, 2, 6, 20, 1, 3]
# for i in range(len(lst)):
#     if lst[i] % 2 == 0:
#         count2 += 1
#         s += lst[i]
#     else:
#         count1 += 1
#
# if count2 >count1:
#     print('summa =',s)
# else:
#     print('нечетных чисел больше')

# Найти совпадающие элементы двух списков.
#
#
# Эти значения записать в новый список
# a = ['ee',5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
# c = []
# for el in a:
#     if el in b:
#         if el not in c:
#             c.append(el)
# print(c)
# Даны 2 списка:
# a = [4,6,'pу','tell',78]
# b = [44,'hello’,56,'exept’,3]
# Выполнить следующие операции:
# Сложить два списка
# Добавьте элемент 6 на 3 позицию.
# Удалите все текстовые переменные
# Посчитайте количество элементов списка
# print(isinstance([2],list))
# a = [4, 6, 'pу', 'tell', 78]
# b = [44, 'hello', 56, 'exept', 3]
# c = a + b
# c.insert(3, 6)
# i = 0
# while i < len(c):
#     if isinstance(c[i],str):
#         del c[i]
#     else:
#         i += 1
#
# print(*c)
# lst = []
# lst1 = list()
# s = 'hello world'
# lst = list(s)
# lst2 = s.split()
# print(lst)
# print(lst2)
# n = int(input('введите количество элементов списка'))
# lst = []
# for i in range(n):
#     x = int(input('введите элемент сприска'))
#     lst.append(x)
# print(lst)
# lst1 = [-5,1, 2, 3, 7, 9]
# lst2 = [0, 1, 2, 7, 9]
# m = None # пусто
# for i in lst1:
#     if i not in lst2:
#         if not m is None:# eсли m не пустота
#             if i < m:
#                 m = i
#         else:
#             m = i
# print(m)
# lst = [14, 5, 2, 188, 31, 10]
# i = 0
# while i < len(lst):
#     if lst[i] % 2 == 0:
#         s = str(lst[i])
#         s = s[::-1]
#         lst.insert(i + 1, int(s))
#         i += 1
#     i += 1
# print(lst)
# 6.	Дан список . Вычислить сколько раз в нем встречается каждый элемент, не используя сортировки
# lst = [1, 2, 2, 5, 6, 7, 6, 7, 7]
# for i in range(len(lst)):
#     if i == lst.index(lst[i]):
#         print(f"{lst[i]} - {lst.count(lst[i])}")

# 7.	Дан список . Перезаписать его так, чтобы сначала были все положительные числа,
# а затем все отрицательные и нули, сохраняя порядок их следования.
# lst = [2, 5, -5, -7, 2, 1, 8, -1]
# i = 0
# l = len(lst) # длинна фактически проверяемого списка
# while i < l:
#     if lst[i] <= 0:
#         lst.append(lst[i])
#         del lst[i]
#         i -= 1 # возврат на 1
#         l -= 1 # длинна списка который нужно проверить
#     i += 1
# print(lst)
# 9.Дан список .Перезаписать его так, чтобы чётные элементы чередовались с нечётными
# lst = [1, 5, 6, 8, 9, 10, 2, 9, 1, 1]
# for i in range(len(lst)):
#     if i % 2 == 0 and lst[i] % 2 == 1:
#         for j in range(i + 1, len(lst)):
#             if lst[j] % 2 == 0:
#                 lst[i], lst[j] = lst[j], lst[i]
#                 break
#     if i % 2 == 1 and lst[i] % 2 == 0:
#         for j in range(i + 1, len(lst)):
#             if lst[j] % 2 == 1:
#                 lst[i], lst[j] = lst[j], lst[i]
#                 break
# print(lst)
# lst = []
# s = input()
# while s!='.':
#     s = s.split(maxsplit=1)
#     if len(s) == 2:
#         lst.append(s[1])
#     elif s[0] == 'GET':
#         print(lst[-1])
#     elif s[0] == 'DELETE':
#         del lst[-1]
#     s = input()
# lst = []
# n = int(input())
# for i in range(n):
#     x = int(input())
#     lst.append(x)
# print(lst)
# list comprehension(генератор списков)
# [что хотите добавить for переменная счётчик in range(диапазон)]
# import random
#

# print([i for i in range(1, n + 1)])
# print([random.randint(1, 10) for i in range(1, n + 1)])
# print([str(random.randint(1, 10)) for i in range(1, n + 1)])
# s = 'hello'
# print([i for i in s])
# print([int(i) for i in input().split()])

# n = int(input())
# print([i for i in range(1, n + 1) if i % 2 == 0])
# print([i if i % 2 == 0 else "hello" for i in range(1, n + 1)])
# print([i**5 if i % 2 == 0 else i**0.5 for i in range(1, n + 1)])
# lst = [int(i) for i in input().split()]
# lst.sort(key=abs)
# # abs - модуль
# print(lst)
# lst = [i for i in input().split()]
# lst.sort(key = len)
# print(lst)

# lst = [int(i) for i in input().split()]
# lst.sort(key = lambda x: x%10)
# print(lst)
# task 6
# lst = [int(i) for i in input().split()]
# lst2 = []
# if len(lst) == 1:
#     lst2 = lst[:]
#     # lst2.copy(lst) 2 вариант
# else:
#     for i in range(len(lst)-1):
#         lst2.append(lst[i-1]+lst[i+1])
#     lst2.append(lst[-2]+lst[0])
# print(lst2)
# 9.	Дан список состоящий из слов. Отсортировать
# его по количеству вхождений буквы 'a'
# lst = ["aads", "adsds", "asdaa", "adsds", "asdaf"]
# # lst.sort(key=lambda x: x.count('a'), reverse=True)
# lst2 = sorted(lst,key=lambda x: x.count('a'), reverse=True)
# print(lst)
# print(lst2)
# tup = (5, 4, "привет", [3, 2, 5], (2, 5, 2))
# tup1 =(5,)
# print(tup)
# print(tup1)

# tup = (1, 4, 5, 6)
# if 4 in tup:
#     print(tup.index(4))
# else:
#     print("4 not in tup")
# tup = (1, 4, 5, 6)
# # print(len(tup))
# for el in tup:
#     print(el)
# print("чётные")
# for i in range(len(tup)):
#     if tup[i]%2==0:
#         print(tup[i])
# print("-------------------")
# for ind,el in enumerate(tup): # перебирает и индексы и элементы одновременно
#     print(ind,el)

# s = 'hello world'
# tup = tuple(s)
# print(tup)

# lst = [int(i) for i in input().split()]
# tup = tuple(lst)
# print(tup)

# info = ("Jhon", "Watson", 31)
# name, surname, age = info
# print(name)
# print(surname)
# print(age)
# 11.	 *Сгенерировать список всех простых чисел до  100 с помощью генератора.
# print([int(x) for x in range(2, 100) if x == 2 or
#        x == 3 or x == 5 or x == 7 or x > 9 and
#        x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0])
# print([int(x) for x in range(2, 10000) if all([x % y != 0 for y in range(2, x)])])
# 12.	 Дан список , преобразуйте исходный список, вставив 0 между числами.
# Дополнительный список не создавать!
# lst = [5, 2, 6, 1]
# i = 0
# while i < len(lst):
#     if i % 2 == 1:
#         lst.insert(i, 0)
#         i += 1
#     i+=1
# print(lst)
# lst = [5, 2, 6, 1]
# i = 1
# while i < len(lst):
#     lst.insert(i, 0)
#     i += 2
# print(lst)

# 13.	 Напишите программу, которая выводит часть последовательности
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).
# На вход программе передаётся неотрицательное целое число n — столько элементов
# последовательности должна отобразить программа.
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
# n = int(input("enter n:"))
# count = 0
# for i in range(1, 100):
#     for j in range(1, i + 1):
#         if count == n:
#             break
#         print(i, end=" ")
#         count += 1
# d = {1: 24, 5: 52, 25: 10}
# # keys 1 5 25
# # values 24 52 10
# d[1] = 65
# d[23] = 105
# print(d)

# d = {2: 21, 6: 24, 7: 34}
# # print(d.keys())
# # # lst = list(d.keys())
# # # print(lst)
# # print(d.values())
# # d.update({8: 14, 19: 12, 1: 16})
# # print(d.get(1))
# # print(d[1])
# # t = d.pop(2)
# # print(t)
# # del d[2]
# # print(d)
#
# # for key in d:
# #     print(key, d[key])
# # for key, value in d.items():
# #     print(key, value)
# # for el in d.items():
# #     print(el)
# # for el in d.items():
# #     print(el[0],el[1])
# key = int(input())
# if key in d:
#     print('yo')
#     del d[key]
# else:
#     print('not yo')
# print(d)
# ввод ключей и значений с клавиатуры
# d = dict()
# n = int(input())
# for i in range(n):
#     key = input()
#     value = int(input())
#     if key not in d:
#         d[key] = value
# print(d)
# d = dict(zip([1,2],['one','two','three']))
# print(d)
# d = {1: 41, 6: 12, 5: 11}
# res = 1
# for value in d.values():
#     res *= value
# print(res)
# d = {1: [41, 1, 4], 'hello': 12, 5: ("11", '12')}
# for key in d:
#     if type(d[key]) == list or type(d[key]) == tuple:
#         print(key, ':',end=" ")
#         for el in d[key]:
#             print(el, end=' ')
#         print()
#     else:
#         print(key, ':', d[key])
# d = {
#     'key1': {"key11": 1, 'key12': 2},
#     'key2': {"key21": 1, 'key22': 2},
#     'key3': {"key31": 1, 'key32': 2}
# }
# for key in d:
#     print(key,":",end=" ")
#     for key_wrapper in d[key]:
#         print(key_wrapper,d[key][key_wrapper],',',end=" ")
#     print()

# множества
# s1 = {1, 5, 2, 7, 10, 8}
# s2 = {1, 10, 7, 8}
# добавление
# s1.add(11)
# s1.update([10, 1, 5])
# удаление
# s1.pop()
# s1.discard(10)
# # s1.remove(10)

# s = "hello world"
# s2 = set(s)
# print(len(s1))
# print(s2)

# перебор
# for el in s1:
#     print(el)
#
# if 1 in s1:
#     print("yes")
# else:
#     print('no')

# проверка размера
# tup = (1,2,3,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2)
# fs = frozenset(tup)
# l = list(tup)
# s2 = set(tup)
# print(tup.__sizeof__())
# print(fs.__sizeof__())
# print(l.__sizeof__())
# print(s2.__sizeof__())

# свойства множеств
# print(s1.intersection(s2))  # пересечение &
# print(s1.union(s2))  # объединение |
# print(s1.difference(s2))  # разность s1 - s2
# print(s2.difference(s1))  # разность s2 - s1
# print(s1.symmetric_difference(s2))  # ^(s1 & s2)
# print(s1.isdisjoint(s2))  # есть ли пересечение есть - False нет - True
# print(s1.issubset(s2)) # является ли s1 подмножеством s2
# print(s1.issuperset(s2)) # входит ли полностью s2 в s1

# генераторы множеств
# a = {int(i) for i in range(10)}
# a2 = {str(i) for i in input().split()}
# print(a)
# print(a2)
# matrix
# row(строка) column(столбец)
#       0       1       2
#     0 1 2   0 1 2   0 1 2
# A = [[1, 2, 4], [5, 2, 5], [1, 5, 2]]
# print(A)
# print(A[0][0])
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         # print(f"A[{i}][{j}]={A[i][j]}", end=" ")
#         print(A[i][j], end=" ")
#     print()
# A = []
# for i in range(3):
#     lst = []
#     for j in range(3):
#         x = int(input())
#         lst.append(x)
#     A.append(lst)
# print(A)
#
# A = []
# for i in range(3):
#     A.append([int(input()) for j in range(3)])
# print(A)
# A = [[int(input()) for i in range(3)] for j in range(3)]
# print(A)
# B = [[0]*3 for i in range(3)]
# print(B)
# for i in range(len(B)):
#     for j in range(len(B[i])):
#         if i == j:
#             B[i][j] = i
#         elif i>j:
#             B[i][j] = 3
# print(B)
# A = [[i + 1 for i in range(4)] for j in range(4)]
# print(A)
# B = [[i * j for i in range(4)] if j < 2 else [i + j for i in range(4)] for j in range(4)]
# print(B)
# for i in range(len(B)):
#     s = 0
#     for j in range(len(B[i])):
#         s +=B[i][j]# сумма по строкам
#     print(s)
# b = [0, 0, 0, 0]
# for i in range(len(B)):
#     for j in range(len(B[i])):
#         b[i] += B[j][i]  # сумма по столбцам
# print(b)

# import random
#
# A = [[random.randint(-100, 100) for i in range(3)] for j in range(3)]
# min_el = max_el = A[0][0]
# imin = jmin = imax = jmax = 0
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j], end=" ")
#         if min_el > A[i][j]:
#             min_el = A[i][j]
#             imin = i
#             jmin = j
#         if max_el < A[i][j]:
#             max_el = A[i][j]
#             imax = i
#             jmax = j
#     print()
# print(max_el, min_el)
# A[imin][jmin], A[imax][jmax] = A[imax][jmax], A[imin][jmin]
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j], end=" ")
#     print()
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("zero division error")
# except TypeError:
#     print("type error :(")
# # except Exception as e:
# #     print(e)
# #     print(type(e))
# else:
#     print("all good")
# finally:
#     print("always work")
#
# print('hello')
# while True:
#     try:
#         name = input()
#         if name.capitalize() == name:
#             print("hello " + name)
#         else:
#             raise NameError("Введите имя с большой буквы")
#     except NameError:
#         print("Попробуй заново")
#     else:
#         break
# import random
#
# n = int(input())
# numb = random.randint(1, n)
# main_set = {i for i in range(1, n + 1)}
# count = 0
# print(numb)
# while True:
#     count += 1
#     print(*main_set)
#     print('Enter guess:', end=" ")
#     set1 = {int(i) for i in input().split()}
#     if numb in set1:
#         print("YES:", end=" ")
#         main_set = set1
#     else:
#         print("NO:", end=" ")
#         main_set = main_set - set1
#
#     if (len(set1) == 1 and numb in set1) or len(main_set) == 1:
#         print(f"YES {numb}' is correct You answered on the  try {count}")
#         break

# запись и дозапись в файл
# d = {
#     "Иванов Иван":[4,1,2,5,2],
#     "Петров Петр":[4,6,2,6,1],
#     "Сидоров Иван":[5,1,5,6,2]
#     }
# lst = [2, 4, 5, 1, 51, 2, 1]
# f = open("test1.txt", 'w', encoding='utf-8')
# for i in range(3):
#     s = input("enter string:")
#     f.write(s + "\n")
# f.write("hello world")
# f.write("help me \n")
# for el in lst:
#     f.write(str(el)+" ")
# for key,value in d.items():
#     f.write(key+":")
#     for el in value:
#         f.write(str(el)+" ")
#     f.write('\n')
# f.close()
# Считывание из файла данных
# try:
#     f = open('test1.txt','r',encoding='utf-8')
#     s = f.read()
#     # repr - позволяет увидеть сырую строку
#     # rstrip - убтрает \n \t \r в конце
#     s = s.replace('\n',' ').rstrip()
#     lst = s.split()
#     # s = s[:-1]
#     print(s)
#     print(lst)
#     f.close()
# except FileNotFoundError:
#     print('file not found')
# чтение данных из файла конструкция with as
# lst = []
# with open('test1.txt','r',encoding='utf-8') as f:
#     for line in f:
#         lst.extend(line.rstrip().split())
#     # s = f.readline().rstrip().split()
#     # lst.extend(s)
#     # s = f.readline().rstrip().split()
#     # lst.extend(s)
#     # s = f.readline().rstrip().split()
#     # lst.extend(s)
# print(lst)
# считать из файла и записать в словарь d
# d = {}
# with open('test1.txt','r',encoding='utf-8') as f:
#     for line in f:
#         key = line.rstrip().split(": ")[0]
#         value = line.rstrip().split(": ")[1].split(" ")
#         value = list(map(int,value))
#         d[key] = value
# print(d)
# Имеется текстовый файл.
# Переписать в другой файл все его строки
# с заменой в них символа 0 на символ 1 и наоборот.
# lst = []
# with open("test1.txt",'r',encoding='utf-8') as f:
#     for line in f:
#         lst.append(line.rstrip().split())
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j],end=" ")
#     print()
# p = []
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         p = list(lst[i][j])
#         for k in range(len(p)):
#             if p[k] =='0':
#                 p[k] = '1'
#             elif p[k] == '1':
#                 p[k] = '0'
#         lst[i][j] = "".join(p)
#         print(lst[i][j],end=" ")
#     print()
# print(lst)
# with open('test2.txt','w',encoding='utf-8') as f:
#     for el in lst:
#         s = ' '.join(el)
#         f.write(s+'\n')
# with open("C:\\Users\Denis\\test155.txt",'r',encoding='utf-8') as f:
#     s = f.read()
#     print(s)

# os modul
# import os
# os.chdir('folder')
# os.remove("test123.txt")
# os.chdir('..')
# os.rmdir("folder")
# open('test122.txt','w')
# os.replace(src='test122.txt',dst='test123.txt',src_dir_fd=None,dst_dir_fd=None)
# os.remove('test122.txt')
# print(os.listdir(path='.'))
# os.mkdir('folder')
# os.rename('test22.txt','test122.txt')
# print("current dir:",os.getcwd())
# list tuple set dict file exeptions
# in not in
# tup = (4,6,{1,2})
# print(len(tup))
# d = dict()
# d['key1'] = 'value1'
# print(d)
# r w a rb wb ab a+
# d1 = {}
# d2 = {}
# # n = int(input("how many questions you are going to answer: "))
# count = 0
# with open("test5.txt", "r", encoding="utf-8") as f:
#     for line in f:  # считывание построчно!
#         lst = line.rstrip().split(".")  # разделяем по точке
#         key = lst[0]  # вывели отдельно ключи
#         value = lst[1]  # вывели отдельно значения
#         d1[key] = value  # создаём словарь
# print(d1)
# with open("test3.txt", "r", encoding="utf-8") as p:
#     for line in p:  # считывание построчно!
#         lst2 = line.rstrip().split(".")  # разделяем по точке
#         key = lst2[0]  # вывели отдельно ключи
#         value = lst2[1]  # вывели отдельно значения
#         d2[key] = value  # создаём словарь
# print(d2)
# # так как ключи одинаковы можно перебирать один словарь
# for key, value in d1.items():
#     print(value)
#     quest = input('Ваш ответ?')
#     if quest == d2[key]:
#         count += 1
# print("Верное количество ответов", count)
# r(read) считываем w(write) запись a(append) дозапись
# rb wb ab r+ w+ a+
# f = open('test162.txt','w')
# for i in range(5):
#     s = input()
#     f.write(s + '\n')
#     if i==3:
#         break
# f.write("world end\n")
# f.close()
# # f = open('test162.txt','r')
# # s = f.read()
# # f.close()
# # s = s.rstrip().replace('\n',' ')
# # lst = s.split()
# # s = s.replace("\n",' ')
# # lst = s.split()
# # lst = s.split('\n')
# # lst = lst[:-1]
# #
# # print(lst)
# # lst = []
# # for line in f:
# #     line = line.rstrip().split()
# #     lst.extend(line)
# #     # print(line)
# # print(lst)
# # f.close()
# # d = {}
# # with open('test162.txt', 'r') as f:
# #     for line in f:
# #         lst = line.rstrip().split()
# #         key = lst[0]
# #         value = lst[1:]
# #         value = list(map(int,value))
# #         d[key] = value
# # print(d)
# with open('test162.txt', 'r') as f:
#     # line = f.readline().rstrip()
#     # print(line)
#     # line = f.readline().rstrip()
#     # print(line)
#     lst = f.readlines()
# #     print(lst)
# A = [[1 for j in range(6)] for i in range(6)]
# print([[A[i][j] for j in range(len(A[i]))] if i == 0
#        else [(lambda i=i, j=j: A[i - 1][j] + A[i][j - 1])() for j in range(len(A[i]))]
#        for i in range(len(A))])
#
# # else [ (lambda i=i,j=j:A[i - 1][j] + A[i][j - 1])() for j in range(len(A[i]))] for i in range(len(A))])
# # A[i - 1][j] + A[i][j - 1]
# A = [1, 2, 3, 4, 5]
# print([(lambda i=i: A[i - 1])() for i in range(len(A))])

