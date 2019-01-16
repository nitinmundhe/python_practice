a = 10
if a == 10 :    
    print('a equal 10.')
if a > 10 :
    print('a greater than 10.')
if a < 10 :
    print('a less than 10.')
    
b = 10
if b == 10 :    
    print('b equal 10.')
elif b > 10 :
    print('b greater than 10.')
elif b < 10 :
    print('b less than 10.')

c = 10
if c == 10 :
    print('c equal 10.')
elif c < 10 :
    print('c less then 10.')
else :
    print('c greater than 10.')

S = 'python'
if not S.startswith('java'):
    print('Not start with Java.')
if S == 'python' :
    print('S is equal to python.')
if S != 'C':
    print('S is not equal to C.')
if 'th' in S:
    print('Substring Found.')

L1 = [10,20,30]
L2 = L1
L3 = L1.copy()

if 20 in L1:
    print('Value is found.')
if L1 is L2 :   # reference equality 
    print('Both Refers to the same object.')
if L1 == L3 :   # Object equality
    print('Contents are the same.')

D = {'A':10,'B':20}
if 'B' in D:  
    print('Key B found')
if 'B' in D.keys() :
    print('Key B found')

if ('A',10) in D.items() :  # items return a list of tuples
    print('Item is found')
    
