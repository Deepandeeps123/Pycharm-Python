'''
1. Number rerverse



a=123456789
i=0
sum=0
while a>i:
    rem=a%10
    sum=sum*10+rem
    a=a//10
print(sum)
# if a == sum(:
#     print('It is reverse')
# else:
#     print('Not')










2..........Number palindrome



a=98766789
b=a
i=0
sum=0
while a>i:
    rem=a%10
    sum=sum*10+rem
    a=a//10
print(sum)
if b==sum:
    print('Palindrome')
else:
    print('Not Palindrome')








3....fabinnocii series




# a=0
# b=1
# count=1
# print(a,b,end=' ')
# # first 20 number
# while count<=18:
#     c=a+b
#     print(c,end=' ')
#     a=b
#     b=c
#     count+=1





a=0
b=1
print(a,b,end=' ')
count=1
while count<=13:
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    count+=1






4.  factorial Number



a=10
i=0
sum=1
while a>0:
    sum=sum*a
    a-=1
print(sum)




5.Perfect Number




a=28
b=a
sum=0
i=1
while i<=a//2:
    if a%i==0:
        sum=sum+i
    i+=1
if b==sum:
    print('Perfect Number')
else:
    print('Not a Perfect Number')




6........Perfect square




#36

a=49
b=a
c=b**0.5
d=int(c)
e=d*d
if b==e:
    print('Perfect Square')
else:
    print('Not a Perfect Square')







7........sum of the number

         #10-------> 10+9+8+7+6+5+4+3+2+1=================>   55






a=10
sum=0
i=0
while a>i:
    sum=sum+a
    a-=1
print(sum)








8......Strong Number

          #145------------>   1     4      5      -------------->      1+24+120





a=145
b=a
i=0
sum=0
while i<a:
    rem=a%10
    fact=1
    while rem>0:
        fact=fact*rem
        rem=rem-1
    sum=sum+fact
    a=a//10
if b==sum:
    print('Perfect Square')
else:
    print('Not a Perfect Square')





9..........Amstrong Number

       153------> len---> 3   ---------->   1    5    3  -------->    1^3    5^3    3^3------->  1    125      27  ---------------> 153





a=156
b=a
c=str(a)
d=len(c)
sum=0
i=0
while a>i:
    rem=a%10
    fact=1
    fact=rem**d
    sum=sum+fact
    a=a//10
if b==sum:
    print('Amstrong number')
else:
    print('Not a amstrong number')




10........Harshad Number


#   124              1     2      4   -------------->    7               124  %  7 ====>  0


a=171
b=a
sum=0
i=0
while a>i:
    rem=a%10
    sum=sum+rem
    a=a//10
print(sum)
if b%sum==0:
    print('Harshad Number')
else:
    print('Not a Harshad Number')






11......xylem and pholem



1234---------->1     4   =====>   5      2      3 ======>   5



a=1234
b=a
o_sum=0
i_sum=0
sum=0
i=0
while a>i:
    rem=a%10
    if a==b or a<10:
        o_sum=o_sum+rem
    else:
        i_sum=i_sum+rem
    a=a//10
if o_sum==i_sum:
    print('Xylem ')
else:
    print('Pholem')





12...............Prime number
'''

