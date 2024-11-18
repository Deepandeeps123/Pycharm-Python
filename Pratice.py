# print    traverse program



'''
s='hello'
i=0
while i<len(s):
    res=s[i]
    i+=1
    print(res)

      output
   h
   e
   l
   l
   o






# print traverse reverse order


a=input('Enter:')
i=1
while i<=len(a):
    res=a[-i]
    i+=1
    print(res)



o
l
l
e
h







   # print traverse in straint line


a=input('Enter:')
i=0
while i<len(a):
    res=a[i]
    print(res,end=' - ')
    i+=1





Enter:Python
P - y - t - h - o - n -








a=input('Enter:')
i=1
while i<=len(a):
    res=a[-i]
    i+=1
    print(res,end=' - ')



Enter:Python
n - o - h - t - y - P -







     # print the traverse if is palindrome or not


a=input('E:')
res=''
i=1
while i<=len(a):
    res=res+a[-i]
    i+=1
if a==res:
    print('Palindrome')
else:
    print('Not')






         # sum of given number
a=123       #6
res=0
i=0
while a>i:
    rem=a%10
    res=res+rem
    a=a//10
print(res)






    # sum of user given number


a=int(input('E:'))
res=0
i=0
while a>i:
    rem=a%10
    res=res+rem
    a=a//10
print(res)





E:12345678
36







     #multiple of user input


a=int(input('E:'))
res=1
i=0
while a>0:
    rem=a%10
    res=res*rem
    a=a//10
print(res)



E:12345
120







     #print the reverese the number------------------------

a=1234
a1=a
res=0
i=1
while i<=a:
    rem=a%10
    res=res*10+rem
    a=a//10
print(res)





4321





     #reverse the number to check palindrome or not


a=int(input('E'))
a1=a
res=0
i=0
while i<a:
    rem=a%10
    res=res*10+rem
    a=a//10
if a1==res:
    print('Palindrome')
else:
    print('Not')




    E:121
    Palindrome






num=145
no=num
sum=0
while num>0:
    temp=num%10
    fact=1
    while temp>0:
        fact=fact*temp
        temp-=1
    sum=sum+fact
    num=num//10
if no==num:
    print('Strong')
else:
    print('Not')\





#find the perfect number or not



a=6
sum=0
i=1
while i<6:
    if a%i==0:
        sum=sum+i
    i+=1
if a==sum:
    print('Prefect')
else:
    print('Not')









a=36
b=a**0.5
c=int(b)
d=c*c
if a==d:
    print('Prefect Square')
else:
    print('Not')










a=0
b=1
print(a,b,end=' ')
while a<20:
    c=a+b
    print(c,end=' ')
    a=b
    b=c







a=0
b=1
count=1
print(a,b,end=' ')
while count<=18:
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    count+=1



0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181







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






    #  3 in 1 program-------------------------------------------------------------------------------------------------------




a=int(input('Enter:'))
a1=a
sum=0
sum1=0
i=1
while i<a:
    if a%i==0:
        sum=sum+i
    i+=1
if a1 == sum:
    print('Prefect')
    num=sum
    res=1
    i1=1
    while i1<=num:
        res=res*i1
        i1-=1
    print(res)

else:
    a = 145
    a2 = a
    sum1 = 0
    while 0 < a:
        temp = a % 10
        fact = 1
        while temp > 0:
            fact = fact * temp
            temp -= 1
        sum1 = sum1 + fact
        a = a // 10
    if a2 == sum1:
        print('Strong Number')
    # a2=a
    # a1=0
    # sum2=0
    # while a>0:
    #     temp=a%10
    #     fact=1
    #     while temp>0:
    #         fact=fact*temp
    #         temp-=1
    #     sum2=sum2+fact
    #     a=a//10
    # if a1 == sum2:
    #     print('Strong Number')
    else:

        print('Not')
# else:
#     a1=0
#     a2=a
#     while 0<a:
#         temp=a%10
#         fact=1
#         while temp>0:
#             fact=fact*temp
#             temp-=1
#         sum1 =sum1+fact
#     a=a//10
# if a2==sum1:
#         print('Yes')
# else:
#         print('Not')









                       #Find Strong Number-------------------------------------------------------------------------------------


a=145
a1=a
sum=0

while a>0:
    temp=a%10
    fact=1
    while temp>0:

        fact=fact*temp
        temp-=1
    sum+=fact
    a=a//10
if a1==sum:
    print('Yes')
else:
    print('No')






num=145
no=num
sum=0
while num>0:
      temp=num%10
      fact=1
      while temp>0:
          fact=fact*temp
          temp-=1
      sum=sum+fact
      num=num//10
if no==sum:
    print('Yes')
else:
    print('No')








print('Skill'+'Rank')






a=int(input('Enter:'))
a1=a
sum=0
i=0
while a>0:
    temp=a%10
    fact=1
    while temp>0:
        fact=fact*temp
        temp-=1
    sum=sum+fact
    a=a//10
if a1==sum:
    print('Strong')
else:
    print('Not')









a=int(input('Enter'))
a1=a
sum=0
b=str(a)
count=len(b)
                                    #    print(count)
while a>0:
    temp=a%10
    fact=1
    fact=temp**count
    # while temp>0:
    #     fact=temp
    sum=sum+fact
    a=a//10
if a1==sum:
    print('Amystrong')
else:
    print('Not')





a=1634
a1=a
sum=0
a2=str(a)
count=len(a2)
i=0
while a>0:
    temp=a%10
    fact=1
    fact=temp**count
    sum=sum+fact
    a=a//10
if a1==sum:
    print('Amstrong number')
else:
    print('Not Amstrong Number')
print(sum)









           # Find the happy number or not




a=23
a1=a
while a>9:
    sum=0
    while a>0:
        rem=a%10
        sum=rem**2
        a=a//10
    a=sum
if a==1:
    print('Happy Number')
else:
    print('Not')










a=26
while a>9:
    sum=0
    while a>0:
        temp=a%10
        sum=temp**2
        a=a//10
    a=sum
    print(sum)
       #sum=1         sum name(value) to change to n
if a==1:
    print('Happy Number')
else:
    print('Not')









a=1234
i=0
while a>0:
    temp=a%10
    sum=0
    sum=sum+temp
    print(sum)
    break











                   #automorphic number
                   #1...n=5
                   #n*n ========> 25 ---------------end with 5 is a automorphic
                   #2......n=25
                   #n*n==============>625-----------------end with 25


a=int(input())
t=10
while a>0:
    temp=a**2
    sum=0
    while temp>0:
        rem=temp%10
        print(rem)
        break
    a=a//10
    t=t*10
print(sum)












              #xylem and phleom program--------------------------------------
              #1234            1....  1+4=5    2.....  2+3=5       1==2
a=1234
a1=a
o_sum=0
i_sum=0
while a>0:
    rem=a%10
    if a==a1 or a<10:
        o_sum=o_sum+rem
    else:
        i_sum=i_sum+rem
    a=a//10
if i_sum==o_sum:
    print('Xylem Number')
else:
    print('Phalem Number')










a=11#int(input('Enter:'))
a1=a
o_sum=0
i_sum=0
while a>0:
    rem=a%10
    if a==a1 or a<10:
        o_sum=o_sum+rem
    else:
        i_sum=i_sum+rem
    a=a//10
if i_sum==o_sum:
    print('Xylem Number')
else:
    print('Phelem Number')



# Enter:12345
# Phelem Number















                          #prime Number


    #7      1 and 7 not divible


a=7
i=2
while i<a:
    if a%i==0:
        print('not Prime Number')
        break
        i+=1
else:
    print('Prime Number')





#
# lst = {'name':'dinga','sal':200 }
#    #o/p-------------->dinga,200
# #              print(lst.values())
# a=dict.values()
# i=0
# while i<len(lst):
#     print(lst(a)[i])
#     i+=1





lst=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(lst):
    print(lst[i])
    i+=1












lst=[1,2,3,4,5,6,7,8,9,10]
i=0
a=[]
while i<len(lst):
    a.append(lst[i])
    # print(lst[i],end=' ')
    i+=1
print(a)



























lst=[1,2,3,4,5,6,7,8,9,10]
i=0
a=[]
while i<len(lst):
    if lst[i]%2==0:
        a.append(lst[i])
    i+=1
print(a)












lst=['apple','bannan','orange','grapes']
a=[]
i=0
while i<len(lst):
    if lst[i][0] in 'AEIOUaeiou':
        a.append(lst[i])
    else:
        a.append(lst[i][::-1])
    i+=1
print(a)












lst=['apple','mango','orange','bannana','neem']
dic={}
i=0
while i<len(lst):
    key=lst[i]
    values=i
    dic[key]=values
    i+=1
print(dic)










lst=['Dhoni','Rohit','Virat','Raina','Samson','Ashwin']
dic={}
i=0
while i<len(lst):
    key=lst[i]
    value=i+1
    dic[key]=value
    i+=1
print(dic)







a=12345
i=0
while a>0:
    if a%10==0:
        break
print(a//10)










lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    a=2
    while a<i:
       if i%a==0:
        break
       a+=1
else:
     print(i)




'''
'''



# lst=[1,2,3,4,5]
# a='int'
# for i in lst:
#     b=(str(type(i))[8:-2])
#     # print(b)
#     break
# if b==a:
#     print('Homo')
# else:
#     print('Not Homo')


# lst=[1,1.2,True,2+3j,'Hello']
# for i in lst:
#    print(str(type(i))[8:-2])
#    print(lst[i])
#
lst=[1,2,3,4,5]
lst1=[]
sum=0
for i in lst:
   sum=sum+i
print(sum)










lst=['apple','bannana','orage','mango','grapes','tarmind']
dic={}
for i in range(len(lst)):
   if i==0:
      key=lst[i]
      value=i
      dic[key]=value
   elif i%2==0:
      key=lst[i]
      value=lst[i][::-1]
      dic[key]=value
   else:
      key=lst[i]
      value=len(lst[i])
      dic[key]=value
print(dic)








n=31
i=0
count=2
sum=0
sum1=0
fact=0
fact1=0
while n>i:
    rem=n%10
    sum=rem**count
    fact=fact+sum
    n=n//10
while fact>9:
    rem1=fact%10
    sum1=rem1**count
    fact1=fact1+sum1
    fact=fact//10
if fact1==1:
    print('Happy Number')
else:
    print('not')






def add():
    for i in range(1,1001):
        if i%2!=0 and i%3==0 and i%5==0:
            yield i
print(list(add()))





lst=['apple','mango','bannana','neem','tarmiand']
dic={}
for i,j in enumerate(lst):
    if i%2==0:
        key=lst[i][len[:lst[i]//2]]
        value=lst[i][len[lst[i]//2:]]
        dic[key]=value
print(dic)




a=7
i=2
res=True
if a%i==0:
    res=False
    i+=1
if res==True:
    print('P')


lst=[2,10]
a=min(lst)
b=max(lst)
for i in range(a,b+1):
    res=True
    for j in range(2,10):
        if i%j==0:
            res=False
            break
    if res:
        print(i)

'''


# a=10
# print(f'{a}')



# a='Input'
# print(a)
# a=10,20
# print(a)
# print(10,20,sep='@')


# a=10
# b=20
# print(a,b,sep='@',end=' ')
# print(a+b)
# if 10%2==0:
#     print('Even')

# if 9%2==0:
#     print('Even')
# else:
#     print('odd')

# print(ord('d'))

# print(ord('a')-ord('A'))
# print(ord('a')+32)
# if 'a' in 'aeiou':
# #     print('Yes')
#
# a=2024
# if a%4==0 or a%100!=0 and a%400==0:
#     print('Leap year')
# else:
#     print('Leap year')

# a=30
# if a%3==0:
#     print('Fizzz')
# elif a%5==0:
#     print('buzz')
# elif a%5==0 and a%3==0:
#     print('fizzbuzz')

# a=10
# if a>0:
#     if a%2==0:
#         print('Yes')
#     else:
#         print('No')
# else:
#     print('Invalid')

# a=1
# while a<6:
#     print('Hello')
#     a+=1


#
# a='1234'
# print(a[::-1])


# 4321


#
# a=1234
# i=0
# sum=0
# while a>0:
#     rem=a%10
#     sum=sum*10+rem
#     a=a//10
# print(sum)

# a='racecar'
# print(a[::-1])


# a=12321
# res=0
# b=a
# i=0
# while a>0:
#     rem=a%10
#     res=res*10+rem
#     a=a//10
# if b==res:
#     print('Palindrome')
# else:
#     print('Not a Plaindrome')



#
# a=12345
# sum=0
# i=0
# while a>0:
#     rem=a%10
#     print(rem,end=' ')
#     sum=sum+rem
#     a=a//10
# print(sum)

#
#
# a=5
# res=1
# while a>0:
#     res=res*a
#     a=a-1
# print(res)



#
#
# a=10
# res=1
# while a>0:
#     res=res*a
#     a=a-1
# print(res)




# a=12345678
# i=0
# while a>0:
#     rem=a%10
#     if rem%2==0:
#         print(rem)
#     a=a//10



# a=12345678
# i=0
# sum=0
# while a>0:
#     rem=a%10
#     if rem%2==0:
#         sum=sum+rem
#     a=a//10
#
# print(sum)
#
#
#
# a='hello'
# print(a[::-1])


#
#
# a='Hello'
# res=' '
# i=1
# while i<=len(a):
#     res=res+a[-i]
#     i+=1
# print(res)



# #145
# a=145
# b=a
# i=0
# sum=0
# while a>0:
#     rem=a%10
#     fact = 1
#     while rem>0:
#
#         fact=fact*rem
#         rem=rem-1
#     sum=sum+fact
#     a=a//10
# print(sum)


# a=6
# i=1
# sum=0
# while a>=0:
#     if a%2==0:
#         sum=sum+a
#     i=i+1
# print(sum)

#
#
# a=25
# b=a**0.5
# c=int(b)
# d=c*c
# if a==d:
#     print('Perfect')
# else:
#     print('Not')


# a=0
# b=1
# print(a,b,end=' ')
# while a<=20:
#     c=a+b
#     print(c,end=' ')
#     a=b
#     b=c
#
#
# a=153
# i=0
# sum=0
# res=0
# b=str(a)
# c=len(b)
# while a>0:
#     rem=a%10
#     res=a**c
# sum=sum+res
# a=a//10
# print(sum)




# n=10
# while n>0:
#     sum=0
#     a=n%10
#     sum=sum**2
#     n=n//10
#     n=sum
# if n==1:
#     print('Happy')
# else:
#     print('Not')


# 6532.0

# n=6
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0:
#             print('*0',end=' ')
#         else:
#             print(' ',end=' ')
#     print(' ')