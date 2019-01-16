# map
L = [100, 200, 300, 400]


def disc(p):
    return p - 10


r1 = map(disc, L)


# print(list(r1))
# print(list(r1))  # empty since map will return generator


# filter
def filt(p):
    return p > 100 & p < 400


r2 = filter(filt, L)
# print(list(r2))
# print(list(r2))  # empty since map will return generator

# reduce
# print(*dir(__builtins__), sep='\t')
from functools import reduce


def red(p, q):
    return p + q


r3 = reduce(red, L)
M = ['W', 'E', 'L']
r4 = reduce(red, M)
# print(r3, r4, sep='\n')

# lambda functions

r5 = map(lambda p: p - 10, L)
r6 = filter(lambda p: p > 100 and p < 400, L)
r7 = reduce(lambda p, q: p + q, L)
r8 = reduce(lambda p, q: p + q, M)
print(L, list(r5))
print(L, list(r6))
print(L, r7)
print(M, r8)

a = lambda a, b: a + b
r9 = a(10, 20)
L = [lambda a, b: a + b, lambda a, b: a - b]
r10 = L[0](50, 20)
r11 = L[1](50, 20)
print(r9, r10, r11)
