'''

Function.....

                           SYNTAX
                        def function_name(parameter):
                              statement 1
                              statement 2
                              return data
                        function_name(argument)



'''
'''
sum the two number

print condition



a=10
b=10
print(a+b)






def add(a,b):
    sum=a+b
    print(sum)
add(10,20)





def addddd(a,b):
    return a+b
print(addddd(10,10))





def adddd(a,b,c):
    return a+b+c
print(adddd(10,10,10))







def add(a,b):
    print(a+b)
add(10,20)





2.print('hello') ('hi')






Normal statement
__________________________________________________


print('Hello')
print('hi')


print('Hello',end=' ')
print('Hi')





Function Statement
__________________________________________


def demo():
    print('Hello')
    print('Hi')
demo()




def demo():
    return 'Hello','Hi'
print(demo())





def demo():
    return 'Hello'
print(demo())
print('Hi')



3..waf to return hello if the user given number is even else retuen bye



Normal (if else condition)
----------------------------------------------------------


no=int(input('Enter:'))
if no%2==0:
    print('Hello')
else:
    print('Bye')



Function
---------------------------------------------------------------


def demo(no):
    if no%2==0:
        return 'Hello'
    else:
        return 'Bye'
no=int(input('Enter'))
print(demo(no))






def palindrome(no):
    n=no
    a=0
    while no>0:
        rem=no%10
        a=a*10+rem
        no=no//10
    print(a)
    if n==a:
        return 'True'
    else:
        return 'False'
print(palindrome(int(input('Enter:'))))




lst1=[1,2,3]
lst2=lst1
lst2.append(4)
print(lst1)






def add(a,b):
    return a+b

print(add(20,10))






def calculator(a,b,c):
    return a+b+c
print(calculator(10,20,30))





def calculator(a,b,c):
    return a+b+c
print(calculator(a=10,b=20,c=30))




def add(a,b):
    return
a=int(input('Enter:'))
b=int(input('Enter:'))
print('1.+\n'
      '2.-\n'
      '3.*\n'
      '4./\n'
      '5.//\n'
      '6.%\n'
      '7./ and %')
option=int(input('Enter:'))
if option==1:
    def add(a,b):
        return a+b
    print(add(a,b))
elif option==2:
    def add(a,b):
        return a-b
    print(add(a,b))
elif option==3:
    def add(a,b):
        return a*b
    print(add(a,b))
elif option==4:
    def add(a,b):
        return a/b
    print(add(a,b))
elif option==5:
    def add(a,b):
        return a//b
    print(add(a,b))
elif option==6:
    def add(a,b):
        return a%b
    print(add(a,b))
elif option==7:
    def add(a,b):
        return a/b,a%b
    print(add(a,b))
else:
    print('Invalid')




'''