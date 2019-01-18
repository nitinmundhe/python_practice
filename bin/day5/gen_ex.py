#generators
L = [ 1,2,3,4 ]
def squares(M):
    res = []
    for i in M:
        res.append(i*i)
    return res
r1 = squares(L)
for a in r1 :
    print('a = ',a)


def gen_squares(M):
    for j in M:
        yield j*j
    for k in M:
        yield k+k

r2 = gen_squares(L)
for b in r2 :
    print('b =',b)

print('Now r2 & r2 =', r1,list(r2))
