'''
1.Raise Error
'''
from logging import exception

# def add(n):
#     if n>10:
#         print(n+n)
#     else:
#         print('It is wrong')
# add(8)




# def add(n):
#     if n<10:
#         print(n+n)
#     else:
#         print('It is wrong')
# add(int(input('Enter:')))



#
# def add(n):
#     if n<10:
#         print(n**n)
#     else:
#         raise ValueError('Less Than 10')
# add(int(input('Enter:')))


'''
Custom Error
'''


# def Error(n):
#     if n>10:
#         print( n*n)
#     else:
#         raise TypeError(n)
# Error(int(input('Enter:')))

#
#
# class LessThanError(Exception):
#     ...
# def Error(n):
#     if n>10:
#         print(n*n)
#     else:
#         raise LessThanError ('Less than 10')
# Error(10)


# class MarriageError(Exception):
#     ...
# def Age(age):
#     if age>21:
#         print(f'Marriage')
#     else:
#         raise MarriageError(f'After {age-21}  the Marriage')
# Age(int(input('Enter:')))



# class Top10Rank(Exception):
#     ...
# class Average10Rank(Exception):
#     ...
# class Below10Rank(Exception):
#     ...
# def Mark(a):
#     if a>90:
#         raise Top10Rank('He score mark in class top 10')
#         print('congulation')
#     elif a<=90 and a>=50:
#         raise Average10Rank('He score mark in class Average 10')
#
#     else:
#         raise Below10Rank('He score mark in class Below 10')
# Mark(int(input('Enter:')))




# class ZeroBalanceError(Exception):
#     ...
# def ac_bal(a):
#     if a>0:
#         print('Amount is debited')
#     else:
#         raise ZeroBalanceError('In your account we have zero Balance')
# ac_bal(int(input('Enter:')))


#
# class ZeroBalanceError(Exception):
#     ...
# class InsufficientError(Exception):
#     ...
# def ac_bal(a,amount):
#     if a>0:
#         if amount <=a:
#             print('Amount is debited')
#         else:
#             raise InsufficientError(f'you have {a} amount')
#
#     else:
#         raise ZeroBalanceError('in your account in have zero rupees')
# ac_bal(int(input('Enter')),int(input('Enter:')))


















