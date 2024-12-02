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




'''