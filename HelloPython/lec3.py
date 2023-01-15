# def f(x):
#     return x**2

# g = f

# # print(type(f))
# # print(type(g))

# # print(f(3))
# # print(g(3))

# def calc1(x):
#     return x+10

# print(calc1(10))

# def calc2(x):
#     return x*10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)


#                       LAMBDA 
# def sum(x, y):
#     return x+y

# sum = lambda x, y: x+y

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)

# calc(lambda x, y: x+y, 4, 5)



#                       List Comprehension

# list = []

# for i in range(1, 21):
#     if(i%2 == 0):
#         list.append(i)

# print(list)


# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i % 2==0]
# print(list)


# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


#                       MAP

# li = [x for x in range(1,20)]
# li = list(map(lambda x: x+10, li)) #увел. на +10
# print(li)

# data = list(map(int, input().split()))
# print(data)

# data = list(map(int, '1 2 3'.split())) # для работы с этими данными доб. list перед map
# for e in data:
#     print((e, e*10))

# print('---')

# for e in data:
#     print(e)



#                           FILTER

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x % 2==0, data))
# print(res)


#                           ZIP

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# # salary = [11, 22, 33]

# data = list(zip(users, ids))
# print(data)

# data = list(enumerate(users))
# print(data)