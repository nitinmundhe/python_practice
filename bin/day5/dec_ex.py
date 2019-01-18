def my_dec( old_fun ):
    def new_func(x,y):
        print('Result is ')
        old_fun(x,y)
        print('End of the Result!!!')
    return new_func

@my_dec
def add(a,b):
    print(a+b)

@my_dec
def sub(a,b):
    print(a-b)

add(10,20)
sub(10,20)