'''
1...Property Function


class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
    def set_pin(self,new_pin):
        self.__pin=new_pin
b=Bank('Dinga',1234)
b.get_pin()
b.set_pin(1111)
b.get_pin()
b.set_pin(2222)
b.get_pin()






class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
    def set_pin(self,new_pin):
        self.__pin=new_pin
b=Bank('dinga',1234)
print(b.name)
b.get_pin()
b.set_pin(1111)
print('Sucesss')
b.get_pin()








2....Property Function


class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
    def set_pin(self,new_pin):
        self.__pin=new_pin
    a=property(get_pin,set_pin)
b=Bank('Dinga',1234)
print(b.name)
b.a
b.a=1111
b.a
b.a=2222
b.a








class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
    def set_pin(self,new_pin):
        self.__pin=new_pin
    a=property(get_pin,set_pin)
b=Bank('Dinga',1234)
print(b.name)
b.a
b.a=8888
b.a
b.a=77777
b.a







class Bank:
    def __init__(self,name,age,pin):
        self.__name=name
        self.__age=age
        self.__pin=pin
    def get_pin(self):
        print(self.__name)
        print(self.__age)
        print(self.__pin)
    def set_pin(self,new_name,new_age,new_pin):
        self.__name=new_name
        self.__age=new_age
        self.__pin=new_pin
b=Bank('Dinga',21,1234)
b.get_pin()
b.set_pin('dingi',21,1111)
b.get_pin()








pw=0000
class Bank:
   def __init__(self,name,age,pin):
       self.__name=name
       self.__age=age
       self.__pin=pin
   def get_pin(self,password):
        if pw==password:
            print(self.__name)
            print(self.__age)
            print(self.__pin)
        else:
            print('Invalid')
   def set_pin(self,password,new_name,new_age,new_pin):
       if pw==password:
            self.__name=new_name
            self.__age=new_age
            self.__pin=new_pin
       else:
           print('Invalid')
b=Bank('Dinga',21,12345)
b.get_pin(int(input('Enter the pw:')))
b.set_pin(int(input('Enter the pw:')),input('Enter the new_name'),int(input('Enter the new_age')),int(input('Enter the new_pin')))
b.get_pin(int(input('Enter the Pw')))





3.Property Decoder



class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
    def set_pin(self,new_name,new_pin):
        self.name=new_name
        self.__pin=new_pin
    a=property(get_pin,set_pin)
b=Bank('Dinga',1234)
print(b.name)
b.a
b.a=(input('Enter the Name:')),(int(input('Enter the pin:')))
b.a








class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    @property
    def a(self):
        print(self.__pin)
    @a.setter
    def a(self,new_pin):
        self.__pin=new_pin
b=Bank('Dinga',1234)
print(b.name)
b.a
b.a=1111
b.a





class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    @property
    def a(self):
        print(self.__pin)
    @a.setter
    def a(self,new_pin):
        self.__pin=new_pin
b=Bank('Dinga',1234)
print(b.name)
b.a
b.a=1110
b.a








class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    @property
    def a(self):
        print(self.__pin)
    @a.setter
    def a(self,new_pin):
        self.__pin=new_pin
    @a.deleter
    def a(self):
        del self.__pin
b=Bank('Dinga',1234)
print(b.name)
b.a
b.a=292020202
b.a
del b.a
b.a





pw=1111
class Bank:
    def __init__(self,name,age,pin):
        self.name=name
        self.age=age
        self.__pin=pin
    @property
    def a(self):
            print(self.name)
            print(self.age)
            print(self.__pin)
    @a.setter
    def a(self,new_pin):
            self.__pin=new_pin
b=Bank('Dinga',21,1234)
b.a=1111
b.a=9999
b.a






class Bank:
    def __init__(self,name,age,pin):
        self.name=name
        self.__age=age
        self.__pin=pin
    def get_b(self):
        print(self.name)
        print(self.__age)
        print(self.__pin)
    def set_c(self,new_age,new_pin):
        self.__age=new_age
        self.__pin=new_pin
    def del_d(self):
        del self.__pin
    a=property(get_b,set_c,del_d)
b=Bank('Dinga',21,1234)
b.a
b.a=(int(input('Enter:')),int(input('Enter:')))
b.a






class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
    def set_pin(self,new_pin):
        self.__pin=new_pin
    def del_pin(self):
        del self.__pin
b=Bank('Dinga',1234)
print(b.name)
b.get_pin()
b.set_pin(1111)
b.get_pin()
b.del_pin()
b.get_pin()






class Bank:
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
    def set_pin(self,new_pin):
        self.__pin=new_pin
    def a(self):
        del self.__pin
    a=property(get_pin,set_pin,a)
b=Bank('dinga',1234)
print(b.name)
b.a
b.a=9999
b.a
del b.a
b.a







class Bank:

    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    @property
    def a(self):
        print(self.__pin)
    @a.setter
    def a(self,new_pin):
        self.__pin=new_pin
    @a.deleter
    def a(self):
        del self.__pin
b=Bank('Dinga',1234)
print(b.name)
b.a
b.a=8989
b.a
del b.a
b.a


'''