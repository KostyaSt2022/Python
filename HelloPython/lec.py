# Ctrl + / (comment)
# типы данных и переменная
# int, float, boolean, str, list, None

# value = None
# # print(type(value))
# a = 123
# b = 1.23
# # print (type(a))
# # print (type(b))
# value = 12334
# # print(type(value))

# s = 'it\'s string'
# print (s) # вывод строки
# print(a, '-',b, '-', s)
# print('{1} - {2} - {0} '.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', '3']
# col = ['hello', 1, 2, 4.5, True]
# print(list)
# print(col)


# Ввод и вывод данных
# print, input

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, ' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')


# Арифмет. операции
# +, -, *, /, %, //, **
# (), Сокращенные операции

# a = 1.312312
# b = 3
# c = round(a*b, 7)
# print(c)

# a = 3
# a += 5
# print(a)


# Логические операции 
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 3 < 5 < 10
# func = 1
# T = 4
# x = 123
# print(func<T>(x))

# f = 1>2 or 4<6
# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)



# Управляющие конструкции 
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


# username = input ('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)


# WHILE (переворачиваем число)
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)


# Цикл for
# r = range(1, 10, 2) #третий аргумент увел. число на 2
# for i in r:
#     print(i)



# text = 'съешь ещё этих мягких французских булок'

# help(int)
# print (len(text)) #39
# print ('ещё' in text) #True
# print (text.isdigit()) #False
# print (text.islower()) #True
# print (text.replace('ещё', 'ЕЩЁ')) #

# for c in text:
#     print(c)


# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

# arg = 2.3
# print(f(arg))
# print(type(f(arg)))