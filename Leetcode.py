'''

1.Python key features


pyhton is a dynamic language
easy syntax
It support oops
it support indexing and slicing
It is dynamic language
It is interpreated language


======================================================


2...List and Tuple


list
--------------
it is Hetrogenous and homogenous
boundry is square brackets
ordered datatype
supporting index and slicing
default value []



tuple
-------------

it is homogenous and hetrogrnous
boundry is parasyntesic
it is ordered datatype
it support index and slice
default value is ()



==========================================================


3...Set and dictionary

set
--------
Is is Homeogenous and hetrogenous
boundry is curely brackets
it is unordered datatype
it is not allow duplicate
default value is {}


dictionary
----------


it is pair of key and values
bountry is curly brackets
it is not all duplicates
default value {}


=====================================================


4..self
----------

It is keyword used in oops in class method
self is refered in address

class function_Name():
       def __init__:
              code
              return
varaiable_name=Class Function_name




example

class Demo():
     def __init__(self,a,b):
          self.a=a
          self.b=b
d1=Demo(10,10)
print(d1.a)
print(d1.b)



====================================================


5.lambda


lst=[1,2,3,4,5,6,7,8,9,10]
a=lambda i : i**2
print(list(map(a,lst)))

=======================================================


6.yield



lst=['Apple','Orange','Mango','Bannana']
def Vowel(lst):
    for i in lst:
        if i[0] in 'aeiouAEIOU':
            yield i
print(list(Vowel(lst)))


===========================================================



7.__init__



class Add():
    def __init__(self,a,b):
        print(a+b)
a1=Add(10,10)



==================================================




8.Variable



a=10
b=10.0
c='Hello'
d=['Hi','Bye']
e={'a':10,'b':20,'c':30}
print(a)
print(b)
print(c)
print(d)
print(e)


==================================================================


9.is(id address) and ==


a=10
b=20
if a is b:
    print('Yes')
else:
    print('no')



a=10
b=10
if a is b:
    print('Yes')
else:
    print('no')





a=10
b=10
if a==b:
    print('Equal')
else:
    print('Not Equal')


=================================================


10.Decorators


def outer(func):
    def inner(a,b):
        print('Welcome to Maths')
        func(a,b)
    return inner
@outer
def add(a,b):
    print(a+b)
add(10,20)

@outer
def sub(a,b):
    print(a-b)
sub(10,20)

@outer
def Mul(a,b):
    print(a*b)
Mul(10,20)



====================================================


11..What is python


Python is a high level language
easy syntax
support oops


===============================================================



12.Function


def Function_name(Parameters):
           startement
           return
Function_name(arguments)



def Area(length,width):
    area=length * width
    return area
print(Area(5,10))



=====================================================


13.Difference between List and tuple



list
--------------------------
list is hetrogenous and homogenous
list is mutable
boundry is square brackets
It is ordered datatype
it is suppot index and slicing
default value is empty square brackets



tuple
-------------------------------
tuple is hetrogenous and homogenous
bountry is parathesis
it is ordered datatype
It is support indexing and slicing
defalt value is ()


=======================================================


14.Module


import math
a=math.log(20)
print(a)

========================================================

15.Break and continue


1.Break
----------------------------

a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i%2==0:
        print(i)
        break


lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i==5:
        break
    print(i)




2.Continue
-------------------------------------

a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i%2==0:
        print(i)
        continue




lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i==5:
        continue
    print(i)


=======================================================



16.Iteration(looping)



num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    if i%2==0:
        print(i,'is Even')
    else:
        print(i,'is odd')




======================================================


17.Dictionary

It is a pair of key and values
I is not support index and slice



dic={'a':'CSK','b':'MI','c':'RR'}
print(dic)
print(dic['a'])
print(dic['b'])
print(dic['c'])
print(dic.keys())

=========================================================


18.Factorial Program


a=0
b=0
print(a,b,end=' ')
while a>=0:
    c=a+b
    print(c,end=' ')
a=b
b=c





def Factorial(n):
    return (n==1) or (n*Factorial(n-1))
print(Factorial(5))

==========================================================



19.AemStrong Number



=======================================================



20.Shallow and deep copy


1.Shallow copy
----------------------------------

variable.copy()

Main Frame value only change
No change in nested value



lst=[1,2,3,[4,5,6]]
lst1=lst.copy()
print(lst)
print(lst1)
lst[3]=44
print(lst)
print(lst1)



2.Deepcopy
----------------------------

from copy import deepcopy

deepcopy(iterable)

main frame not changes
Nexted frame also not Change




from copy import deepcopy
lst=[1,2,3,[4,5,6]]
lst1=deepcopy(lst)
print(lst)
print(lst1)
lst[3]=44
print(lst)
print(lst1)

=============================================================



21.Garbage Collection


it is used to freeup the memory allocation


========================================================




22.append and extend



1.append
-------------------

it is add the element at last
it allow both indivual and collection datatype




lst=[1,2,3,4,5]
a=lst.append(10)
print(lst)

b=lst.append('Hello')
print(lst)


2.Extend
------------------


it is also add the element at last
it allow only collection datatype





lst=[1,2,3,4,5]
a=lst.extend('Hello')
print(lst)

b=lst.extend({'hello','hi'})
print(lst)


===============================================


23.Yield(generator)

It is used gengertor the function



def Demo():
    for i in range(1,10):
        if i%2==0:
            return i
print(Demo())




def Demo():
    for i in range(1,10):
        if i%2==0:
            yield i
print(list(Demo()))


==========================================




'''



