# Hash is the single line comment
# Numbers -Immutable
# String  -Immutable
'''
    Hello This is multiline comment
    List  -Mutable
    Tuple -Immutable
'''
"""
 Dictionary -Mutable
 Set        -Mutable
"""
# no primitives everything is object
# dynamically typed
a = 10 # int object
b = 12.5 # float object
c = 0x12 # hex object
d = 0b1010 # bin object
e = 0o12 # oct
print('hello')
# default end of line is \n
print('Result =',a,b,c,d,e,end=".")
# file=  and flush=
# two more argument will be discussed later
print('Test')
# default separator is space  we can change by passing vaiable sep
print('Result =',a,b,c,d,e,sep=',')
f = hex(10)
g = bin(10)
print(f,g,sep='\n')
# to print the address or we should call the reference
print(id(a),id(b),sep='\n')
print(type(a),type(b))
print(type(a).__name__)
print(type(0x12))
z=a #reference copy # reference count of object will be increment by 1
#automatic GC and manual GC  gc stands for garbage collection


