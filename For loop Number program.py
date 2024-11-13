'''

     # reverse

# a=1234
# b=str(a)
# for i in range((len(b)),0,-1):
#     print(b[i-1],end='')







a=12321
b=a
c=str(b)
sum=0
for i in range(1,len(c)):
    sum=sum*10+1
print(sum)
    # print(c[i],end='')


lst=[13,9,25,30,23]             #13,fizz,buzz,fizz buzz,23
a=[]
b=[]
for i in lst:
    if i%3 ==0 and i%5==0:
        a.append('fizz buzz')
    elif i%3==0:
        a.append('fizz')
    elif i%5==0:
        a.append('buzz')
    else:
        a.append(i)
print(a)




'''
