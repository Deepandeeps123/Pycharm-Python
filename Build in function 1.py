'''
1.List comprehension
'''
'''


res=[]
for i in range(1,101):
    if i%5==0:
        res.append(i)
print(res)
print(len(res))





a=[i for i in range(1,101) if i%5==0]
print(a)
print(len(a))




res=set()
for i in range(1,101):
    if i%5==0:
        res.add(i)
print(res)
print(len(res))




a={i for i in range(1,101) if i%5==0}
print(a)
print(len(a))



'''
'''
2...Dictionary comprehension



lst=[1,2,3,4,5,6,7,8,9,10]
res=[]                 #0,1   1,2    2,3
for i in range(len(lst)):
     res.append((i,lst[i]))
print(res)




res1=set()
for i in range(len(lst)):
    res1.add((i,lst[i]))
print(res1)


dic={}
for i in range(len(lst)):
    key=i
    value=lst[i]
    dic[key]= value
print(dic)






lst=[1,2,3,4,5,6,7,8,9,10]
a=[(i,lst[i]) for i in range(len(lst))]
print(a)


b={(i,lst[i]) for i in range(len(lst))}
print(b)


c={i:lst[i] for i in range(len(lst))}
print(c)





example---1


wap to key and values in square





lst=[1,2,3,4,5,6,7,8,9,10]
 #1   1   --    2    4    ---- 3      9
dic={}
for i in range(1,len(lst)+1):
    key=i
    value=i**2
    dic[key]=value
print(dic)




lst=[1,2,3,4,5,6,7,8,9,10]
res=[]
for i in range(1,len(lst)):
    a=i
    b=i**2
    c=(a,b)
    res.append(c)
print(res)





lst=[1,2,3,4,5,6,7,8,9,10]
dic={}
for i in lst:
    dic[i]=i**2
print(dic)








example-------------2



lst={'apple','bannana','orange','grapes','neem'}
# #    {0:5,1:nana,2:6,3:pes,4:4}
# dic={}
# for i,j in enumerate(lst):
#     if i%2==0:
#         key=i
#         value=len(j)
#         dic[key]=value
#     else:
#         key=i
#         value=j[len(j)//2:]
#         dic[key]=value
# print(dic)


a={i:len(j) if i%2==0 else j[len(j)//2:] for i,j in enumerate(lst)}
print(a)









    # if i%2==0:
    #  value=i
    #  key=i
    #  dic[key]=value
    # else:
    #     value=lst[i]
    #     key=i
    #     dic[key]=value
#
# print(dic)





Example-------3



city=['chennai','cuddalore','kallakurichi','salem','ooty']
population=[12344433,45544,3435654,23345,2344455]
dic={}
for i in range(len(city)):
     key=city[i]
     value=population[i]
     dic[key]=value
print(dic)








city=['chennai','cuddalore','kallakurichi','salem','ooty']
population=[12344433,45544,3435654,23345,2344455]
a={city[i]:population[i] for i in range(len(city))}
print(a)







city=['chennai','cuddalore','kallakurichi','salem','ooty']
population=[12344433,45544,3435654,23345,2344455]
dic={}
for i,j in enumerate(city):
    key=city[i]
    dic[key]=population[i]
print(dic)






city=['chennai','cuddalore','kallakurichi','salem','ooty']
population=[12344433,45544,3435654,23345,2344455]
dic={}
for i,j in zip(city,population):
    dic[i]=j
print(dic)








from itertools import zip_longest
city=['chennai','cuddalore','kallakurichi','salem','ooty']
population=[12344433,45544,3435654,23345]
dic={}
for i,j in zip_longest(city,population,fillvalue=123456):
    dic[i]=j
print(dic)


'''