'''
Access specifics
'''
'''
1.Public Access Specfies
2.Protected Access Specifies
3.Private Access Specifies
'''



'''
1.Public Access Specifies

class Sample:
    def cycle(self):
        print('Cycle')
class Sample1:
    def cycle1(self):
        print('Cycle1')
s=Sample()
s.cycle()
s1=Sample1()
s1.cycle1()



class Sample:
    def __init__(self,name,pin):
        self.name=name
        self.pin=pin
s=Sample('dinga',1234)
print(s.name)
print(s.pin)





class Sample:
    def __init__(self,name,pin,age):
        self.name=name
        self.pin=pin
        self.age=age
s=Sample('Dinga',1234,21)
print(s.pin)
print(s.name)
print(s.age)




2.Protected Access specified(_)

class Sample:
    def __init__(self,name,age,pin):
        self.name=name
        self.age=age
        self._pin=pin
s=Sample('dinga',21,1234)
print(s.name)
print(s.age)
print(s._pin)





class Sample:
    def __init__(self,name,pin):
        self.name=name
        self._pin=pin
s=Sample('dinga',1234)
print(s.name)
print(s._pin)




3.Private Access specifier(__)

class Sample:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
s=Sample('Dinga',1234)
print(s.name)
print(s.__pin)








Encapsulation

Get and Set


class Sample:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
s=Sample('Dinga',1234)
print(s.name)
s.get_pin()




class Sample:
    def __init__(self,name,pin,):
        self.name=name
        self.__pin=pin
    def set_pin(self,new_pin):
        self._new_pin=new_pin
s=Sample('Dinga',1234)
print(s.name)
s.set_pin('1111')
print(s._new_pin)



class Sample:
    def __init__(self,name,atmpin):
        self.name=name
        self.__atmpin=atmpin
    def get_atmpin(self,password):
        if password==1234:
            print(self.__atmpin)
        else:
            print('Invalid Pin')
    def set_atmpin(self,old_pin,new_pin):
        if old_pin==self.__atmpin:
            self.new_pin=new_pin
            self.__pin=new_pin
            print('update')
d=Sample('Dinga',1234)
d.get_atmpin(int,input(':'))




class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.pin=pin
b=Bank('Dinga',1234)
print(b.name)
print(b.pin)
        


print('1.Name\n'
      '2.Contact\n'
      '3.Address\n'
      '4.Exit')
flag=True
option=int(input('Enter:'))
if option==1:
    print('1.Name\n'
          '2.Contact\n'
          '3.Exit')
    flag1=True
    option1=int(input('Enter:'))
    if option1==1:
        print('Deepan')
    elif option1==2:
        print(123)
    else:
        flag1=False
elif option==2:
    print('Contact')
elif option==3:
    print('Address')
elif option==4:
    flag=False
else:
    print('Invalid')




class Bank:
    def __init__(self,name,pin):
        self._name=name
        self._pin=pin
b=Bank('Dinga',1234)
print(b._name)
print(b._pin)







class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
b=Bank('Dinga',1234)
print(b.name)
print(b.__pin)





class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
b=Bank('Dinga',1234)
print(b.name)
b.get_pin()




1)get

class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
b=Bank('Dinga',1234)
print(b.name)
b.get_pin()





2)set




class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def set_pin(self,old_pin,new_pin):
        self.old_pin=old_pin
        self.new_pin=new_pin


# '''
# dic={'dinga':1111,'dingi':2222}
# class Bank:
#     def __init__(self,name,atmpin):
#         self.name=name
#         self.__atmpin=atmpin
#     def get_atmpin(self,password):
#          if password==dic[self.name] :
#             print(self.__atmpin)
#     # def set_atmpin(self):
# b=Bank('dinga',1234)
# dinga.get_atmpin()
'''



class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
    def set_pin(self,new_pin):
        self.__pin=new_pin
b=Bank('Dinga',1234)
print(b.name)
b.get_pin()
b.set_pin(1111)
b.get_pin()




password=1111
pin=1234
a=1
class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self,get_pin):
        if password==get_pin:
            print(self.__pin)
        else:
            print('Invalid')
    def set_pin(self,old_pin,new_pin):
        if old_pin==pin:
            self.__pin=new_pin
b=Bank('Dinga',1234)
print(b.name)
b.get_pin(int(input('Enter:')))
b.set_pin(int(input('Enter:')),int(input('Enter:')))




'''
