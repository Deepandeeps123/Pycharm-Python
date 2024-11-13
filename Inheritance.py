'''
1.Single level inheritance
'''
'''
          father-------son

class Father:
    def land(self):
        print('50 acrs')
class Son(Father):
    def house(self):
        print('3bhk')
f=Father()
s=Son()
f.land()
s.land()
s.house()


2.Multi level inheritance

class Python:
    def software(self):
        print('Python Software')
class Sql(Python):
    def database(self):
        print('Database')
class WT(Sql):
    def frond(self):
        print('Front')
p=Python()
p.software()
s=Sql()
s.database()
s.software()
f=WT()
f.frond()
f.database()
f.software()


3..Multiple inheritance

class Python:
    def program(self):
        print('Developer')
class SQL:
    def Database(self):
        print('Database')
class Full(Python,SQL):
    def Stack(self):
        print('Full Stack Developer')
p=Python()
p.program()
s=SQL()
s.Database()
f=Full()
f.Stack()
f.program()
f.Database()


4.hirarachical inheritance


class Full:
    def Stack(self):
        print('Full Stack')
class Python(Full):
    def Program(self):
        print('Program')
class SQL(Full):
    def Database(self):
        print('Database')
f=Full()
f.Stack()
p=Python()
p.Program()
p.Stack()
s=SQL()
s.Database()
s.Stack()



5.Hybrid inheritance


class Animals():
    def Sound(self):
        print('Sound..')
class Lion(Animals):
    def King(self):
        print('King')
class Tiger(Animals):
    def Speed(self):
        print('Speed')
class Liger(Lion,Tiger):
    def Hunting(self):
        print('Hunting..')
a=Animals()
a.Sound()
l=Lion()
l.King()
l.Sound()
t=Tiger()
t.Sound()
t.Speed()
l1=Liger()
l1.Hunting()
l1.Sound()
l1.King()




class sample:
    @staticmethod
    def disp(msg):
        print(msg)
s1=sample()
s1.disp('I am Static method')



class Teacher:
    def staff(self):
        print('English')
class Student:
    def member(self):
        print('Artificial')
t=Teacher()
s=Student()
t.staff()
s.member()





class Hod:
    def Head(self):
        print('Principle')
class Teacher(Hod):
    def Staff(self):
        print('Web')
class Student(Teacher):
    def member(self):
        print('Artificial')
h=Hod()
t=Teacher()
s=Student()
t.Staff()
t.Head()
h.Head()
s.member()
s.Head()
s.Staff()




class Employee:
    def id(self):
        print('Name')
class Secretary(Employee):
    def args(self):
        print('*args')
class TemporarySecretary(Employee):
    def kwargs(self):
        print('**kwargs')
class Salary_policy(Secretary):
    def payroll(self):
        print('Number')
class Secretary_role(Secretary,TemporarySecretary):
    def work(self):
        print('Hours')
class Hourly_policy(TemporarySecretary):
    def payroll1(self):
        print('Number1')
class  Role(Secretary_role):
    def work1(self):
        print('Hours1')
class Payroll(Salary_policy,Hourly_policy):
    def payroll2(self):
        print('Number2')
e=Employee()
s=Secretary()
e.id()
print(f'{'='*20}')
s.args()
s.id()
print(f'{'='*20}')
t=TemporarySecretary()
t.kwargs()
t.id()
print(f'{'='*20}')
s1=Salary_policy()
s1.args()
s1.id()
s1.payroll()
print(f'{'='*20}')
s2=Secretary_role()
s2.args()
s2.id()
s2.work()
s2.kwargs()
print(f'{'='*20}')
h=Hourly_policy()
h.kwargs()
h.id()
h.payroll1()
print(f'{'='*20}')
r=Role()
r.id()
r.work1()
r.kwargs()
r.args()
r.work()
print(f'{'='*20}')
p=Payroll()
p.args()
p.id()
p.payroll2()
p.kwargs()
p.payroll1()
p.payroll()
print(f'{'='*20}')








class Father:
    def land(self):
        print('20 acres')
class Son(Father):
    def house(self):
        print('3bhk')
s=Son()
s.house()
s.land()



class GrandFathersFather:
    def add(self):
        print('add')
class GrandFather(GrandFathersFather):
    def gold(self):
        print('3 kg of gold')
class Father(GrandFather):
    def land(self):
        print('50 acres')
class Son(Father):
    def house(self):
        print('3bhk')
g=GrandFathersFather()
g.add()
g1=GrandFather()
g1.gold()
g1.add()
f=Father()
f.gold()
f.add()
f.land()
s=Son()
s.add()
s.gold()
s.land()
s.house()





class Father:
    def land(self):
        print('50 acres')
class Mother:
    def gold(self):
        print('20 kg of gold')
class Son(Father,Mother):
    def house(self):
        print('3bhk')
f=Father()
f.land()
m=Mother()
m.gold()
s=Son()
s.land()
s.gold()
s.house()




class Father:
    a=10
    def land(self):
        print('50 acres')
class Son1(Father):
    def house(self):
        print('3bhk')
class Son2(Father):
    def car(self):
        print('Cars')
f=Father()
f.land()
s1=Son1()
s1.house()
s1.land()
s2=Son2()
s2.car()
s2.land()
print(s1.a)
print(s2.a)




class Animals:
    def sound(self):
        print('Sound')
class Lion(Animals):
    def Lion(self):
        print('Hunting')
class Tiger(Animals):
    def Speed(self):
        print('Speed')
class Liger(Lion,Tiger):
    def Height(self):
        print('Height')
a=Animals()
a.sound()
l=Lion()
l.Lion()
l.sound()
t=Tiger()
t.sound()
t.Speed()
l1=Liger()
l1.sound()
l1.Speed()
l1.Height()
l1.Lion()



method overridding


class Whatsapp:
    def chat(self):
        print('Chating..')
    def status(self):
        print('Status....')
    def videocall(self):
        print('Videocall')
w=Whatsapp()
w.chat()
w.status()
w.videocall()



class Sample:
    def add(self):
        print('add')
class Sample1(Sample):
    def sub(self):
        print('Sub')
s=Sample()
s.add()
s=Sample1()
s.sub()
s.add()





class GrandFathersFather:
    def culture(self):
        print('Culture')
class GrandFather(GrandFathersFather):
    def gold(self):
        print('gold')
class Father(GrandFather):
    def land(self):
        print('land')
class Son(Father):
    def house(self):
        print('house')
g=GrandFathersFather()
g.culture()
g1=GrandFather()
g1.culture()
g1.gold()
f=Father()
f.culture()
f.gold()
f.land()
s=Son()
s.culture()
s.gold()
s.land()
s.house()




class Father:
    def land(self):
        print('Land')
class Mother:
    def gold(self):
        print('Gold')
class Son(Father,Mother):
    def house(self):
        print('House')
f=Father()
f.land()
m=Mother()
m.gold()
s=Son()
s.land()
s.gold()
s.house()





class Father:
    def land(self):
        print('Land')
class Son1(Father):
    def land1(self):
        print('land1')
class Son2(Father):
    def land2(self):
        print('land2')
class Son3(Father):
    def land3(self):
        print('Land3')
class Son4(Father):
    def land4(self):
        print('Land4')
f=Father()
f.land()
s=Son1()
s.land()
s.land1()
s1=Son2()
s1.land()
s1.land2()
s3=Son3()
s3.land()
s3.land3()
s4=Son4()
s4.land()
s4.land4()





class Father:
    def land(self):
        print('Land')
class Son1(Father):
    def land1(self):
        print('Land1')
class Son2(Father):
    def land2(self):
        print('Land2')
class Son1Son1(Son1):
    def land1son1(self):
        print('Land1Son1')
class Son1Son2(Son1):
    def land1son2(self):
        print('Land1Son2')
class Son1Son3(Son1):
    def land1son3(self):
        print('Land1Son3')
class Son2Son1(Son2):
    def land2Son1(self):
        print('Land2son1')
class Son2Son2(Son2):
    def land2Son2(self):
        print('Land2Son2')
class Son2Son3(Son2):
    def land3son3(self):
        print('Land2Son3')
f=Father()
f.land()
print(f'{'-'*10}')
s1=Son1()
s1.land()
s1.land1()
print(f'{'-'*10}')
s2=Son2()
s2.land()
s2.land2()
print(f'{'-'*10}')
s3=Son1Son1()
s3.land()
s3.land1()
s3.land1son1()
print(f'{'-'*10}')
s4=Son1Son2()
s4.land()
s4.land1()
s4.land1son2()
print(f'{'-'*10}')
s5=Son1Son3()
s5.land()
s5.land1()
s5.land1son3()
print(f'{'-'*10}')
s6=Son2Son1()
s6.land()
s6.land2()
s6.land2Son1()
print(f'{'-'*10}')
s7=Son2Son2()
s7.land()
s7.land2()
s7.land2Son2()
print(f'{'-'*10}')
s8=Son2Son3()
s8.land()
s8.land2()
s8.land3son3()
print(f'{'-'*10}')








class Whatsapp:
    def chat(self):
        print('Chating')
    def status(self):
        print('Status')
class Whatsapp_v1(Whatsapp):
    def videocall(self):
        print('Videocall')
w=Whatsapp()
w.chat()
w.status()
w1=Whatsapp_v1(+)
w1.status()
w1.chat()
w1.videocall()






class Whatsapp:
    def chat(self):
        print('Location,Payment')
    def status(self):
        print('Status')
class Whatsapp_v1(Whatsapp):
    def contact(self):
        print('Contact')
w=Whatsapp()
w.chat()
w.status()
w1=Whatsapp_v1()
w1.contact()
w1.chat()
w1.status()                                                                                                                                 




class Whatsapp:
    def chat(self):
        print('Location,Payment')
    def status(self):
        print('status')
class Whatsapp_v1(Whatsapp):
    def chat(self):
        super().chat()
        print('contact')
w=Whatsapp()
w.chat()
w.status()
w1=Whatsapp_v1()
w1.status()
w1.chat()
 




class Sample:
    def add(self,a,b,c=0,d=0):
        print(a+b+c+d)
s=Sample()
s.add(2,3)
s.add(2,3,4)
s.add(2,3,4,5)


'''


'''
4.Polymorphisom
'''
'''
1.operator

print(10+20)
print('Hi'+'Hello')
print([1,2,3]+[4,5,6])
print(['hi','hello']+['bye'])


2.Subraction

print(10-2)
print({1,2,3}-{4,5,6})
s1={1,2,3,}
s2={4,5,6}
s1.difference_update(s2)
print(s1)


3.Multiplication

print(1*2)
print('2'*2)
print(['hi'*2])
print({'hi'*2})
print([1,2,3]*3)
a=[1,2,3,4]
print(*a)
b=('hi','hello','bye')
print(*b)
c={'hi'}
print(*c)




2...Function()

1.String

a='Hello'
print(len(a))

2.List

a=['hello','hi','bye']
print(len(a))


3.Tuple

a=('Hello','hi','bye')
print(len(a))


4.set

a={'hello','hi','bye'}
print(len(a))



5.Set

a={'a':1,'b':2,'c':3}
print(len(a.values))




3.Class Method

class Sample:
    def add(self):
        print('Hello')
class Sample1:
    def sub(self):
        print('Hello')
s=Sample()
s.add()
s1=Sample1()
s1.sub()



class Sample:
    def demo(self):
        print('Hello')
class Sample1:
    def demo(self):
        print('Hello')
s=Sample()
s.demo()
s1=Sample1()
s1.demo()



4...polymorphisom(inheritance)


class Animals:
    def sound(self):
        print('animal sound')
class cat(Animals):
    def sound(self):
        print('Cat sound')
class dog(Animals):
    def sound(self):
        print('Dog sound')
class rat(Animals):
    def sound(self):
        print('rat sound')
a=Animals()
a.sound()
c=cat()
c.sound()
d=dog()
d.sound()
r=rat()
r.sound()




class Sample:
    def demo(self):
        print('Hello')
class Sample1:
    def demo(self):
        print('Hello')
s=Sample()
s.demo()
s1=Sample1()
s1.demo()



inheritance

class Animals:
    def sound(self):
        print('Animal sound')
class Cat:
    def cat(self):
        print('Cat sound')
class Dog:
    def dog(self):
        print('Dog sound')
class Rat:
    def rat(self):
        print('Rat sound')
a=Animals()
a.sound()
c=Cat()
c.cat()
d=Dog()
d.dog()
r=Rat()
r.rat()





user input()


class Animals:
    def sound(self):
        print('animal Sound')
class Cat:
    def sound(self):
        print('Cat sound')
class Dog:
    def sound(self):
        print('Dog sound')
class Rat:
    def sound(self):
        print('rat sound')
a=Animals()
c=Cat()
d=Dog()
r=Rat()
print('1.Animal Sound\n'
      '2.Cat Sound\n'
      '3.Dog Sound\n'
      '4.Rat Sound\n')
option=int(input('Enter the option:'))
if option==1:
    a.sound()
    print(a.sound())
elif option==2:
    c.sound()
elif option==3:
    d.sound()
elif option==4:
    r.sound()
else:
    print('Invalid option')


'''


