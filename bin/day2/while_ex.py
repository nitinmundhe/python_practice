# pass is just a dummy placeholder
a = 0
if a == 0:
    pass
for i in range(5):
    pass
while a < 10:
    print('a = ', a)
    # a = a + 1
    a += 1
S = 'python'
print('-' * 50)
i = 0
while i < len(S):
    print('i = ', S[i])
    i += 1
print('-' * 50)

print('-' * 50)
L = [10, 20, 30]
j = 0
while j < len(L):
    print('j = ', L[j])
    j += 1
print('-' * 50)
print('-' * 50)
while L:
    x = L.pop()
    print('X =', x)
print('-' * 50)
print('-' * 50)
L = ['l1', 'l2', 'TS', 'r1', 'l1', 'TS', 'r2', 'l1']
i = 0
while i < len(L):
    if L[i].startswith('TS'):
        i += 1
        print(L[i])
        i += 1
    else:
        i += 1
print('-' * 50)
print('-' * 50)
L = ['l1', 'l2', 'TS', 'r1', 'r2', 'TS', 'r3', 'r4', 'l1']
j = 0
while j < len(L):
    if L[j].startswith('TS'):
        for k in range(j + 1, j + 3):
            print(L[k])
        else:
            j = k + 1
    else:
        j += 1
print('-' * 50)
print('-' * 50)
k = 0
while k < len(L):
    if L[k].startswith('TS'):
        print('Found')
        break
    else:
        k += 1
else:
    print('Not Found')
print('-' * 50)

print('-' * 50)
l = 0
while l < len(L):
    if not L[l].startswith('r'):
        l += 1
        continue
    else:
        print('Line =', L[l])
        l += 1
print('End of While')
print('-' * 50)
