#tuple -> class
# immutable
T = (10,12.5,'python',['a','b'],(10,20))
# both positve and neagtive index will be genearated
print(T)
print(T[2])
# all type of slicing will work with tuple as well
print(T[1:])
print(T[2][1])
i = T.index('python')
c = T.count(12.5)
print('index i is ',i,'count c is',c,sep=' ')
# to modify the tupple we first need to convert it into list
L = list(T)
L.append(300)
T = tuple(L)
print(L,T)
