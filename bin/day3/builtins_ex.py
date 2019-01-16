# map
L = [100, 200, 300, 400]


def disc(p):
    return p - 10


r1 = map(disc, L)

r2 = map(lambda p: p - 10, L)

print(list(r1))
print(list(r1))  # empty since map will return generator
