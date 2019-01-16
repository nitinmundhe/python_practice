# Strings
# str -> class
a = 'Person'
b = "Person's"
c = """Person's Hight is xyx". """
d = '''Person's Hight is xyx". '''
e = '''line 2
line 2'''
# e will be with new line character
f = 'line 1 \
line 2'
# f will be with out new line character
print(a,b,c,d,e,f,sep='\n')

s1 = 'Hello'
s2 = 'Python'
r1 = s1 + s2
r2 = s1 * 5
print(s1,s2,sep='\n')
print(r1,r2,sep='\n')
line = '-' * 40
print(line)

g =  'Wel Come'
print(g)
print(len(g),' ',g[0])
#slicing
print(g[4:])
# start index is inclusive and end index is exclusive.
print(g[:6])
print(g[4:])
print(g[0:6:1])
# default value of step is 1
print(g[0:8:2])
print(g[::-1])
print(g[7:-1:-1])
# need to provide proper index otherwise empty string will be return
# for each string  two indsex will get created
#     01234567           # Positve index
#g = 'Wel Come' 
#     -8-7-6-5-4-3-2-1   # neagtive reverse index
print(g[-4:])  #Come
print(g[-4::-1])  #C leW
print(g[:-4])
r3 = g.startswith('Wel')
r4 = g.endswith('Come')
r5 = g.isupper()
r6 = g.upper()
r7 = g.islower()
r8 = g.lower()
r9 = g.count('W')
r10 = g.capitalize()
r11 = g.istitle() # firt letter of each word will be capital
r12 = g.title()
print(r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,sep='\n')

r13 = g.replace('W','w')
r14 = g[3].isspace();
r15 = g[0:3].isalpha();
r16 = '123abc'.isalnum();
print(r13,r14,r15,r16,sep='\n')
r17 = g.index('e')  # find will give index error 
r18 = g.find('e')   # find will give -1 if not found
#r17 = g.index('x')  # find will give index error 
r18 = g.find('x')   # find will give -1 if not found
r19 = g.index('e',3)
r20 = g.find('e',3)
#r21 = g.index('e',2,7)  ## need to check again
#r22 = g.find('e',2,5)   ## need to check again
#print(r17,r18,r19,r20,r21,r22)
j = ' wel come '
r23 = j.lstrip()
r24 = j.rstrip()
r25 = j.strip()
print(r23,r24,r25,sep='\n')

k = '[wel[come][]'
r26 =  k.strip('][ew')  # remoes all character from given list in the string from front and end of string
print(r26)

r27 = k.lstrip('w[')
r28 = k.rstrip('][e')
print(r27,r28,sep='\n')

x = 10
y = 20
z = x+y
r30 = 'add of x & Y is z'
r31 = 'add of {} & {} is {}'.format(x,y,z)
print(r30)
print(r31)
r32 = 'add of {1} & {2} is {0}'.format(z,x,y)
print(r32)
r33 = f'add of {x} & {y} is {z}'  # python 3.5 onwards only 
print(r33)
r34 = 'Pearson\'s'
r35 = 'c:\newfolder\test.py'
r36 = 'c:\\newfolder\\test.py'
r37 = r'c:\newfolder\test.py'
print(r34,r35,r36,r37,sep='\n')

m = 'wel   come'
r38 = m.split()
r39 = m.split('e')
r40 = ' '.join(r38)
print(r38,r39,r40,sep='\n')


