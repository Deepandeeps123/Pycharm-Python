                       # For Loop
''''                       
                       
                           Syntax
                           
                           
                    for (variable name)   in     collection /  range :
                                  statement


'''







'''

1...print 1 to 5 number




for i in range(1,6):
    print(i)





lst=[1,2,3,4,5]
for i in range(1,10):
    print(i)








lst=[1,2,3,4,5]
for i in lst:
    print(i)





2.print 5 to 1 number for loop





for i in range(10,0,-1):
    print(i,end=' ')



i=10
while i>0:
    print(i,end=' ')
    i-=1







3.....wap to print 10 in 1 number






for i in range(10,0,-1):
    print(i)




for i in range(10,0,-1):
    print(i,end=' ')




i=10
while i>0:
    print(i,end=' ')
    i-=1






4.......Traverse through a string



s='hello'
i=0
while i<len(s):
    print(s[i])
    i+=1


                              or



s='hello'
for i in range(0,len(s)):
    print(s[i])




5....traverse through a list





lst=['apple','mango','orange','grapes']
i=0
while i<len(lst):
    print(lst[i])
    i+=1


                          or

lst=['apple','mango','orange','grapes']
for i in range(0,len(lst)):
    print(lst[i])





6......new list to old list element are starting with capital







lst=['Apple','potato','Java','Python','dinga','dingi']
lst1=[]
for i in lst:
    if i[0].isupper():
        lst1.append(i)
print(lst1)








lst=['Apple','potato','Java','Python','dinga','dingi']
lst1=[]
for i in lst:
    if ord('A')<=ord(i[0])<=ord('Z'):
        lst1.append(i)
print(lst1)

                                
                                or



lst=['Apple','potato','Java','Python','dinga','dingi']
lst1=[]
for i in lst:
    if 'A'<=i[0]<='Z':
        lst1.append(i)
print(lst1)










7..........New list if the length of the element is more than 6



              #while loop


lst=['qspider','neem','tarmarind','dinga','manga']
lst1=[]
i=0
while i<len(lst):
    if len(lst[i])>6:
        lst1.append(lst[i])
    i=i+1
print(lst1)





          #for loop



lst=['qspider','neem','tarmarind','dinga','manga']
lst2=[]
for i in lst:
    if len(i)>6:
        lst2.append(i)
print(lst2)





lst=['qspider','neem','tarmarind','dinga','manga']
lst3=[]
for i in lst:
    count=0
    for j in i:
        count+=1
    if count>6:
        lst3.append(i)
print(lst3)








8.........Create a dictionary from a string with element and value as index



   while loop
   
   
   
   

str ='hello'
str1={}
i=0
while i<len(str):
    key=str[i]
    values=i
    str1[key]=values
    i+=1
print(f'{str1}\n')






        for loop





s='hello'
dic={}
for i in range (len(s)):
    key=s[i]
    values=i
    dic[key]=values
print(dic)





{'h': 0, 'e': 1, 'l': 3, 'o': 4}






9.........Dictionary from a list with word and reversed word




                   for loop


lst=['Dhoni','Rohit','Virat','Ashwin']
lst1={}
for i in lst:
    key=i
    values=i[::-1]
    lst1[key]=values
print(lst1)









lst=['Dhoni','Rohit','Virat','Ashwin']
lst2={}
i=0
while i<len(lst):
    key=lst[i]
    values=lst[i][::-1]
    lst2[key]=values
    i+=1
print(lst2)





10............Find  1 to 20 prime number




lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# lst1=str(lst)
# lst2=[]
# lst3=[]
# a=0
# i=1
# while lst[a]>len(lst):
#      if lst[a]%i==0:
#         lst2.append(lst[a])
#         break
#      a+=1
#      i+=1
# else:
#      lst3.append(lst[a])





lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in lst:
     a=2
     while a<i:
        if i%a==0:
          break
        a+=1
else:
     if i>1:
      print(i)















# while i<len(lst):
#     rem=lst%10
#     if rem%2==0:
#         lst1.append(rem)
#     lst=lst//10
# print(lst1)
















Typecasting      print data and type of data


lst=[1,1.1,True,1+1j,'hello',[1,2,3],(1,2,3),{1,2,3},{'a':1,'b':2}]
for i in lst:
     print(f'{i} is a {str(type(i))[8:-2]} datatype ')









lst=[1,2.2,True,2+3j,'hello',[1,2,3],(4,5,6),{7,8,9},{'a':1,'b':2}]
for i in lst:
     print(f'{i} is a {str(type(i))[8:-2]} datatype')









lst=[1,2.2,True,2+3j,'hello',[1,2,3],(4,5,6),{7,8,9},{'a':1,'b':2}]
i=0
while i<len(lst):
     print(f'{lst[i]} is a {str(type(lst[i]))[8:-2]} datatype')
     i+=1





dictionary   to add hike 20% salary

hike========>    sal+sal*20//100






name=['dinga','dingi','manga','mangi','sanga','sangi']
salary=[1000,2300,1234,2311,5678,4444]
dic={}
for i in range(len(name)):
     key=name[i]
     value=salary[i]+salary[i]*20//100
     dic[key]=value
print(dic)






dictionary key index odd length first half reverse   and    even length  second half



s=['dinga','dingi','qspider','orange','neem']
dic={}
for i in range(len(s)):
     key=s[i]
     if len(s[i])%2==0:
          value=(s[i][-2:])
     else:
          value=(s[i][0:2][::-1])
     dic[key]=value
print(dic)





                              or



s=['dinga','dingi','qspider','orange','neem']
dic={}
lst=list(s)
for i in range(len(s)):
     key=lst[i]
     if len(lst[i])%2==0:
          value=lst[i][len(lst[i])//2:]
     else:
          value=lst[i][0:len(lst[i])//2][::-1]
     dic[key]=value
print(dic)






seperate fruit flower and plant list and dictionary




lst=['rose flower','neem plant','jasmine flower','apple fruit','thulasi plant','orange fruit']
                #flower----rose,jasmine
# dic={}
# for i in lst:
#      value,key=i.split()
#      if key not in dic:
#           dic[key]=[value]
#      else:
#           dic[key]+=[value]
# print(dic)


     # print(i.split())
# print(dic[key])






lst=['rose flower','neem plant','jasmine flower','apple fruit','thulasi plant','orange fruit']
                #flower----rose,jasmine
dic={}
for i in lst:
     value,key=i.split()
     if key not in dic:
       dic[key]=[value]
     else:
          dic[key]+= [value]
print(dic)







'''

   #Assignment ------------->    datatype based on datatype in create in dictionary
   
   
   


'''
lst=[1,2.3,3,5.78,True,False,'hi','Hello',[1,2,3],[4,5,6],3+3j,7+10j]
dic={}
# for i in lst:
#      key=str(i)
#      if key not in dic:
#         value=(str(type(i))[8:-2])
#         dic[key]=value
#      else:
#         value+=(str(type(i))[8:-2])
#         dic[key]+=value
# print(dic)



 # print(str(type(i))[8:-2])




for i in range(len(lst)):
     value=lst[i]
     key=(str(type(lst[i]))[8:-2])
     # print(value)
     if key not in dic:
        dic[key]=[value]
     else:
          dic[key]+=[value]
print(dic)





'''