'''
syntax
             lambda args1,arg2,...... : expression

'''

# square the nummber
'''

a=2
print(a**2)


a=int(input('Enter:'))
print(a**2)





def square(n):
    return n**2
print(square(int(input('Enter:'))))





def square(n):
    print(n**2)
square(int(input('Enter:')))





def square(n):
    return n**2
print(square(5))





def square(n):
    print(n**2)
square(6)




def square(values):
    return values ** 2
print(square(3))




lambda values : values**3
print(values(2))




a=lambda values : values **2
print(a)





a=lambda values : values **2
print(a(5))






a=lambda values  : values  **2
print(a(int(input('Enter:'))))





#add a 2 number

a=10
b=20
print(a+b)





a=int(input())
b=int(input())
print(a+b)





def add(a,b):
    print(a+b)
add(20,30)




def add(a,b):
    return a+b
print(add(20,30))





a=lambda a,b : a+b
print(a(20,30))






s='Hello'
print(len(s))





s=input()
print(len(s))





def length(n):
    return len(n)
print(length('Hello'))





def length(n):
    return len(n)
print(length(input()))






a=lambda n : len(n)
print(a('Hello every one'))






#find the how many decimal value


# a=10.22222
# 5

a=10.22222
b=str(a)
c=b.split('.')
d=len(c[0]),len(c[1])
e=max(d)
print(e)






def decimal(n):
    b=str(n)
    c=b.split('.')
    d=len(c[1])
    return d
print(decimal(10.22222))




a= lambda n : len(str(n).split('.')[1])
print(a(10.22222))



'''
# a='Hello every one'
# print(a[0:-1])



# s=int(input('Enter:'))
# s1='Hello every one'
# a=s1[-s:]
# print(a)




# def reverse(s,number):
#     return s[-number:]
# print(reverse('Hello every one',5))



# def reverse(s,number):
#     print( s[-number:])
# # reverse(input(),int(input()))
#
#
# n=5
# s='Hello every one'
# a= lambda s : s[-1:-(n)]
# print(str(a))




# s='hello'
# if len(s)%2==0:
#     print(len(s) **2)
# else:
#     print(len(s)**3)



# s='Hello'
# a=[len(s)**2 if len(s)%2==0 else len(s)**3]
# print(a)


#
# a=lambda s : len(s)**2 if len(s)%2==0 else len(s)**3
# print(a('Hello'))