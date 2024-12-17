'''
Collection datatype

1.String

It is collection of charater
string bountry is single quotes
It  is a ordered datatype
it is support indexing and slicing
default value is ''
It is immutable datatype


Types od string



1.upper
2.lower
3.swapcase
4.Capitalize
5.Title
6.index
7.rindex
8.find
9.rfind
10.count
11.replace
12.join
13.split
14.rsplit
15.strip
16.rstrip
17.lstrip
18.startswith
19.endswith
20.isupper
21.islower
22.isalpha
23.isalnum
24.isdigit
25.isspace
26.isidentifier




1.upper
it is used to convert lowercase into uppercase

2.lower
It is used to convert into uppercase into lowercase

3.swapcase
It is used to  convert lowercase into uppercase and uppercase into lowercase


4.Capitalize

It is used to convert first letter convert lowercase into uppercase

5.Title

It is used to allthe fiest word connvert into lowercse into uppercase


6.index
it is used in findx the first occured of specific in left side
It return value erroe if specific element is not present


7.rindex
it is used to find the first occured sof specific element inright side
it return value error if specific element not present

8.find

It is used to find the first occured specific element in left side
it return -1 if specific element is not present

9.rfind

 it is used to find the first occured specific element in right side
 It return -1 if specific element is not present

 10.count
 It isused to returm how many times element are present
 it return if the specific not present

 11.replace

 It is used replace the old chracter into new character
 If not give the character not the original string

 Syntax
 string.replace(old character,new character[count])


12.join
join travels through iterable

string.join(iterable


13.split()
it is used find the first occured specific element based on left side
default spit is used space


14.rsplit

It is used find the first occured specific element basec on r9ght side
default rsplit through space

syntrax

string.split(character,[max character])


15.strip
It is used strip the character from leading point to trailing point

16.lstrip

it is used strip the character from leading point


17.rstrip

it is used strip the character from tailing point



18.Startswith
It is check the condition wheter substring are stratswith or not

syntax
string.startswith(substr)


19.Endswith
It is chec the condition whevther substring endswith or not

syntax
string.endswith(substr)

20.isupper
if return if cindition uppercase
return boolean value

21.islower
it return if condition is lower

22.isalpha

it return if cindition is only aphabet

23.isdigit
it return if condition is only number

24.isalnum

it return if condition having alphabet,number or numeric vzlue


25.isspace


26.Isidentifier

it is inbuild method whereter check condition are identifier or not...










2,...List


it is collection homogenous and hetrogenous


homogenous---[1,2,3,4,5,6,7]-----int
hetrogenous---[1,0.2,True,1+2j,'Hekllo]---int,float,complex,boolean,string

bountey of list is cloasd brackets
it is ordered datatype
it support indexing and slicing
it is mutable datatype
default value is []


nexted list

listis combine with another list




Types of list


1.append
2.extend
3.insert
4.index
5.remove
6.pop
7.clear
8.count
9.reverse
10.sort
11.copy




1.append

it is used app lement at last
 it accent both individual and collection datatype
it will add theelement as it is


syntax

list.append(element)




2.extend

It Is used to add the element at last
it accept only collection datatype
 it occour only unpacking

syntax

list.extend(iterable)



3.insert


it is add  the element based on index
syntax

list.insert(index,element)




4.index

it is used to find the first occured specific element in left side

syntax
list.index(index)



5.remove
it is remove the first occured specific based on element
list.remove(element)


6.pop
it is pop the first occured specific based on index

7.clear

It is used cleae the all element
it show empty square brackets


8.count

it return how many times elemee are present in the collection

syntax
list.count(element)


9.reverse

it is used reveese the element

syntax
list.reverse()


10.sort

it is used to arrange the value ascendibng and descending value
default it assign ascending order
syntax

list.sort(key=true/False)



11.copy

three type
1.=operatotr
2.copy() method
3.deepcopy()


1.= operator  (normal copy)
it is used copy the data from one list to another list
if change the value main frame valuse also change and nested frame also change


2.copy()or(shallow copy)

it is used copy the data from one list to another list
if the valuse change main frame not change but nested frame different


3.deepcoyp

it is used to copy the data from one list to another list
it use only import deepcopy
from copy import deepcopy
if change main frame and nexted not change the value


sntax

deepcopy()






3.tuple


it is used collection of homogenous and hetrogenous
bountry is parasynthesis
it is orderdatype
it support indexing and slicing
it is immutable
default value is ()



types


1.index

it is used to find the first occcursed specific element on left side
it raise value error



2.count
it used count hoe many times lement are repeated

syntax
tuple.count(element)








4.Set
it ia acollection of homogrnous and hetrogenous
boundry is curly brackrts
it is not support ordered list
it iss not support indexing and slicing
it is mutable
defult is set()




types

1.union
2.update
3.intersection
4.intersection_update
5.difference
6.difference_update
7.symmmertic_difference
8.symmertric_difference_update



1.union
it is used to retuen value of both baseset and iterable by removing duplicates


syntax
baseset.union(iterable)


2.update
it update the value of both baseset and iterable by removing duplicates or repeated value

syntax
baseset.update(iterable)



3.intersection
it is return the common value of both baseset and iterable

symtax
baseseet,intersection(iterable)


4.intersection_update
it is update return the common value of both baseset and iterable

syntax

baseset.intersection_update(iterable)



5.difference
it is return the value of baseset but not in itereable andremoving duplixcayes

syntax
baseset.difference(iterable)


6.it is update the return value baseset but not in iterable

syntax
baseset.difference_update(iterable)


7.symmertic_difference

it return uncommon element uncommon value based on both baseset and iterable

syntax
baseset.symmertic_difference(iterable)




8.symmertic_difference_update
it update the return uncommon value based on both baseset and itrerable

syntax
baseset.symmertic_difference_update(iterable)








Muttable datatype

modification

1.add
2.update
3.remove
4,discard
5.pop
6.clear
7.issuperset
8.issubset
9.isdisjoint








1.add
it is used to add the element unorcdered
ut is nit allow duplicates


2.update
it used to update the value randomly



3.remove

it is  remove the value based on element
if the specific element is not present it show erroer



4.discard

it is also remove the valuebased on element
if the element is not presentit doesnot show any erroe



5.pop

it used to return the value based on based on index
if the element not present it aremove the element at last


6.clear

it remove the all the element












5.Dictionary

itis  pair of key  and values
it is sepeated by colon
it is seperated by comma
it is orderd data
it is mutable but inside value is immutable
default valuse is {} or dict


Types
1.keys
2.values
3.items
4.get
5.update
6.clear
7.pop
8.popitem
9.fromkeys
10.setdefault




1.keys
it return only keys
dict_keys


2.values

it return only values
dict_values

3.items
it return tuple value of pair in keys and values


4.get


5.update



7.pop



8.popitem


9.fromkeys



10.setdefault






# ---------------------------------------------------------------------------------------------------------------------------------


'''
from itertools import zip_longest
from mimetypes import inited

'''

                                            Part=2
                                            



a=10
print(type(a))
print(float(a))
print(bool(a))
print(complex(a))
print(str(a))
print(list(a))
print(tuple(a))
print(set(a))
print(dict(a))







a=10.0
print(int(a))

print(bool(a))
print(complex(a))
print(str(a))
print(list(a))
print(tuple(a))
print(set(a))
print(dict(a))





a=True
print(int(a))
print(float(a))
print(complex(a))
print(str(a))
print(list(a))
print(tuple(a))
print(set(a))
print(dict(a))









a=10+10j
# print(int(a))
# print(float(a))
print(bool(a))
print(str(a))
# print(list(a))
# print(tuple(a))
# print(set(a))
# print(dict(a))




a='hello'
print(int(a))
print(list(a))
print(bool(a))
print(complex(a))
print(str(a))
print(list(a))
print(tuple(a))
print(set(a))
print(dict(a))




2.Operatorts


1.Arithmatic
2.relational
3,logical
4,membership
5.assignment
6.identify 
7.bit -wise identify


1.Arithematic

print(10+10)
print(10-2)
print(10*2)
print(10%2)
print(10/2)
print(10//2)


2.Relational 

print(10>20)
print(10<20)
print(2>=2)
print(5<=2)
print(2==2)
print(5!=3)


3.Logical

print(100 and 200)
print(100 or 200)
print(not 100 or 200)


memebership

s='heelos '
if 's' in s:
    print('Yrs')
    
    
assignment


a=10
b=20


identify
    


a=20
b=200
print(a is b)


bitwise
    and

print(128 & 4)




    or
    

print(16 | 21)

   xor


print(16 ^ 21)


   not


print(-(5+1))

   Left shift
   


print(12<<1)

     right shift
print(12>>1)


string format

1.%   

       1.int-%d
       2.float-%f
       3.string-%s
2.format
3.f





Input

a=10




output


a=10

10





print



a=10
print(a)



10





control statement

1.conditional
2.control



1.conditional


       1.if
       2,if else
       3,if elif
       4.nexted if


1.if

a=10
if a>=10:
    print(a)


2.if else


a=10
if a>=10:
    print(a)
else :
    print(a-a)


3.if elif

a=10
if a>10:
    print(a)
elif a<=10:
    print(a)
else:
    print(a)



4.nested if

a=10
if a<=10:
    if a==1:
        print(a)
    else:
        print(a-a)
else:
    print(a)





looping


while
for





          Number Program
           
           
           1.Number reverse
           
           
a='1234'
print(a[::-1])




a=1234
sum=0
i=0
while a>0:
    rem=a%10
    sum=sum*10+rem
    a=a//10
print(sum)




2.Number palindrome


a=12321
b=a
sum=0
while a>0:
    rem=a%10
    sum=sum*10+rem
    a=a//10
if b==sum:
    print('Palindrome')
else:
    print('Not')



3.Fibanocci


a=0
b=1
print(a,b,end=' ')
while a<=10:
    c=a+b
    print(c,end=' ')
    a=b
    b=c



4.Factorial


num=5
sum=1
while num>0:
    sum=sum*num
    num=num-1
print(sum)



5.Perfect  Number


num=6
a=num
sum=0
i=1
while num>i:
    if num%i==0:
        sum=sum+i
    i+=1
if a==sum:
    print('Yes')
else:
    print('Not')



6.Perfect square



a=25
b=a
c=a**0.5
d=int(c)
e=c*c
if b==e:
    print('Perfect Square')
else:
    print('Not')



7.Sum of the number


a=12345
sum=0
while a>0:
    rem=a%10
    sum=sum+rem
    a=a//10
print(sum)



8.Strong Number

a=145
b=a
sum=0
while a>0:
    rem=a%10
    fact=1
    while rem>0:
        fact=fact*rem
        rem=rem-1
    sum=sum+fact
    a=a//10
if b==sum:
    print('Strong Number')
else:
    print('Not')



9.amstrong Number


a=153
b=a
c=len(str(b))
sum=0
fact=1
while a>0:
    rem=a%10
    fact=rem**c
    sum=sum+fact
    a=a//10
if b==sum:
    print('Amstrong Number')
else:
    print('Not')



10.Harshad Number

a=124
b=a
sum=0

while a>0:
    rem=a%10
    sum=sum+rem
    a=a//10
if b%sum==0:
    print('Harshad Number')
else:
    print('Not')


11.Xylem and pyleoem


a=1234
b=a
o_sum=0
i_sum=0
while a>0:
    rem=a%10
    if a==b or a<10:
        o_sum=o_sum+rem
    else:
        i_sum=i_sum+rem
    a=a//10
if o_sum==i_sum:
    print('Xylem')
else:
    print('Pylem')


12.prime Number


a=7
i=2
res=True
while a>=i:
    if a%i==0:
        res=False
        break
    i+=1
if res == True:
    print('Prime Number')
else:
    print('Not')



13.Happy Number


a=13
while a>9:
    sum=0
    while a>0:
        rem=a%10
        sum=sum+rem**2
        a=a//10
    a=sum






For Loop



lst=[1,2,3,4,5]
for i in lst:
    print(i)



loop control
      1.break
      2,continue
      3.pass
      
      
1.break

lst=[1,2,3,4,5,6,7,8,9]
for i in lst:
    if i>9:
        pass
    else:
        print(i)



In-build Method

1.type
2,id
3.dic
4.round


print(round(10.7))

5.help
6.len
7.abs

print(abs(-10))


8.divmod
print(divmod(10,2))


9.input
10.output
11.range
12.Enumerate


lst=['hi','hello','bye','good']
for i in enumerate(lst):
    print(i)

13.zip


lst1=['hello','hi']
lst2=['bye','good']
for i in zip(lst1,lst2):
    print(i)



14.zip_longest

lst1=['hello','hi','welcome']
lst2=['bye','good']
for i in zip_longest(lst1,lst2,fillvalue='none'):
    print(i)


15.Compreshion

a=[i**2 for i in range(1,6)]
print(a)


Pattern



n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




'''








# -----------------------------------------------------------------------------------------------------------------------------------------



'''
                                                Part-3



1.Function

Function is a block of code or set of instriuction which are used to perform from some specific tasks whenever we call



def function_name(Parameters):
        statement
        return data
function_name(argument)


2.return 

Return is a keyword which is used return the data
to the function calling


Types of Arguments

1.Postional
2.keyword
3.combination of positional and keyword
4.only positional
5,.only Keywords
6.combination of only positional and keyword
7.variable positional
8.variable keywords
9.combination of possitional and keyword



1.positional

def add(a,b):
    return a+b
print(add(10,20))



2.keywords

def add(a,b):
    return a+b
print(add(a=10,b=20))



3.combination positional and keyword


def add(a,b):
    return a+b
print(add(10,b=20))



4.only possitional

def add(a,b,/):
    return a+b
print(add(10,20))



5.only Keyword


def add(*,a,b):
    return a+b
print(add(a=10,b=20))



6.combination of only keyword and positional


def add(a,/,*,b):
    return a+b
print(add(10,b=20))



7.variable positional

def add(*args):
    print(*args)
(add(10,20))



8.variable keywords

def add(**kwargs):
    print(kwargs)
add(a=10,b=20)



9.combination of *args and **kwargs


def add(*args,**kwargs):
    print(*args,kwargs)
add(10,20,c=30,d=40)






generator

it is used to generator a sequence of value
it is used to generator with the help of def keyword and we not use return we use yeild keyword


def function_name(parameter):
      yeild data
function name(argument) 


# def even():
#     for i in range(1,11):
#         if i%2==0:
#             return i
# print(list(even()))

def even():
    for i in range(1,11):
        if i%2==0:
            yield i
print(list(even()))





oops


object oriented programming system

         1.class
         2.object
         3.inheritance
         4.polymorhims
         5.abstraction
         6.Encapsulation



1.Class

class is a  blueprint or templete which are uded to create the object


syntax

class class_name:
    ststement
    
    
    
    
    
2.object

Object is a instance of a class or real time entity



syntax

object_name=class_name




3.Inheritance


inheritance properties is used one class to another class is called inheritance

          1.Single level inheritance
          2.multi level inheritance
          3.Multiple inheritance
          4.Hirarchical inheritance
          5.Hybrid inheritance
          
          
1.Single Level Inheritance


the inheritance propertied used one super class and subclass is called single level inheritance




class Father:
    def land(self):
        print('land')
class son:
    def house(self):
        print('House')
s=son()
s.house()
f=Father()
f.land()



2.Multi-level inheritance


inheritance propertires one derived class to another derived class is called mult-level




class GrandFather:
    def grandfather(self):
        print('Gold')
class Father(GrandFather):
    def father(self):
        print('land')
class Son(Father):
    def son(self):
        print('House')
g=GrandFather()
g.grandfather()

f=Father()
f.father()

s=Son()
s.son()




3.Multiple inheritance




class Father:
    def land(self):
        print('land')
class Mother:
    def gold(self):
        print('gold')
class Son(Father,Mother):
    def house(self):
        print('House')

s=Son()
s.house()
s.gold()
s.land()



4.Hirarchical inheritance


class Father:
    def land(self):
        print('Land')
class Son1(Father):
    def house1(self):
        print('House1')
class Son2(Father):
    def house2(self):
        print('House2')

s1=Son1()
s2=Son2()
s1.land()
s1.house1()
s2.land()
s2.house2()




5..Hybird

It is inheritence properties combination of multiple and hirarachical



'''


'''
class function_name():
      code
      
      
object_name=class_name



inheritance



1.datatype

1.individual datatype
2.collection datatype



1.individual datatype

1.int
2.flaot
3.boolean
4.complex


1.int-used without decimal point
2.float-using with decimal point
3.boolean-it is either of true or false
4.complex-it is combination of real and imanignary number




2.collection datatype

1.string
2.list
3.tuple
4.set
5.dictionary




1.string
it is collection of a  character
bountry is ""
it is immutable
ordered datatype
indexing and slicing
default value ''



types

1.upper()
s.upper()

2.lower()
s.lower()

3.swapcase()
s.swapcase()


4.capitalize()
s.capitalize()

5.title()
s.title()


6.index()
s.index(element,[s1:ei])

7.rindex()


8.find()
s.find(element.si,ei)


9.rfind()
s.rfind(element,si,ei)


10.count()
s.count(element,si:ei)


11.split()
s.split(character,max_split)


12.rsplit()
s.rsplit(character,max_split)


13.strip()
s.strip(character)


14.rstrip()
s.rstrip(character)


15.lstrip()
s.lstrip(character)


16.join()
s.join(iterable)


17.startswith()
s.startswith(substr,si,ei)


18.endswith()
s.endswith(substr,si,ei)


19.isupper()
s.isupper()

20.islower()
s.islower()

21.isalpha()
s.isalpha()


22.isalnum()
s.isalnum

23.isdigit()
s.isdigit()

24.isspace()
s.isspace()


25.isidentifier()
s.isidentifier()


26.replace()
s.replace(old character,new charcter)







2.List

it is collection of homogenous and hetrogenous
it boundry is []
ordered datadype
indexing and slicing
mutable datatype
default value is []



1.append()
s.append()


2.extend()
s.extend()


3.insert()
s.insert(index,element)


4.index
s.index()


5.remove()


6.pop()
s.pop(index)


7.clear()
s.clear()


8.count()
s.count()


9.sort()

s,sort(key=function,true/false)


10.reverse()
s.reverse()


11.copy()

1.normal copy
lst2=lst1


2.shallow copy()
lst2=lst1.copy()


3.deepcopy()

from copy import deepcopy
lst2=deepcopy(lst1)




---------------------------------------------------------------------------------------

3.tuple()
it ia a collection of homogenous and hetrogenous
ordered datatype
indexing and slicing
boundry is ()
immutable datatype
default value is ()



1.index()
s.index(element)


2.count()
s.count(element)



-------------------------------------------------------------------------------------------------


4.srt
it is a collection of homogenous and hetrogenous
boundry is {}
unorded datatype
mutable
default value set()



1.union()
baseset.union(iterable)

2.update()
baseset.update(iterable)

3.intersection()
basest.intersection(iterable)


4.update_intersection()
basest.update_intersection(iterable)

5.difference()
baseset.difference(iterable)

6.update_difference()
basest.update_difference(iterable)

7.symmetric_difference()
baseset.symmertic_difference(iterable)

8.update_symmertic_difference()
baseset.update_symmertric_difference(iterable)






1.add()



2.update()



3.remove()


4.discard()



5.pop()



6.clear()



7.issuperset()




8.issubset


------------------------------------------------------------------------------




5.dictionary
it is pair of keys and values
seperate by cooma
key an value between colon
ordered datatype
boundery is {}
default value is {}





1.keys()
s.keys()


2.values()
s.values()


3.items()
s.items()


4.get()
s.get()


5.update()
s.update()

6.pop()
s.pop()


7.popitem()
s.popitem()


8.clear()
s.clear()

9.fromkeys()
s.fromkeys()


10.setdefault()

s.setdefault()




-----------------------------------------------------------------------------------------------------

2.control structure

1.conditional statement
2.control statement



1.conditional statement

1.if
2.if elif
3.if else
4.nested if






1.if

a=10
if a>=10:
   print('Yes)




2.if elif

a=10
if a==10:
    print(Yes)
elif a>=10:
    print(Yes Yes)
elif a<=10:
   print(Yes Yes Yes)
   
   
   
3.if else

a=10
if a=10:
   print('Yes')
else:
   print('No')
   
   
   
   
4.Nested if

a=10
if a==10:
    if a>=10:
        print(Yes)
    else:
        print('No)
else:
   print(Invalid)
   
   
   
   
   
   
   
   
2.control statement


1.while
2.for



1.while

a=10
i=0
rem=0
while a>=0:
   rem=rem-a
   a-=1
print(rem)





2.for

for i in range(1,11):
    print(i)
    
    
    
    
---------------------------------------------------------------------------------------------




3.Exception Handling


1.try
2.except
3.else
4.finally





------------------------------------------------------------------------------------------------------



oops

1.class
2.object
3.inheritance
4.polymorishm
5.abstraction
6.Encapsulation






1.class

class inner():
    def __init__(self):
        print('Hello')
    class outer():
        def __init__(self):
            print('Bye')
    o1=outer()
    o1.__init__()
i1=inner()
i1.__init__()



2.object


class inner():
    def add(self,a,b):
        print(a+b)
    add(10,20)
i1=inner()
i1.add()


3.inheritance

1.Single level inheritance
2.Multi level inheritance
3.Multiple inheritance
4.hierarchical inheritance
5.Hybrid inheritance



1.Single level inheritance

   
class Father():
    def land(self):
        print('Land')
class Son(Father):
    def house(self):
        print('House')
f=Father()
f.land()
s=Son()
s.land()
s.house()



2.Multi level inheritance


class Grandfather():
    def gold(self):
        print('Gold')
class Father(Grandfather):
    def land(self):
        print('Land')
class Son(Father):
    def house(self):
        print('House')
g=Grandfather()
g.gold()
f=Father()
f.gold()
f.land()
s=Son()
s.house()
s.land()
s.gold()




3.Multiple inheritance



class Father():
    def land(self):
        print('Land')
class Mother():
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



4.hierarchical




class Father():
    def land(self):
        print('Land')
class Son1(Father):
    def house(self):
        print('House1')
class Son2(Father):
    def house(self):
        print('House2')
f=Father()
f.land()
s=Son1()
s.land()
s.house()
s1=Son2()
s1.land()
s1.house()



5.Hybird



class Animal():
    def sound(self):
        print('Sound')
class Lion(Animal):
    def one(self):
        print('Lion')
class Tiger(Animal):
    def two(self):
        print('Tiger')
class Liger(Lion,Tiger):
    def three(self):
        print('Liger')
a=Animal()
a.sound()

l=Lion()
l.sound()
l.one()

t=Tiger()
t.sound()
t.two()

l1=Liger()
l1.sound()
l1.one()
l1.two()
l1.three()





4.Poylmormishm


1.respect with operator
2.respect with function
3.rescept with inheritance







1.respect with operator

1.+

print(20+30)
print('Computer ' + 'Science')

2.-


print(30-10)
print({1,2,3,4}-{1,2,3})


3.*

print(10*20)
print('=' * 10)




5.Encapsulation


1.public
2.protected
3.private



1.Public


class Sample:
    def land(self):
        print('Land')
s=Sample()
s.land()





class Sample:
    def __init__(self,a,b):
        self.a=a
        self.b=b
s=Sample(10,20)
print(s.a)
print(s.b)


2.Protected



class Sample():
    def __init__(self,name,pin):
        self.name=name
        self._pin=pin
s=Sample('Dinga',1234)
print(s.name)
print(s._pin)



3.Private


class Sample():
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
s=Sample('Dinga',1334)
print(s.name)
print(s.__pin)



class Sample():
    def __init__(self,name,pin):
        self.name=name
        self.__pin=pin
    def get_pin(self):
        print(self.__pin)
    def set_pin(self,new_pin):
        self.__pin=new_pin
s=Sample('Dinga',12345)
print(s.name)
s.get_pin()
s.set_pin(123123)
s.get_pin()




6.Abstraction


from abc import ABC,abstractmethod
class Demo(ABC):
    @abstractmethod
    def chat(self):
        pass

    @abstractmethod
    def reels(self):
        pass

    @abstractmethod
    def story(self):
        pass

    @abstractmethod
    def calls(self):
        pass


class Instragram(Demo):
    def chat(self):
        print('Chatting...')
    def reels(self):
        print('Reels...')
    def story(self):
        print('Story...')
    def calls(self):
        print('Calls...')
i=Instragram()
i.chat()
i.reels()
i.story()
i.calls()




'''





# n=153
# a=n
# b=str(a)
# c=len(b)
# sum=0
#
# i=0
# while n>0:
#     rem=n%10
#     sum=sum+rem**c
#     n=n//10
# if a==sum:
#     print('Amstrong')
# else:
#     print('Not')





# a={'virat kohli','ms dhoni','csk mi rcb rr','ashwin','marnus'}
# dic={}
# for i in a:
#     b=i.split()
#     if len(b)==2 or len(b)==3 or len(b)==4 or len(b)==5:
#         dic[i]=len(i)
#     else:
#         dic[i]=i[::-1]
# print(dic)



# a='AABBBCCDAB'
# b=[]
# count=1
# for i in range(1,len(a)):
#     if a[i]==a[i-1]:
#         count+=1
#     else:
#         b.append(str(count) +a[i-1])
# b.append(str(count) +a[i-1])
# print(b)



# Lambda


# a=lambda a,b,c,d:a+b+c+d
# print(a(10,20,30,40))




# a=lambda n,no:no[::-1]
# print(a("hello","hello"))




# map

# lst=[1,2,3,4,5,6,7,8,9,10]
#
# a=lambda sq:sq**2
# print(list(map(a,lst)))


# n=53
# res=True
# i=2
# while n>i:
#     if n%i==0:
#         res=False
#         break
#     i+=1
# if res==True:
#     print("Prime")
# else:
#     print("Not")




# n=53
# icount=0
# count=0
# i=2
# while n>i:
#     if n%i==0:
#         icount=icount+1
#     else:
#         count=count+1
# print(icount)
#



# arr1=[2,9,12,18]
# arr2=[3,5,11,20]
# c=arr1+arr2
# print(sorted(c))



# a=5
# count=0
# for i  in range(1,a+1):
#     if a%i==0:
#         count=count+1
# if count==2:
#     print("Prime")
# else:
#     print("Not")




# def prime(n):
#     count = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             count=count+1
#     if count==2:
#         print("Prime")
#     else:
#         print("Not")
# prime(23)



#
# def prime(n):
#     count=0
#     for i in range(2,n+1):
#         if n%i==0:
#             count=count+1
#     if count==1:
#         print("Prime")
#     else:
#         print("Not Prime")
# prime(int(input("Enter:")))


# 1 to 20     [2,3,5,7,11,13,17,19]



# for i in range(1,21):
#     if i>1:
#         res=True
#         for j in range(2,i):
#             if i%j==0:
#                 res=False
#                 break
#         if res==True:
#             print(i)





#
# n=21
# for i in range(1,n):
#     if i>1:
#         res=True
#         for  j in range(2,i):
#             if i%j==0:
#                 res=False
#                 break
#         if res==True:
#             print(i)


# n=21
# for i in range(1,n):
#     if i>1:
#         res=True
#         for j in range(2,i):
#             if i%j==0:
#                 res=False
#                 break
#         if res==True:
#             print(i)




# #
# n=50
# a=[]
# for i in range(1,n+1):
#     if i>1:
#         res=True
#         for j in range(2,i):
#             if i%j==0:
#                 res=False
#                 break
#         if res==True:
#             a.append(i)
# print(a)



#
#
#
# def prime(n):
#     a=[]
#     for i in range(1,n+1):
#         if i>1:
#             res=True
#             for j in range(2,i):
#                 if i%j==0:
#                     res=False
#                     break
#             if res==True:
#                 a.append(i)
#     print(a)
# prime(50)






#
#
# arr1=[2,9,12,18]
# arr2=[3,5,11,20]
# arr3=[]
# a=len(arr1)
# b=len(arr2)
# i=0
# j=0
# while i<a and j<b:
#     if arr1[i]<arr2[j]:
#         arr3.append(arr1[i])
#         i+=1
#     else:
#         arr3.append(arr2[j])
#         j+=1
# print(arr3)









# arr1=[2,9,12,18]
# arr2=[3,5,11,20]
# arr3=[]
# a=len(arr1)
# b=len(arr2)
# i=0
# j=0
# while i<a and j<b:
#     if arr1[i] < arr2[j]:
#         arr3.append(arr1[i])
#         i+=1
#     else:
#         arr3.append(arr2[j])
#         j+=1
# print(arr3)
#



#
#
# arr1=[2,9,12,18]
# arr2=[3,5,11,20]
# arr=[]
# a=len(arr1)
# b=len(arr2)
# i=0
# j=0
# while i<a and j<b:
#     if arr1[i]<arr2[j]:
#         arr.append(arr1[i])
#         i+=1
#     else:
#         arr.append(arr2[j])
#         j+=1
# print(arr)




# def remove(n):
#     a=n
#     b=""
#     for i in a:
#         if i not in b:
#             b=b+i
#     print(b)
# remove("racecar")



# arr=[1,2,3]
# [1] [1,2] [1,2,3]

#
# a=[1,2,3]
# b=[]
# c=len(a)
# for i in range(c):
#     for j in range(i,c):
#         b.append(a[i:j+1])
# print(b)

#
#
# def arr(n):
#     a=n
#     b=[]
#     c=len(a)
#     for i in range(c):
#         for j in range(i,c):
#             b.append(a[i:j+1])
#     return b
# print(arr([1,2,3]))





# a = "abcabcbb"
# b=""
# c=len(a)
# for i in a:
#     if i not in b:
#         b=b+i
# print(b)






# a = "bbbbb"
# b=""
# c=len(a)
# for i in a:
#     if i not in b:
#         b=b+i
# print(len(b))
#




# def repeat(n):
#     a=n
#     b=""
#     for i in a:
#         if i not in b:
#             b=b+i
#         print(len(b))
# repeat("bbbbb")




# print(1+2)
# print(1+'2')


# class A:
#     val=1
# class B(A):
#     pass
# class C(A):
#     pass
# a=A()
# print(A.val,B.val,C.val)
# B.val=2
# print(A.val,B.val,C.val)
# A.val=3
# print(A.val,B.val,C.val)



#
# data=50
# try:
#     print(data/0)
# except ZeroDivisionError:
#     print("Canntot div by 0")
# else:
#     print("Print")
# try:
#     print(data/5)
# except:
#     print("yes")
# else:
#     print("GFD")







# r=lambda q:q*2
# s=lambda q:q*3
# x=2
# x=r(x)
# x=s(x)
# x=r(x)
# print(x)




# print(4.5//2)




#
# a=True
# b=False
# c=False
# if 0 or 1 and 0:
#     print(1)
# elif 0 or 0 and 0:
#     print(2)
# elif 0 or 0 or 1 and 0:
#     print(3)
# else:
#     print(4)






# def num():
#     return True,"hello",1
# print(num,type(num))
0


# print(int(21.13))


#
# for i in range(2):
#     for i in range(4,6):
#         print(i)




# count=1
# def do():
#     global  count
#     for i in range(3):
#         count=count+1
# do()
# print(count)





# l=[1,2,3,4]
# l.append([5,6,7,8])
# l.extend([6,7,8])
# print(len(l))



#
#
#
# dic={1:1,2:2,3:3}
# dic[1]+=10
# del dic[1]
# dic[1]='10'
# del dic[2]
# dic.pop(3)
# dic[2]=0
# dic['2']=3
# dic['2']+=1
# dic.pop(2)
#
#





































