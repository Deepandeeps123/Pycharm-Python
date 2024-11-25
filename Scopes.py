'''
1.global scope
2.Local scope
3.Non local Scope

'''

'''
1.Global Scope



a=10
print(f'i am before {a}')
def Sample():
    a=20
    print(f'i am inside {a}')
Sample()
print(f'i am after {a}')


'''

'''
2.local scope


# a=10
# print(f'i am before {a}')
# def Sample():
#     a=20
#     print(f'i am inside {a}')
# Sample()
# print(f'i am after {a}')



a=10
print(f'i am before {a}')
def Sample():
    global a
    a=20
    print(f'i am inside {a}')
Sample()
print(f'i am after {a}')



'''



'''
3.Non-Local
'''


# a=10
# print(f'i am before {a}')
# def Sample():
#     a=20
#     print(f' i am inner {a}')
#     def Demo():
#         a=30
#         print(f'i am inner inner {a}')
#         def Demo1():
#             nonlocal a
#             a=40
#             print(f'i am inner inner inner {a}')
#         Demo1()
#         print(f'i am inner inner inner {a}')
#     Demo()
#     print(f'i am inner inner inner {a}')
# Sample()
# print(f'i am after {a}')




# a=10
# print(f'i am before {a}')
# def Sample():
#     global a
#     a=20
#     b=30
#     print(f'i am inner {a}')
#     print(f'i am inner {b}')
#     def Demo():
#         global a
#         a=100
#         nonlocal b
#         b=50
#         c=40
#         print(f'i am non local {c}')
#         print(f'i am inner inner inner {b}')
#     Demo()
#     print(f'i am local {b}')
# Sample()
# print(f'i am after {a}')

