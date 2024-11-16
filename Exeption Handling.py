'''
Exeption Handling

                     Exception
                     *Specific Exception
                     *Generic Exception
                     *Multiple Exception
'''

'''
Try :
    Code
ExCept :


Else :

Finally :

'''

# print(s)
# print('Hello')



# print('Hello')
# print(s)




'''
1.General Exception
'''
# a=10
# b=0
# print(a//b)
#
#
# a=10
# b=0
# try:
#     print(a//b)
# except:
#     print('Error')
# else:
#     print('No Error')
# finally:
#     print('This is Exception Handling z z')


'''
Error
This is Exception Handling

a=10
b='Hello'
try:
    print(a%b)
except :
    print('Error')
else:
    print('No erro')
finally:
    print('It is Manatory')




Error
It is Manatory




# lst=[1,2,0,3,4,0,5,6,0]
# for i in lst:
#     print(i)


# lst=[1,2,0,3,4,0,5,6,0]
# for i in lst:
#     print(25//i)

# lst=[1,2,0,3,4,0,5,6,0]
lst=[1,2,4,0,5,6,0,4,2]
for i in lst:
    try:
        print(45//i)
    except:
        print('Error')
    # else:
    #     print('No error')
    # finally:
    #     print('This is Error Topic')


a=10
try:
    print(a[1])
except:
    print('Error')
else:
    print('No error')
finally:
    print('''''')

'''


#----------------------------------------------------------------------------------------------------------------------------------------------------

'''
2.Specific Exception
'''
'''
a=10
print(c)



NameError: name 'c' is not defined





a=10
try:
    print(c)
except NameError:
    print('Error')
else:
    print('No error')
finally:
    print('It is Mantatory') 






a=10
try:
    print(a[1])
except NameError:
    print('Error')
else:
    print('No error')
finally:
    print('It is mantatory')




a=10
try:
    print(a'z')
except NameError:
    print('Error')
else:
    print('No error')
finally:
    print('It is manatator')






a=65
try:
    print(a[1])
except TypeError as msg:
    print(f'TypeError: {msg}')
else:
    print('No Error')
finally:
    print('')



'''




#-----------------------------------------------------------------------------------------------------------------------------



'''
3.Specific Exception

                    Syntax
                    
                try:
                   statement
                except (Error Name1 ,error Name2 ,...........):
                    statement
                else:
                    statement
                finally:
                    statement



a=10
try:
    # print(a[1])
    print(a.add(1))
except TypeError as msg:
    print(f'Typeerror:{msg}')





a=10
try:
    # print(a[1])
    # print(a.add(1))
    print(a.append())

except TypeError  as msg:
    print(f'Error :{msg} ')
else:
    print('No Error')
finally:
    print('')




'''


'''
4.Multiple Exception
                              Syntax
                        try:
                            statement
                        except <ErrorName1>:
                            statement
                        except <ErrorName2>:
                            statement
                        except <ErrorName3>:
                            statement
                        except <ErrorName4>:
                            statement
                            .
                            .
                            .
                            .
                            
                        else:
                            statement
                        finally:
                            statement


a=int(input('Enter:'))
try:
    print(a[100])
except TypeError as msg:
    print(f'Error:{msg}')
except ValueError as msg:
    print(f'Error:{msg}')
except AttributeError as msg:
    print(f'Error:{msg}')
except ZeroDivisionError as msg:
    print(f'Error:{msg}')
else:
    print('No Error')
finally:
    print('')




'''


#----------------------------------------------------------------------------------------------------------------------------------------

'''
Raise and custom Exception
'''
'''
1.Raise

Name=input('Enter:')
age=int(input('Enter:'))
if age>21:
    print(f'{Name} congrulation ' )
else:
    print(f'{21-age} after years')
print('Program......')




name=input('Enter:')
age=int(input('Enter:'))
if age>21:
    print(f'{name} congrulation ' )
else:
    raise Exception (f'{21-age} after years')
print('Program......')




'''


class AgeError(Exception):
    ...
name=input('Enter:')
age=int(input('Enter:'))
if age>21:
    print(f'{name} congrulation ' )
else:
    raise AgeError (f'{21-age} after years')
print('Program......')
