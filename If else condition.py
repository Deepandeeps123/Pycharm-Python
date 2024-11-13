        #if else condition

'''
a=int(input('Enter:'))
if a % 2 == 0:
    print('Even')
else:
    print('Odd')



a=int(input('Enter:'))
if a > 0 :
    print('Hello')
else:
    print('Bye')



a=int(input('Enter:'))
if a > 0 :
    print('Positive')
else:
    print('Negative')



ch = input('Enter:')
if ch.isupper():
    print('Uppercase')
else:
    print('Lowercase')

'''

    

'''
ch = input('Enter:')
if ch:
    print(ch.upper())


a= input('Enter:')
if a.isupper():
    print(a.lower())
else:
    print(a.upper())
    
    


     ###### ascii    value



a=input('Enter')
if ord(a) >= 97 and ord(a) <=122:
    print(chr(ord(a)-32))
else:
    print(chr(ord(a) + 32))
    
    
    


#assignment


num1=int(input('Enter:'))
num2=int(input('Enter:'))
if num1%2 == 0 and num2%2==0:
    print('Square')
else:
    print('Cube')
    

age=int(input('Enter:'))
if age >=18:
    print('You Are Eligible')
else:
    print('Not Eligible')
    


a=int(input('Enter:'))
if a>=0 :
    print('Hi')
else:
    print('Bye')



a= input('Enter:')
if a.upper():
    print('Lower')
else:
    print('Vice Versa')
    


a=input()
if (ord(a)%2==0):
    print(chr('Even'))
else:
    print(chr('not'))
    

ch = input('enter:')
if ord(ch)>=31 and ord(ch)<=57:
    print('Special character')
else:
    print('Not')



#   Harshad Number



a=124
a1=a
sum=0
i=0
while a>i:
    rem=a%10
    sum=sum+rem
    a=a//10
print(sum)
if a1%sum==0:
    print('harshad Number')
else:
    print('No')


'''



a=145
a2=a
sum1=0
while 0<a:
    temp=a%10
    fact=1
    while temp>0:
        fact=fact*temp
        temp-=1
    sum1 =sum1+fact
    a=a//10
if a2==sum1:
    print(sum1)
    print('Yes')
else:
        print('Not')