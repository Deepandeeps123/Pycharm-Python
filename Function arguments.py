'''
Function arguments
'''
from tkinter.messagebox import ERROR

'''
            Function Syntax
            
            def function_name(Parameters)
                     code
                     return data
            function_name(argument)
'''
'''
Argument Types
1.positional Argument
---------------------------------------------------------


'''

'''

def data(name,age):
    print(f'Hey {name} your age is {age}')
data('dinga',22)



def data(name,age):
    return name,age
print(data('Dinga',22))



def data(name,age):
    print(f'Hey {name} your is age {age}')
data('dingi',22)




def data(name,age):
    print(f'Hey {name} your age is {age}')
data(22,'dingi')
data (22,'dingi')
data(22,22)
data('dinga','dinga')





2.......Keyword Argument
-----------------------------------------------------------------


def data(a,b):
    print(f'{a}+{b}={a+b}')
data(10,10)




def data(a,b):
    print(f'{a}+{b}={a+b}')
data(a=10,b=10)



def data(a,b):
    print(f'{a}+{b}={a+b}')
data(10,b=20)





def data(name,age,salary):
    print(f'Hey {name} your age is {age} and salary is {salary}')
data('dinga',22,salary=2000)
data(name='dinga',age=22,salary=2000)
data(name='dinga',age=22,salary=2000)






def data(name,age):
    print(f'Hey {name} your age is {age}')
data(name='dinga',age=22)
data(name=22,age='Dinga')




3...Combination of positional and keyword argument


def data(name,age):
    print(f'Hey {name} your age is {age}')
data('dinga',22)




def data(name,age):
    print(f'Hey {name} your age is {age}')
data(name='dinga',age=22)




def data(name,age):
    print(f'Hey {name} your age is {age}')
data('dinga',age=22)




ERROR---------------------------------------------------------------

def data(name,age):
    print(f'Hey {name} your age is {age}')
data(name='Dinga',22)



data(name='Dinga',22)
                   ^
SyntaxError: positional argument follows keyword argument





def data(a,b,c,d):
    print(f'{a}+{b}+{c}+{d}={a+b+c+d}')
data(1,2,3,4)




def data(a,b,c,d):
    print(f'{a}+{b}+{c}+{d}={a+b+c+d}')
data(b=2,c=3,d=4,a=1)




def data(a,b,c,d):
    print(f'{a}+{b}+{c}+{d}={a+b+c+d}')
data(2,3,4,1)



(Positinal argument)

def data(a,b,c,d):
    print(f'{a}+{b}+{c}+{d}={a+b+c+d}')
data(1,2,3,4)


(keyword argument)

def data(a,b,c,d):
    print(f'{a}+{b}+{c}+{d}={a+b+c+d}')
data(a=1,b=2,c=3,d=4)


Combination of positional and Keyword arguments




1...Error-------------------------------------------------

def data(a,b,c,d):
    print(f'{a}+{b}+{c}+{d}={a+b+c+d}')
data(1,2,a=2,d=4)



2...

def data(a,b,c,d):
    print(f'{a}+{b}+{c}+{d}={a+b+c+d}')
data(1,2,c=3,d=4)






Return Function


def data(a,b,c,d):
    return a,b,c,d,(a+b+c+d)
print(data(1,2,c=3,d=4))





4......only Positional Argument

def data(a,b,c,d):
    print(a+b+c+d)
data(1,2,3,4)




def data(a,b,c,d):
    print(a+b+c+d)
data(a=1,b=2,c=3,d=4)





def data(a,b,c,d):
    print(a+b+c+d)
data(1,2,c=3,d=4)




def data(a,b,c,d):
    return a+b+c+d
print(data(1,2,3,4))


def data(a,b,c,d):
    return a+b+c+d
print(data(a=1,b=2,c=3,d=4))




def data(a,b,c,d):
    return a+b+c+d
print(data(1,2,c=3,d=4))




def data(a,b,c,d,/):
    return a+b+c+d
print(data(1,2,3,4))





Error---------------------


#   print(data(a=1,b=2,c=3,d=4))
#           ^^^^^^^^^^^^^^^^^^^^^
# TypeError: data() got some positional-only arguments passed as keyword arguments: 'a, b, c, d'

def data(a,b,c,d,/):
    return a+b+c+d
print(data(a=1,b=2,c=3,d=4))








def data(a,b,c,/,d):
    return a+b+c+d
print(data(1,2,3,d=4))
print(data(1,2,c=3,d=4))    # ERROR_------------






def data(a,b,/,c,d):
    return a+b+c+d
print(data(1,2,3,d=4))
print(data(1,2,c=3,d=4))
print(data(1,b=2,3,4))     #Error-------------------------------




5..Only Keywords argument

def data(a,b,c,d):
    return a+b+c+d
print(data(1,2,3,4))




def data(a,b,c,d):
    return a+b+c+d
print(data(a=1,b=2,c=3,d=4))



def data(a,b,c,d):
    return a+b+c+d
print(data(1,2,c=3,d=4))




def data(*,a,b,c):
    return a+b+c
print(data(1,2,3))------------------>Error



def data(*,a,b,c):
    return a+b+c
print(data(a=1,b=2,c=3))





def data(a,*,b,c):
    return a+b+c
print(data(1,b=2,c=3))



def data(a,b,*,c):
    return a+b+c
print(data(1,2,c=3))







6..combination of only positional and only Keyword argument 
----------------------------------------------------------------------------------------


def data(*,a,b,c,/):
    return a+b+c
print(data(a=1,b=2,c=3))




def data(a,b,c,/,d,e,f):
    return a+b+c+d+e+f
print(data(1,2,3,4,5,6))





def data(a,b,c,d,e,*,f):
    return a+b+c+d+e+f
print(data(1,2,3,4,5,f=6))




def data(a,b,c,/,d,e,f,*):
    return a+b+c+d+e+f
print(data(1,2,3,d=4,e=5,f=6))





def data(a,b,c,/,*,d,e,f):
    return a+b+c+d+e+f
print(data(1,2,3,d=4,e=5,f=6))





7..Variable Positional Argument
-------------------------------------------------------------------------------
def data(*args):
    return (*args)
print(data(1,2,3,4))




def data(*args):
    print(*args)
data(1,2,3,4)



def data(*args):
    print(args)
data(1,2,3,4)



def data(*args):
    sum=0
    for i in args:
        print(i)
data(1,2,3,4)



def data(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
data(1,2,3,4,5,6,7,8,9,10)




def data(*args):
    print(sum(args))
data(1,2,3,4,5,6,7,8,9,10)



def sample(*args):
    return args
print(sample(1,2,3,4))





def sample (*args):
    print(*args)
sample(1,2,3,4)




def sample(*args):
    print(args)
sample(1,2,3,4)





def sample(*args):
    print(*args)
    print(args)
sample(1,2,3,4)





8.variable Keyword argument(**kwargs)
--------------------------------------------------------------------------------------------------
def sample(**kwargs):
    print(*kwargs)
sample(a=10,b=20,c=30)





def sample(**kwargs):
    print(kwargs)
sample(a=1,b=2,c=3,d=4)






def sample(**kwargs):
    print(kwargs)
sample(a=1,b=2,c=3)




9...Combination of a *args and **args
-------------------------------------------------------------------------
1..
def p_a(*args):
    print(args,*args)
    print(args)
    print(*args)
p_a(1,2,3,4,5,6,7,8,9,10)


2..



def k_a(**kwargs):
    print(kwargs,*kwargs)
    print(kwargs)
    print(*kwargs)

k_a(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10)





def add(*args,**kwargs):
    print(args,kwargs)
add(1,2,3,4,5,a=1,b=2,c=3,d=4,e=5)
add(10,20,30,a=40,b=20,c=30)






example,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
--------------------------------------------------------------------

1...wap to return sum of possional and keyword argument




def sum1(*args,**kwargs):
    print(args)
    print(kwargs)
sum1(10,20,30,a=40,b=20,c=30)


(10, 20, 30)
{'a': 40, 'b': 20, 'c': 30}



(inbuild method)
def sum1(*args,**kwargs):
    print(sum(args))
    print(sum(kwargs.values()))
sum1(10,20,30,a=40,b=30,c=20)



(without inbuild method)

def sum1(*args,**kwaargs):
    print(kwaargs)
sum1(a=1)




def sum1(*args,**kwargs):
    p_a=0
    k_a=0
    for i in args:
        p_a=p_a+i
    for j in kwargs.values():
        k_a=k_a+j
    print(p_a)
    print(k_a)
sum1(10,20,30,a=40,b=20,c=30)





def sum1(*args,**kwargs):
    p_a=0
    k_a=0
    for i in args:
        p_a=p_a+i
    for j in kwargs:
        k_a=k_a+kwargs[j]
    print(p_a)
    print(k_a)
sum1(10,20,30,a=30,b=20,c=40)




2...Default Parameters

                              Function Syntax
                              
                        def function_name(parameters)
                                  return data
                        function_name(arguments)


def sample(a,b):
    return a+b
print(sample(10,20))




def sample(a,b):
    return a+b
print(sample(a=10,b=20))




def sample(a,b):
    return a+b
print(sample(10,b=20))




def sample(a,b):
    return a+b
print(sample(a=10,20))     #ERROR______







ERROR
-----------------------------------------
def sample(a,b,c,d):
    print(a+b+c+d)
sample(10,20)



ERROR

def sample(a,b,c,d):
    print(a+b+c+d)
sample(a=0,b=20)



ERROR

def sample(a,b,c,d):
    print(a+b+c+d)
sample(10,b=20)





Default
------------



def sample(a,b,c,d=0):
    print(a+b+c+d)
sample(10,20,30)







def sample(a,b,c=0,d=0):
    print(a+b+c+d)
sample(a=10,b=20)




def sample(a,b=0,c=0,d=0):
    print(a+b+c+d)
sample(a=10)



def sample(a=0,b=0,c=0,d=0):
    print(a+b+c+d)
sample()




def sample(a=0,b=0,c=0,d=0):
    print(a+b+c+d)
sample(a=1,b=2,c=3)




2....waf to return Present in even number to print range(1,100) 

for i in range(1,101):
    if i%2==0:
        print(i,end=' ')




res=[]
for i in range(1,101):
    if i%2==0:
        res.append(i)
print(res,end=' ')




def even():
    for i in range(1,101):
        if i%2==0:
            return i
print(even())




output---2






def even():
    for i in range(1,101):
        if i%2==0:
            yield i
print(even())







def even():
    for i in range(1,101):
        if i%2==0:
            yield i
print(even())
print(str(even()))
print(set(even()))
print(tuple(even()))






def even():
    for i in range(1,11):
        return i
        return i+1
print(even())






def even():
    for i in range(1,11):
        print(i)
#         return i
#         return i+1
print(list(even()))





def even():
    for i in range(1,11):
        yield i
print(even())




def even():
    for i in range(1,11):
        yield i
print(list(even()))





def even():
    for i in range(1,11):
        yield i
        yield i+1
print(list(even()))









3.....waf to return to print which are starting with vowels 


lst=['apple','Mango','Tomato','Qspiders','Union']
def vowels(a):
    for i in a:
        if i[0] in 'aeiouAEIOU':
            return i
print((vowels(lst)))






lst=['apple','orange','Tarmaind','qspiders','jspiders']
def vowels(lst):
    res=[]
    for i in lst:
        if i[0] in 'aeiouAEIOU':
#             yield i
# print(list(vowels(lst)))
#               return i
# print(vowels(lst))
              res.append(i)
    print(res)
vowels(lst)






lst=['apple','orange','tarmarind','qspiders','jspiders']
res=[]
for i in lst:
    if len(i)%2==0:
        a=(i,i[::-1])
        res.append(a)
    else:
        b=(i,len(i))
        res.append(b)
print(res)


# lst=['apple','orange','tarmarind','qspiders','jspiders']
# def res(lst):
#     for i in lst:
#         if len(i)%2==0:
#             yield(i,i[::-1])
#         else:
#             yield(i,len(i))
# print(list(res(lst)))




'''

# lst=['apple','orange','tarmarind','qspiders','jspiders']
# res=[]
# for i in range(len(lst)):
#     if lst[-1] not in 'aeiouAEIOU':
#         a=(lst[i],lst)
#         res.append(a)
#     else:
#         b=(lst[i],i[len(i)//2:])
#         res.append(b)
# print(res)



# [('apple', 'ple'), ('orange', 'nge'), ('tarmarind', 2), ('qspiders', 3), ('jspiders', 4)]

#
# lst=['apple','orange','tarmarind','qspiders','jspiders']
# def demo(a):
#     for i,j in enumerate(a):
#         if j[-1] not in 'aeiouAEIOU':
#             yield(j,i)
#         else:
#             yield(j,j[len(j)//2:])
# print(list(demo(lst)))






'''



#decoders

def add(a,b):
    print(a+b)
add(4,5)

def sub(a,b):
    print(a-b)
sub(a=10,b=1)


def mul(a,b):
    print(a*b)
mul(10,b=5)



def div(a,b):
    print(a/b)
div(10,2)


def add(a,b):
    print(f'you got:{a+b}')
add(4,5)



def sub(a,b):
    print(f'you got:{a-b}')
sub(a=10,b=1)


def mul(a,b):
    print(f'you got:{a*b}')
mul(20,b=4)





def div(a,b):
    print(f'you got:{a/b}')
    div(20,2)


def add(a,b):
    print(1+a+2+b)
add(10,20)



def add(a,b):
    print(1+b)
add(10,20)


def outer(func):
    def inner(a,b):
        print(f'you got:',end=' ')
        func(a,b)
    return inner
@outer
def add(a,b):
    print(a+b)
add(4,5)
@outer
def sub(a,b):
    print(a-b)
sub(a=10,b=1)
@outer
def mul(a,b):
    print(a*b)
mul(4,4)
@outer
def div(a,b):
    print(a/b)
div(4,2)



lst=[5,6,7,5,8,9,10,6,11]
a=set(lst)
b=list(a)
print(b[2:])




def outer(func):
    def inner(*args,**kwargs):
        print(f'args:{args} and kwargs:{kwargs}')
        func(*args,**kwargs)
    return inner
@outer

def add(*args,**kwargs):
    print(sum(args),sum(kwargs.values()))
add(1,2,3,4,5,a=1,b=2,c=3,d=4,e=5)




def sum1(*args,**kwargs):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
    sum2=0
    for i in kwargs.values():
        sum2=sum2+i
    print(sum1,sum2)
    print(sum2)
sum1(1,2,3,4,5,a=1,b=2,c=3,d=4,e=5)




from time import sleep
def outer(func):
    def inner(a,b):
        print('Hello everyone:',end=' ')
        sleep(2)
        func(a,b)
    return inner
@outer
def add(a,b):
    print(a+b)
add(4,5)
@outer
def sub(a,b):
    print(a-b)
sub(10,1)
@outer
def mul(a,b):
    print(a*b)
mul(5,5)
@outer
def div(a,b):
    print(a/b)
div(10,2)




def outer(func):
    def inner(a,b):
        print('Hello Compiler')
        func(a,b)
    return inner
@outer
def add(a,b):
    print(a+b)
add(4,5)
@outer
def sub(a,b):
    print(a-b)
sub(4,2)






Hello Compiler
9
Hello Compiler
2





from time import sleep
def n_delay(n):
    def outer(func):
        def inner(a,b):
            print('Hello')
            sleep(2)
            func(a,b)
        return inner
    return outer
@n_delay(3)
def add(a,b):
    print(a+b)
add(4,5)
@n_delay(3)
def sub(a,b):
    print(a-b)
sub(10,3)





n=4
a=1
for i in range(n):
    for j in range(n):
        if i==0 and j==0 or i==0 and j==1 or i==1 and j==0 or (i==0 and j==2):
        # if i<=n and j<=n:
            print(a,end=' ')
            a+=1
        else:
            print(' ',end=' ')

    print()




'''

