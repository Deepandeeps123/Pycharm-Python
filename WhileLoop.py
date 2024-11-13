                                          #Syntax
                                # while Condition      #loop (mantatory)
                                        #Statement
                                        #upadtion     (increment,decrement)


#while
'''

a = int(input('Enter:'))
while a > 10:
    print('Correct')
    
    
output:
>>>




a = int(input('Enter:'))
while a < 10:
    print('Correct')
    a+=1


output

Enter:1
Correct
Correct
Correct
Correct
Correct
Correct
Correct
Correct
Correct




i =1
if i < 6:
    print('Hello')
    i+=1


i = 5
if i <=5:
    print('hello\n' * 5)


i=1
while i<6:
    print('Hello Python')
    i+=1
    
    
Hello Python
Hello Python
Hello Python
Hello Python
Hello Python
    


#print 1 to 5 number
i = 1
while i <=5:
    print(f'{i}')
    i+=1
    

1
2
3
4
5





i = int(input('Enter:'))
while i < 6:
    print(i)
    i+=1


Enter:4
4
5





i = 10
while i > 0:
    print(i)
    i-=1

10
9
8
7
6
5
4
3
2
1




#print 1 to 10
i =1
while i <=10:
    print(i)
    i+=1





# print 1 t0 n number:

i = 1
n =int(input('Enter:'))
while i <= n:
    print(i)
    i+=1





  # print n to 1 number revrese:
        # normal Method

i = 10
while i >= 1:
    print(i)
    i-=1





      # user input

i = 10
n =int(input('Enter'))
while i >= n:
    print(i)
    i-=1



Enter1
10
9
8
7
6
5
4
3
2
1






   # wap 1 to 10 even number

i = 1
while i <=10:
    if i % 2 == 0:
        print(i)
    i+=1



2
4
6
8
10






   # 1 to n number even number

i = 1
n = int(input('enter:'))
while i <= n:
    if i %2==0:
        print(i)
    i+=1





   # 10 to 1 number even number

i = 10
while i >= 1:
    if i % 2==0:
        print(i)
    i-=1

    10
    8
    6
    4
    2







   # n to n check even number in reverse order:

i = int(input('enter:'))
n = int(input('enter:'))
while i >=n:
    if i % 2==0:
        print(i)
    i-=1


enter:10
enter:1
10
8
6
4
2







   # 1 to n odd number

i =1
n = int(input('Enter:'))
while i <=n:
    if i % 2 ==1:
        print(i)
    i+=1
    
Enter:10
1
3
5
7
9






   # print n to n odd number


i = int(input('Enter:'))
n = int(input('Enter:'))
while i <=n:
    if i % 2 == 1:
        print(i)
    i +=1
    
    




  # wap traverse a string

s= 'hello'
print(s)




s='hello'  
i =0
while i < len(s):
    print(s[i],end='')
    i+=1




    # reverse order:

s ='hello'
i = -1
while i >= len(s):
    print(s[i])
    i-=1


no output







s ='hello'
i = 1
while i <=len(s):
    print(s[-i])
    i+=1
    
    
o
l
l
e
h







s='hello'
i =len(s)-1
while i >=0:
    print(s[i])
    i-=1





s='hello'
i=1
while i <=len(s):
    print(s[i])
    i+=1




error






a = input('Enter:')
res=''
i=1
while i<=len(a):
    res=res+a[-i]
    i+=1
if a == res:
    print('Palindrome')
else:
    print('Not')




a = input('Enter:')
if a==a[::-1]:
    print('Palindrome')
else:
    print('Not')





i = 42
while i>=7:
    print(i)
    i-=7



a=str(123)
print(len(a))




                      # 1.Print  to check 100 and 300 both divide by 3 and 5:
i =100
while i <=300:
    if i % 3 ==0 and i%5==0:
        print(i,end=' ')
    else:
        print('',end='')
    i+=1



a=int(input())
b = str(a)

if b == b[::-1]:
    print('palindrome')
else:
    print('Not')






               # To print using while loop


 #1. (i)  First 10 even number

i=1
while i <=10:
    if i%2==0:
     print(i)
    i+=1




   # (ii)   First 10 odd number

i=0
while i <=10:
    if i%2==1:
        print(i)
    i+=1
    
    



     # (iii) First  10 Natural Number

i=1
while i<=10:
    print(i)
    i+=1





      # (iv)  First 10 whole Number

i=0
while i<=10:
    print(i)
    i+=1






          #2.First 10 integer and their square
i=1
while i<=10:
    print(i,'-',i**2)
    i+=1



       #3.Print Tables

i =1
n = int(input('Enter:'))
while i<=10:
    print(i,'*',n,'=',i*n)
    i+=1







      #4.Print 10,20,30,,,,,,100 following Series


i = 10

while (i <=100):
        print(i,end=', ')
        i+=10






    #5.Write a while loop in 105,98,91,..........7 following statement


i = 105
while i>=7:
    print(i,end=', ')
    i-=7



# user input

i = int(input('Enter:'))
n = int(input('enter:'))
while i>=n:
    print(i,end=', ')
    i-=n









           # 6.First 10 Natural Number Reverse order

i=10
while i>=1:
    print(i)
    i-=1









         #7.Sum of 10 natural Number print while loop


i=1
sum=0

while i<=10:
     sum = sum+i
     i+=1
     print(sum)

    # sum+=i
    # i+= 1
    # print('print',sum)


# 1+2+3+4+5+6+7+8+9+10 = 55




        # 8.print sum of first 10 even number



i=2
sum=0
while i<=20:
    sum=sum+i
    i+=2








#string

s='python'
i=0
while i<len(s):
    print(s[i])
    i+=1




#List

s=['python']
s1=str(s)
i=0
while i <len(s1):
    print(s1[i])
    i+=1


#set


s={'python'}
i=0
while i<len(s):
    print(s[i])
    i+=1





#tuple



s=('python')
i=0
while i<len(s):
    print(s[i])
    i+=1







i = int(input('Enter:')) #variable name
n=int(input('Enter:'))
while i<n:
    print('Correct')
    i+=1

    Enter: 1
    Enter: 10
    Correct
    Correct
    Correct
    Correct
    Correct
    Correct
    Correct
    Correct
    Correct









print('hello\n'*5)




hello
hello
hello
hello
hello





a='hello'
i=1
while i <=5:
    print(a)
    i+=1

    hello
    hello
    hello
    hello
    hello






a=1
res=0
while a<6:
    res=res+a
    a+=1
print(res)


                 #10





a=1
while a<6:
    print(a)
    a+=1




1
2
3
4
5







         #10 to 1

a=10
while a>0:
    print(a)
    a-=1


10
9
8
7
6
5
4
3
2
1






a=1
n=int(input('Enter:'))
while a <=n:
    print(a)
    a+=1
    
    
    
    




         #1to 40 even number and odd number

a=1
while a<=40:
    if a%2==0:
         print(a,end='  ')
    # else:
    #      print(a,end='  ')
    a+=1






2  4  6  8  10  12  14  16  18  20  22  24  26  28  30  32  34  36  38  40








           #1 to 40 odd number


i=1
while i<=40:
    if i%2==1:
        print(i,end='  ')
    i+=1




2  4  6  8  10  12  14  16  18  20  22  24  26  28  30  32  34  36  38  40









         #12345
         #54321

i=1
while i<=5:
    print(i,end='')
    i+=1              #12345



i=5
while i>=1:
    print(i,end='')
    i-=1             #54321









           #string while loop                      #error-----------------------------------------------------

a='hello'
b=int(a)
c=int(len(a))                   #error
while b<=c:
    print(a)
    a+=1







a='hello'
i=0
while i<len(a):
    print(a[i])
    i+=1

# a=1
# while i<=6:
#     print(i)
#     i+=1







a=input('Enter:')
i=0
while i <len(a):
    print(a)
    i+=1




Enter:python
python
python
python
python
python
python








###python reverse


a=input('Enter:')
i=1
while i<=len(a):
    print(a[::-1])
    i+=1





Enter:python
nohtyp
nohtyp
nohtyp
nohtyp
nohtyp
nohtyp







a=input('Enter:')
i=0
while i<len(a):
    print(a[i].upper())
    i+=1






Enter:python
P
Y
T
H
O
N







a='PyThOn'
i=0
while i<len(a):
    print(a[i].swapcase())
    i+=1








a='Python'
i=0
while i<len(a):
    print(a[i],end=' ')
    i+=1


P y t h o n 






a='Python'
i=0
while i<len(a):
    print(a[i],end=' ')
    i+=1





Python Python Python Python Python Python






a='hello world'
i=0
while i<len(a):
    print(a[::-1])
    i+=1

    dlrow olleh
    dlrow olleh
    dlrow olleh
    dlrow olleh
    dlrow olleh
    dlrow olleh
    dlrow olleh
    dlrow olleh
    dlrow olleh
    dlrow olleh
    dlrow olleh




    a = 'hello world'
    i = 0
    while i < len(a):
        print(a[::-1])
        i += len(a)



dlrow olleh





                   #if condition to check palindrome or not    

a='racecar'
if a == a[::-1]:
    print('Palindrome')
else:
    print('Not')

 
 
 
 
 
Palindrome








        #to check palindrome or not using while condition


a=input('Enter:')
res=''
i=1
while i<=len(a):
    res=res+a[-i]
    i+=1
if a==res:
    print('Palindrome')
else:
    print('Not')





Enter:racecar
Palindrome









                                          #number

   #      reverse method
a=121
b=str(a)
c=int(b)
d=b[::-1]
print(d)







121







                        #while loop



a=input('Enter:')
res=''
i=1
while i<=len(a):
    res=res+a[-i]
    i+=1
print(res)







a=1234
res=0
i=0
while a>0:
    rem=a%10
    res=res*10+rem
    a=a//10
print(res)










#                          Easy method ===================================================================


a=1234
b=str(a)
c=b[::-1]
d=int(c)
print(c)









a=1234
res=0
i=0
while a>0:
    rem=a%10
    res=res*10+rem
    a=a//10
print(res)








#  find palindrome or not---------------------------------------

a=int(input('Enter:'))
num=a
res=0
i=0
while a>0:
    rem=a%10
    res=res*10+rem
    a=a//10
print(res,num)
if num==res:
    print('Palindrome')
else:
    print('Not')








      #sum of the number


a=1234                  #10
res=0
i=0
while a>0:

    rem=a%10
    res=res+rem
    a=a//10
print(res)






a=87654321          #36
res=0
i=0
while a>0:
    rem=a%10
    res=res+rem
    a=a//10
print(res)





                                          #1*2*3*4*5 ====== 120


a=6
res=1
while a>0:
    res=res*a
    a-=1
print(res)



720







                #Find the sum of even number


a=123456
res=0
i=0
while a>0:
    rem=a%10
    if rem%2==0:
      res=res+rem
      a=a//10
print(res)





a=145
res=1
while a>0:
    rem=a%10
    num=rem
    res=res*num
    # result=rem
    # res=res*result
    # result1=res
    a=a//10s
print(res)







a=int(input())
b=int(input())
c=a+b
print(c)


'''





num=6
res=1
i=1
while i<=num:
    res=res*i
    i+=1
print(res)