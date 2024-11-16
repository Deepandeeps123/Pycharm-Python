'''
Types of Python error

'''
'''
1.Name Error


a=10
print(b)


s='Hello'
pint(s)


NameError: name 'b' is not defined

'''


'''
2.Attribute Error

s='Hello'
s.append('Hi')




AttributeError: 'str' object has no attribute 'append'



'''


'''
3.Value Error



s='Hello'
print(s.index('z'))



ValueError: substring not found


'''

'''
4.Index Error

s='Hello'
print(s[100])




IndexError: string index out of range


'''


'''
5.Key Error


dict={'a':1,'b':2}
print(dict['c'])



KeyError: 'c'


'''




'''
6.Type Error


a=10
print(a[1])




TypeError: 'int' object is not subscriptable


'''


'''
7.Zero Division Error

a=10
b=0
print(a%b)


ZeroDivisionError: integer modulo by zero


'''


'''
8.IndentationError

     s='Hi'
print(s)



IndentationError: unexpected indent
'''


'''
9.Syntax Error


a=''hi''
print(a)


SyntaxError: invalid syntax

'''
