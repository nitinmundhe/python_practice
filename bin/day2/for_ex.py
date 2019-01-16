S = 'python'
print(S[0])
print(S[1])
for A in S:
    print('a = ', A)
B = 100
L = [10, 20, 30]
for B in L:
    print('b = ', B)
print('Now outside of A and B', A, B)

D = {'A': 10, 'B': 20}
for C in D:
    print('C = ', D[C])
for d in D.values():
    print('d = ', d)
for e in D.items():
    print('e = ', e)
    print(e[0], e[1])
for g, h in D.items():
    print('g = ', g, 'h =', h)
L1 = [10, 20, 30]
L2 = ['a', 'b']
i = zip(L1, L2)
print(list(i))
for j, k in i:
    print('j = ', j, 'k =', k)
# for(i=2,i<10,i+2)
l = range(10)
m = range(1, 10)
n = range(1, 10, 2)
print(list(l), list(m), list(n), sep='\n')
for p in range(2, 10, 2):
    print('p =', p, end=' ')
for q in range(len(L1)):
    print('{}th element of {}'.format(q, L1[q]))
comp = ['IBM', 'SYN1', 'SAP', 'SYN2']
for r in comp:
    if r.startswith('SYN'):
        print('Name starting with SYN Found. Name is ', r)
for r in comp:
    if r.startswith('SYN'):
        print('Found')
        print('Breaking and coming out of loop')
        break
    else:
        print('NF')

print('-' * 50)
for r in comp:
    if r.startswith('SYN'):
        print('Found')
        print('Breaking and coming out of loop')
        break
    else:
        print('NF')
print('-' * 50)
for c in comp:
    if not c.startswith('SYN'):
        continue
    if c.startswith('SYN'):
        print('Some Logic')
    print('Last line of For')
print('-' * 50)
print('-' * 50)
for c in comp:
    if c.startswith('SYN'):
        print('Some Logic')
    print('Last line of For')
print('-' * 50)