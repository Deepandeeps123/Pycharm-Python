# dictionary
'''
s='hello'


  o/p---------> H E L L O



s='heLlO'
dic={}
for i in range(len(s)):
    key=s[i]
    value=s[i].swapcase()
    dic[key]=value
print(dic)


{'h': 'H', 'e': 'E', 'L': 'l', 'l': 'L', 'O': 'o'}




                             or


s='heLlO'
dic={}
for i in s:
    if i.isupper():
        dic[i]=i.lower()
    else:
        dic[i]=i.upper()
print(dic)





      while loop,,,,,,,,,,,




s='heLlO'
dic={}
i=0
while i<len(s):
    rem=s[i].swapcase()
    key=s[i]
    i+=1
    value=rem
    dic[key]=value
print(dic)





2...count how many alphabet in given string


s='deepanvinayagam1411@gmail.com'
count=0
for i in s:
    if i.isalpha():
        count+=1
print(count)



          while loop   (incorrect)



s='deepanvinayagam1411@gmail.com'
i=0
rem=0
sum=0
while i<len(s):
    if s[i].isalpha():
        a=s[i]
        i+=1
        sum=sum+len(a)
        print(sum)





find count in number in program


s='deepanvinayagam1411@gmail.com'
count=0
for i in s:
    if i.isdigit():
        count+=1
print(count)




'''

'''
s='deepanvinayagam1411@gmail.com'
s1=''
s2=len(s1)
i=0
sum=0
while i<len(s):
    rem=s[i]
    if s[i].isdigit():
        s1=s[i]
    i+=1
print(len(s1))



'''
'''
find the count of special character in given string


s='deepanvinayagam1411@gmail.com'
count=0
for i in s:
    if i.isalnum()==False:
        count+=1
print(count)






s='deepanvinayagam1411@gmail.com'
count=0
for i in s:
    if i in '!@#$%^&*()_+.`':
     count+=1
print(count)


    interview question
    
    
    


s='String123World'
s1=123

for i in s:
    if i in '123':
        print(i,end='')





4..........dictionary price is even add 10 rs   and odd add  15 rs



a={'apple':1000,'bannana':1231,'orange':2340,'graphes':3207}
dic={}
for i,j in a.items():
    if j %2==0:
        value=j+10
    else:
        value=j+15
    key=i
    dic[i]=value
print(dic)





remove duplicate



lst=[1,2,3,4,1,2,3,1,2,3,4,5,6]
a=set(lst)
b=list(a)
print(b)



'''

#
# dic=input()
# dic1={}
# for i in dic:
#     key=i
#     value=0
#     dic1[key]=value
# print(dic1)







