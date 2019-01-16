print('-' * 50)
F1 = open('out1.txt', 'w')
# only string can be passed to file
# we have to convert the number to string
X = 10
S = 'Python\n'
X = str(X) + '\n'
F1.write(X)
F1.write(S)
F1.flush()  # to transfer the data from buffer to file but will not close the connection
# F1.close() # transfering data from the buffer to file and also closing the file
print('-' * 50)
L = [X, S]
F1.writelines(L)
F1.flush()
F1.close()
F2 = open('out1.txt', 'r')  # read we have three methods while write has two methods
r1 = F2.read()
print(r1)
F2.seek(0)
r2 = F2.read()
print(r2)
F2.seek(0)
r3 = F2.readline()
print(r3)
print('-' * 50)
F2.seek(0)
for r in F2.readlines():
    print(r)
# print('-' * 50)
# name = input('Enter Name :')
# print('Name is =',name)
# print('-' * 50)

print('-' * 50)
F2.seek(0)
while True:
    line = F2.readline();
    if line == '':
        break
    else:
        print('line = ', line)
print('-' * 50)
F2.seek(0)
for line in F2:
    print('line in For = ', line)
print('-' * 50)
print('-' * 50)
F2.seek(0)
r4 = F2.readlines()
print('lines with readlines = ', r4)
print('-' * 50)
r5 = []
for i in r4:
    i = i.strip()
    r5.append(i)
print('r5= ', r5)
F2.close()
print('-' * 50)

print('-' * 50)
F3 = open('out1.txt', 'a')
F4 = open('out2.txt', 'a')
print(20, 'Java', sep='\n', file=F3, flush=True)
print(20, 'Java', sep='\n', file=F4, flush=True)
F3.close()
F4.close()
print('-' * 50)

# 'w' -> Write only
# 'r' -> Read Only
# 'a' -> Append Only
# 'w+' ->  wr
# 'r+' ->  rw
# 'a+' ->  ar
