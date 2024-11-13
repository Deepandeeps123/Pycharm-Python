'''
oops-object oriented programming system
'''
from symtable import Class

'''
1.class
2.object
3.inheritence
4.polymorphisum
5.abstraction
6.encapsulation
'''


'''
1.Class




                          Syntax
                    class class_name:
                           statement

class Demo:
    a=10
    b=20
d1=Demo()
print(d1)
print(d1.a)
print(d1.b)


class Demo:
    a=10
    b=20
    c=30
'''

'''
2.Object



class Demo:
    a=10
    b=20
print(a)


>>>>Error




class Demo:
    a=10
    b=20
d1=Demo
print(d1)




class Demo:
    a=10
    b=20
    c=30
d1=Demo()
print(d1.a)
print(d1.b)
print(d1.c)



class sample:
    a=10
    b=20
    c=30
o1=sample()
print(o1.a)
print(sample.a)
print(o1.b)
print(sample.b)
print(o1.c)
print(sample.c)


class Sample:
    a=10
    b=20
    c=30
o1=Sample()
o2=Sample()
print(o1.a)
print(o2.a)
print(Sample.b)
print(Sample.b)
print(o1.c)
print(Sample.c)






class Sample:
    a=10
    b=20
    c=30
    d=40
    e=50
    a=60
o1=Sample()
print(o1.a)





class Sample:
    a=10
    b=20
    c=30
o1=Sample()
o2=Sample()
o1.a=100
o2.a=200
print(o1.a)
print(o2.a)
print(o1.b)
print(o2.b)
print(o1.c)
print(o2.c)




class Sample:
    a=10
    b=20
    c=30
o1=Sample()
o2=Sample()
o1.a=50
print(o1.a)
print(o2.a)
print(Sample.a)






class Sample:
    a=10
    b=20
    c=30
o1=Sample()
o1.b=50
print(o1.a)
print(Sample.a)
print(o1.b)
print(Sample.b)
print(o1.c)
print(Sample.c)






class Sample:
    a=10
    b=20
    c=30
o1=Sample()
o2=Sample()
o2.b=100
print(Sample.b)
print(o1.b)
print(o2.b)




class Sample:
    a=10
    b=20
    c=30
o1=Sample()
o2=Sample()
o1.c=500
print(Sample.c)
print(o1.c)
print(o2.c)






class Sample:
    a=10
    b=20
    c=30
o1=Sample()
o2=Sample()
Sample.c=500
print(Sample.c)
print(o1.c)
print(o2.c)




class Sample:
    def add(a,b):
        print(b+b)
d1=Sample()
d1.add(10)




class Demo:
    def add(a,b):
        print(a)
        print(b)
d1=Demo()
d1.add(2)



class Demo:
    def add(a,b,c):
        print(b+c)
d1=Demo()
d1.add(2,3)



class Demo:
    def add(self,a,b):
        print(a+b)
d1=Demo()
d1.add(2,3)


class Sample:
    name='Dinga'
    age=21
    address='Vadapalani'
s1=Sample()
s2=Sample()
print(s1)
print(s1.name)
print(s1.age)
print(s1.address)



class Sample:
    name='Dinga'
    age=21
    address='Vadapalani'
s1=Sample()
s2=Sample()
print(s1)
print(s2)
print(s1.name)
print(s2.name)
print(s1.age)
print(s2.age)
print(s1.address)
print(s2.address)




class Sample:
    name='Dinga'
    age=21
    address='Vadapalani'
d1=Sample()
d2=Sample()
d1.name='Dingi'
print(d1.name)
print(d2.name)
print(d1.age)
print(d2.age)
print(d1.address)
print(d2.address)



class Sample:
    name='Dinga'
    age=21
    address='Vadapalani'
d1=Sample()
d2=Sample()
d1.age=22
print(d1.name)
print(d2.name)
print(d1.age)
print(d2.age)
print(d1.address)
print(d2.address)



class Sample:
    name='Dinga'
    age=21
    address='Vadapalani'
d1=Sample()
d2=Sample()
d1.address='Chennai'
print(d1.name)
print(d2.name)
print(d1.age)
print(d2.age)
print(d1.address)
print(d2.address)



class Work:
    name='Deepan'
    age=21
    address='Adari'
w1=Work()
w2=Work()
w2.name='Deeps'
print(w1.name)
print(w2.name)
print(w1.age)
print(w2.age)
print(w1.address)
print(w2.address)



class Shop:
    name='Deepan'
    age=21
    address='Adari'
s1=Shop()
s2=Shop()
s2.age=22
print(s1.name)
print(s2.name)
print(s1.age)
print(s2.age)
print(s1.address)
print(s2.address)



class Demo:
    name='Deepan'
    age=21
    address='Adari'
d1=Demo()
d2=Demo()
d2.address='Vadapalani'
print(d1.name)
print(d2.name)
print(d1.age)
print(d2.age)
print(d1.address)
print(d2.address)



class demo:
    name='Deepan'
    age=21
    address='Adari'
d1=demo()
d2=demo()
demo.name='Deeps'
print(d1.name)
print(d2.name)
print(d1.age)
print(d2.age)
print(d1.address)
print(d2.address)



class Demo:
    name='Deepan'
    age=21
    address='Vadapalani'
d1=Demo()
d2=Demo()
Demo.address='Chennai'
print(d1.name)
print(d2.name)
print(d1.age)
print(d2.age)
print(d1.address)
print(d2.address)




class Demo:
    name='Dinga'
    age=21
    address='Vadapalani'
    def inner(self,a,b):
        print(a+b)
d1=Demo()
d1.inner(10,20)




class Demo:
    def inner(self,*args,**kwargs):
        print(args)
        print(kwargs.values())
d1=Demo()
d1.inner(11,11,111,11111,a=11,b=211,c=1111,d=1111)





class Sample:
    def add(self):
        print(self)
o1=Sample()
print()





class Demo:
    name='icici'
    ifsc_code='ici1234'
    address='Vadapalani'
d1=Demo()
print(d1.name)
print(d1.ifsc_code)
print(d1.address)




class Demo:
    name='icici'
    ifsc_code='ici1234'
    address='Vadapalani'
    def inner(self,c_name,phno):
        pass
d1=Demo()
d1.inner('Dinga',1234)
print(d1.name)
print(d1.ifsc_code)
print(d1.address)
print(c_name)
print(phno)------------------------------------->  ERROR






class Demo:
    name='icici'
    ifsc_code='ici1234'
    address='Vadapalani'
    def __init__(self,c_name,phno):
        self.c_name=c_name
        self.phno=phno
d1=Demo('Dinga',1234)





class Bank:
    def __init__(self,c_name,phno):
        self.c_name=c_name
        self.phno=phno
o1=Bank('Dinga',123)
o2=Bank('Dingi',5678)
print(o1)




class Bank:
    name='icici'
    ifsc_code='ici1234'
    address='Vadapalani'
    def __init__(self,c_name,phno):
        self.c_name=c_name
        self.phno=phno
    def details(self):
        print(f'{self.name}')
        print(f'{self.ifsc_code}')
        print(f'{self.address}')
        print(f'{self.c_name}')
        print(f'{self.phno}')
o1=Bank('Dinga',1234)
o2=Bank('Dingi',1234)
o1.details()
o2.details()






class Bank:
    name='icici'
    ifsc_code='ici1234'
    address='Vadapalani'
    def __init__(self,c_name,phno):
        self.c_name=c_name
        self.phno=phno
    def details(self):
        print(f'Bank Name:{self.name}\n'
              f'Bank ifsc_code:{self.ifsc_code}\n'
              f'Bank Address:{self.address}\n'
              f'c_name:{self.c_name}\n'
              f'phno:{self.phno}\n')
b1=Bank('Dinga',1234)
b2=Bank('Dingi',5678)
b1.details()
b2.details()






class Bank:
    name='icici'
    ifsc_code='ici1234'
    address='Vadapalani'
    def __init__(self,c_name,phno,Balance):
        self.c_name=c_name
        self.phno=phno
        self.bal=Balance
    def Details(self):
        print(f'{'='*20}\n'
              f'Bank_Name:{self.name}\n'
              f'Bank_ifsc_code:{self.ifsc_code}\n'
              f'Bank_Address:{self.address}\n'
              f'c_name:{self.c_name}\n'
              f'phno:{self.phno}\n'
              f'Balance:{self.bal}')
o1=Bank('Dinga',1234,1000)
o2=Bank('Dingi',5678,2000)
o1.Details()
o2.Details()


class Bank:
    name='icici'
    ifsc_code='ici1234'
    address='Vadapalani'
    def __init__(self,c_name,phno,Balance):
        self.c_name=c_name
        self.phno=phno
        self.bal=Balance
    def details(self):
        print(f'{'='*20}\n'
              f'Bank_name:{self.name}\n'
              f'Bank_ifsc_code:{self.ifsc_code}\n'
              f'Bank_Address:{self.address}\n'
              f'c_name:{self.c_name}\n'
              f'Phone_no:{self.phno}\n'
              f'Acc_Balance:{self.bal}\n'
              f'{'='*20}')
    @classmethod
    def update(cls,name):
            cls.name=name
o1=Bank('Dinga',1234,1000)
o2=Bank('Dingi',5678,2000)
o1.details()
o2.details()
print(o1.name)
o1.update('SBI')





class Bank:
    name='icici'
    def __init__(self,c_name):
        self.c_name=c_name
    @classmethod
    def update(cls,c_name):
        cls.c_name=c_name
o1=Bank('Dinga')
o2=Bank('Dingi')
print(f'{'='*20} Before')
print(o1.name)
print(o2.name)
o1.update('SBI')
print(f'{'='*20} After')
print(o1.name)
print(o2.name)




'''