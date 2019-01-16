# classes
# multiple objects
# inheritance support
# operator overloading

class Account1:
    bank = 'ICICI'

    def __init__(self):
        print('SB Account Logic')

    def adduser(self, name):
        self.name = name

    def viewuser(self):
        return self.name

    def bankrules():
        return 'Bank rules';


'''
a = Account1();
b = Account1();
a.adduser('Customer A')
b.adduser('Customer B')
print(a.viewuser())
print(b.viewuser())
print(Account1.bank)
print(Account1.bankrules())
'''


class Account2(Account1):
    def addAddNumber(self, ID):
        self.UID = ID

    def viewAddhar(self):
        return 'Addhar ID is ' + str(self.UID)

    def viewuser(self):
        return 'Welcome ' + self.name

    def __init__(self):
        super().__init__()
        # Account.__init__(self)
        print('CA Logic')


'''
c = Account2();
c.adduser('Customer C')
c.addAddNumber(100)
print(c.viewuser())
print(Account2.bank)
print(c.viewAddhar())
'''


class RBI:
    def viewrules(self):
        return 'RBI rules.'


class Account3(Account2, RBI):
    def message(self):
        return 'Inside Account 3'


d = Account3();
d.adduser('Customer D')
d.addAddNumber('1234 9080 2139')
print(d.viewuser())
print('Bank Name : ', Account2.bank)
print(d.viewAddhar())
print(d.viewrules())


class Goverment:
    def viewrules(self):
        return 'Goverment Rules.'


class Account4(Account3):
    def __init__(self):
        self.g = Goverment();


e = Account4();
e.viewrules()  # RBI Rules
e.g.viewrules()  # Goverment Rules


# E here is a composite object as it has a G which is Goverment Object

class Account5:
    def __init__(self, a):
        self.name = a

    def __add__(self, other):
        return 'Welcome ' + self.name + ' and ' + other.name

f = Account5('abc');
g = Account5('zyx')
h = f + g
print(h)
