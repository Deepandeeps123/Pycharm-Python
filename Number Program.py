'''
1.Number Reverse Program without Typecasting

#1.Number Reverse
      #1234    #4321
a=1234
b=4321
sum=0
while a>0:                  #variable_name,Updation   is important
     rem=a%10
     sum=sum*10+rem                  #sum*10    impoetant
     a=a//10
print(b)
print(sum)
if b==sum:
    print('Reverse Number')
else:
    print('Not Reverse Number')





#2.Palindrome Number


a=123321                                  #1224568076433257646                                 #123456789                     #14541
b=a
sum=0
i=0
while a>0:
    rem=a%10
    sum=sum*10+rem
    a=a//10
print(b)
print(sum)
if b==sum:
    print('Palindrome')
else:
    print('Not a Palindrome')







#3.Factorial Number                       #5--------5*4*3*2*1======120

a=10
sum=1
while a>0:
    sum=sum*a
    a=a-1
print(sum)








#4.Fabanacci Series        0 1 1 2 3 5 8 13 21 34


#output
# 13 21 34 55 89 . . . . .

a=0                #int(input('a--'))
b=1               #int(input('b--'))
# print(a,b,end=' ')
sum=0
#print(a,b,end=' ')
while a<=100:
    c=a+b
    a=b
    b=c
    print(a,b,end=' ')
    print(c,end=' ')







                            #  (or) based on count
a=0
b=1
count=1
print(a,b,end=' ')
while count<=8: #a,b is present
     c=a+b
     a=b
     b=c
     print(c, end=' ')
     count+=1











 # 5....Perfect Number
 #28-----------------28 half 14     14--------only divided by 28--------[1,2,3,4,7,14]===14+14===28


a=28
b=a
a1=a//2        #14
sum=0
i=1
while i<=a1:
    if a%i==0:
        sum=sum+i
    i+=1
print(sum)
if b==sum:
    print('Perfect Number')
else:
    print('Not Perfect Number')











#    6.....Perfect Square number

# root of 25   is ----------- 5    is equal to        5*5=25       but output is only integer


a=39
b=a**0.5
c=b//1
if b==c:
    print('Perfect Square')
else:
    print('Not a Perfect Square')









# 7...sum of the number
           #1+2+3+4+5+6+7+8+9+10=55


a=10
sum=0
i=1
while i<=a:
    sum=sum+i
    i+=1
print(sum)



               (or)         123456789========45


a=123456789
sum=0
i=0
while a>0:
    rem=a%10
    sum=sum+rem
    a=a//10
print(sum)










#    8....Strong number

          #input   ----145   =====>  1   4   5    and    1!   4!   5!    ======>1+16+125=====>145---(output)




   #654





a=145
sum=0
i=0             #multiple
while a>0:
    rem=a%10
    fact=1
    while rem>0:
        fact=fact*rem
        rem-=1
    sum=sum+fact
    a=a//10
print(sum)









#       9........harshad Number
             #124------------1+2+4=====7   --------->   124/7==0


a=278
a1=a
sum=0
i=0
while a>0:
    rem=a%10
    sum=sum+rem
    a=a//10
if a1%sum==0:
    print('Harshad Number')
else:
    print('Not a Harshad Number')















    #10.Amstrong Number

           #input   370  ----length 3   ----> 3   7   0     3(3)-----> 27   7(7)-------> 243    0(0)------>    243+27========>370






a=370
b=a
c=str(b)
d=len(c)
sum=0
i=0
while a>i:
    rem=a%10
    sum=sum+rem**d
    a=a//10
if b==sum:
    print('Amstrong Number')
else:
    print('Not a Amstrong Number')










      #11 ....Xylem  and Pholem    Number


      #input 1234        #first and last  add-----> 1+4====> 5        &&&&&      middle  number add====> 2+3 =======> 5       (5==5)


a=int(input('Enter:'))                                        #1234
a1=a
o_sum=0
i_sum=0
i=0
while a>0:
    rem=a%10
    if a==a1 or a<10:
        o_sum=o_sum+rem
    else:
        i_sum=i_sum+rem
    a=a//10
if o_sum==i_sum:
    print('Xylem Number')
else:
    print('Pholem Number')












           #12..............Prime Number

            #input----------13           divisible by 1 and 13 ======>   prime number





=23
i=2
while a>0:
    if a%i==0:
        print('Not a prime ')
        break
        a+=1
    else:
        print('prime')












a=23
i=2
res=True
while a>0:
    if a%i==0:
        res=False
    a+=1
    break
if res==True:
    print('Prime Number')
else:
    print('Not a Prime Number')










a=7
i=2
while i<a:
    if a%i==0:
        print('Not a Prime Number')
        break
    i+=1
else:
    print('Prime Number')





'''