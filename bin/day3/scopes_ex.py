# Global namespace and each function will have its own namespace
x = 10  # Global Scope


def f1():
    x = 20  # Enclosed Scope

    def f2():
        # global x
        # nonlocal x
        x = 30  # Local Scope
        global y
        y = 200
        print('f2 x =', x)

    f2()
    print('f1 x =', x)


f1()
print('Global x =', x)
print('Global y =', y)

a = 100


def f3():
    global a
    a = 200


def f4():
    global a
    a = 300


f3()
a = 400
print('Value of a =', a)
f4()
print('Value of a =', a)

print('Shared variable between the function we define or make use of nonlocal')
b = 100


def f5():
    b = 10

    def f6():
        nonlocal b
        b = 20
        print('Value of b defined in f6 = ', b)

    def f7():
        print('Value of b available to f7 = ', b)

    f6()
    f7()


f5()


def exe_count():
    count = 0
    def abc():
        nonlocal count
        count += 1
        print('No of the exe = ',count)
    return abc
r = exe_count()
print(r())
y = exe_count()
print(y())
print(r())
print(y())
print(r())
print(y())
