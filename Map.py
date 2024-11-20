'''
Map
                            Syntax

                        map(function,iterable)
'''

#
# lst=[1,2,3,4,5,6,7,8,9,10]
# for i in lst:
#     print(i**i)



# lst=[1,2,3,4,5,6,7,8,9]
# a=lambda sq : sq**2
# print(list(map(a,lst)))



# number=[1,2,3,4,5,6,7,8,9,10]
# a=map(lambda x : x**2,number)
# print(list(a))



# def square(*args):
#     return (args**2)
# print(square(1,2,3,4,5,6,7,8,9,10))


#
#
# lst=['apple','grapes','orange','tomato']
# for i in lst:
#     print((i,len(i)),end=' ')




# lst=['apple','grapes','orange','tomato']
# a=[ (i,len(i))    for i in lst]
# print(a)


#
# lst=['apple','grapes','orange','tomato']
# a=lambda s : (s,len(s))
# print(dict(map(a,lst)))



lst=['apple','grapes','orange','tomato']
a= lambda s : (s,len(s))
print(dict(a))

