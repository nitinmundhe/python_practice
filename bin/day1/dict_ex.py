# dict -> class
# index will not be auto generated we have to provide the index as well
L = ['python',5,'pune']
print(L[0])
# for index/key we can use any immutable objects
D = {'course':'python','dur':5,'loc':'Pune' }
print(D)
print(D['course'])
# add & update
D['course'] = ['python','java']
print('D=',D)
#print(D['abc'])
print(D.get('abc','No such Key'))
E = D.copy()
# remove
r1 = D.pop('dur')
print('D = ',D)
print('r1 = ',r1)

X = 10
S = 'py'
L = [10,20]
del X
del L[0]
del L
del D['loc']
del D
D = {'course':'python','dur':5,'loc':'Pune' }
r2 = D.popitem()
print('r2 =',r2,'D = ' ,D)
K = E.keys()
V = E.values()
i = E.items()
print('K = ',K,'V =',V,'i =',i)

