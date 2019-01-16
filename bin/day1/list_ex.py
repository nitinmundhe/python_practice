# list -> class
# string id collection of character
# list is collection of the items
# list is mutable
L = [10,12.5,'python',['a','b']]
print(L)
print(L[2]) # all probabilites of the slicing will work here
print(len(L))
# update
print(id(L))
print(id(L[1]))
L[1] ='Java'
print(L)
print(id(L))
print(id(L[1]))
# add
L.append(200)
print(L)
L.insert(2,300)
print(L)
L1 = [10,20,30]
L2 = ['a','b']
L3 = L1+L2
print(L1,L2,L3,sep = '\n')
L1.extend(L2)
print('New L1 with L1.extends(L2) is ==>',L1)
# remove from the list
print(L)
r1 = L.pop()
print(r1,L,'pop removes the end value from the list.',sep='\n')
r2 = L.pop(2) # remove the value at the mentioned index
print(r1,L,sep='\n')
print("List before r3 = L.remove('python')",L)
r3 = L.remove('python') # removes the first occurence of the gievn item # remove function will return value as none
print("List after r3 = L.remove('python')",L)
L4 = ['z','x','y']
L5 = [20,10,30]
L4.sort()
L5.sort(reverse=True)
print(L4,L5,sep = '\n')
# default sort will work only one type of items  if we combine number with string then sort will not work
L6 = [ 10,'a','b',20]
print('L6 before reverse => ',L6)
L6.reverse()
print('L6 after reverse => ',L6)
c = L6.count('b')
i = L6.index(10)
L6.clear() # to empty the list
print("c=L6.count('b')",c,'i = L6.index(10)',i,L6,sep='\t')
x = 100
y = 100
print(id(x),id(y)) # reuse of the object specifially mutable
M = [10,['a']]
N = M
P = M.copy()  # shallow copy  New object will be crearted but referencecs within list will remian the same
print(id(M),id(N),id(P),sep='\t')  # so id of the the M and N will remain the same but id of the P will be different
print(id(M[1]),id(M[1]))  #inside references will remain the same
import copy  # deep copy not available in List but available in copy.py
Q = copy.deepcopy(P)
print(id(M),id(N),id(P),id(Q),sep='\t')  # deep copy will create new object and nee references
print(id(P[1]),id(Q[1]))  #inside references will also be new one 









