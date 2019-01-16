def add1():
    pass


add1()
add1()


def add2():
    a = 10
    b = 20
    c = a + b
    print('add = ', c)


add2()


# print('c = ',c)
def add3():
    a = 10
    b = 20
    c = a + b
    print(id(c))
    # return c
    # print('add3 = ',c) # this will never execute
    # return
    # return a,b,c
    # return [a,b,c]
    # return { 'v1':a,'v2':b,'v3':c }
    return (a + b) / (a - b)


add3()
r1 = add3()
print('r1 = ', r1, id(r1))


# positional arguments
def add4(a, b):
    return a + b


r2 = add4(10, 20)

print('r2 = ', r2)


# positional arguments with default values

def add5(a, b=-10):
    return a + b


r3 = add5(20)
r4 = add5(50, 20)
print('r3 = ', r3)
print('r4 = ', r4)


# variable arguments
def add6(a, b=10, *c):
    print('Remaining ', c)
    r = a + b
    for i in c:
        r += i
    return r


r5 = add6(10, 20, 30, 40, 50)
print('r5 = ', r5)
r6 = add6(10)
print('r6 = ', r6)

L = [10, 20, 30, 40, 50]  # packing
r7 = add6(*L)  # un-packing
print('r6 = ', r7)


def add7(*a):
    print('args passed :', a)


X = 100
S = 'py'
L = [10, 20]

add7(10, X, S, L, ('a', 'b'))


def add8(a, b=10, *c, d, e):  # d,e are keyword only arguments
    r = a + b + d + e
    for i in c:
        r += i
    return r


r8 = add8(10, 20, 30, 40, e=50, d=60)  # order doesnt matter here
print('r8 = ', r8)


def add9(a, b=10, *c, d, e, **f):
    print('Extra keyword only Args :', f)
    r = a + b + d + e
    for i in c:
        r += i
    for j in f.values():
        r += j
    return r


r9 = add9(10, 20, 30, 40, e=50, d=60, f=100, g=100)  # order doesnt matter here
print('r9 = ', r9)

r10 = add9(10, d=20, e=30)
print('r10 = ', r10)

D = {'d': 50, 'e': 60, 'f': 70, 'g': 80, 'h': 90}
r11 = add9(*L, **D)
# unpacking the positional argument
# unpacking the variable keyword only argument
print('r11 = ', r11)


# how to make variables as strictly keyword only argument
def dbconnect(*,username, password):
    print(username, password)


dbconnect(password='ABC',username='ZYZ')
