'''
Filter
'''


# lst=[1,2,3,4,5,6]
# for i in lst:
#     print(i)

#
# lst=[1,2,3,4,5]
# a= lambda i : i%2==0
# print(list(filter(a,lst)))
#
# lst=['Apple','bannana','Orange','Grapes']
# a= lambda i :i[0].isupper() and len(i)%2==0
# print(list(filter(a,lst)))


# lst=[1,2,3,4,5,6,7,8,9,10]
# # a=lambda i :i%2==0
# # b=lambda a:a**2
# # print(list(filter(b,a)))
# a=lambda i : i%2==0
# square=list(filter(a,lst))
# b=lambda i1:i1**2
# print(list(map(b,square)))




# lst=['Apple','bannana','Orange','Grapes']
# a=lambda i:i[0].isupper()
# b=list(filter(a,lst))
# length=lambda i1 : len(i1)%2==0
# print(list(filter(length,b)))