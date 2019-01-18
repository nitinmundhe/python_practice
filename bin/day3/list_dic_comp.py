# List and Dict comprehensions
L1 = [a for a in range(10)]
L2 = [b * b for b in L1 if b % 2 == 0]
F1 = open(r'C:\nitsmagic\bin\day2\out1.txt')
L3 = [line.strip() for line in F1]
F2 = open(r'C:\nitsmagic\log\server_log.txt')
F2.seek(0)
IP = [line.split()[0] for line in F2 if line[:3].isdigit()]
F2.seek(0)
date = [line.split()[3].split(':')[0].strip('[') for line in F2 if line[:3].isdigit()]
F2.seek(0)
image = [line.split()[6].split('/')[-1]
         if 'pics' in line.split()[6]
         else 'Not Image'
         for line in F2
         if line[:3].isdigit()]
F2.seek(0)
website = [line.split()[10][0:line.split()[10].index('com')+3]
           for line in F2
           if line[:3].isdigit()]
F2.seek(0)
test = [ line for line in F2 if line[:3].isdigit()]

k = ['A','B']
v = [10,20]
D = { a:b for a,b in zip(k,v) }
#print(D)
T = ( i for i in range(10))
print(type(T))
print(list(T))
print(list(T))
##########################################
# print statements

print(date)
print(date)
print(image)
print(website)
print(test)