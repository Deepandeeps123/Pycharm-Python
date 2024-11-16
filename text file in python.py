'''
1.Folder
'''



# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# print(os.getcwd())


'''
Create a folder
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# os.mkdir('e12')

'''
Delete the folder
'''

# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# os.rmdir('e12')


#-----------------------------------------------------------------------------------------------------------------------------------------



'''
2.file handling the text file

1.create
2.Read
3.write
4.append
'''
'''

1.Read()
             *read()
             *readline()
             *readlines()
             
             
'''

# import os
# os.chdir(r'C:\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r'):
#     pass

'''


without close method
'''


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('sample.txt','r') as file:
#     print(file.read())

'''
with close method
'''
#
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('Sample.txt','r')
# print(a.read())
# a.close()
# a.closed



'''
1.read()
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#     print(file.read())


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('Sample.txt')
# print(a.read())


'''
2.readline(
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#     print(file.readline())

# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('Sample.txt','r')
# print(a.readline())



'''
3.Readlines()
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#     print(file.readlines())


#------------------------------------------------------------------------------------------------------------------------------------



'''
2.Create
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample1.txt','x'):
#     pass


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open("Sample11.txt",'x')
# pass




#-----------------------------------------------------------------------------------------------------------


'''
3.Write()

4.append()

        *write()
        *writelines()
'''

'''
1.write()
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample1.txt','w')  as file:
#     file.write('Hello')


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('Sample1.txt','w')
# a.write('Hello Hello')

'''
append()
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','a') as file:
#     file.write('Hello')


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('Sample1.txt','a')
# a.write('Hello')




'''
2.writelines()
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample1.txt','w') as file:
#     file.writelines(['Hello\n','Hi\n','Bye'])

# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('Sample1.txt','w')
# a.writelines(['Hello\n','Hi\n','Bye'])

'''
append()
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample1.txt','a') as file:
#     file.writelines(['Hello\n','Hi\n','Bye'])


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('Sample1.txt','a')
# a.writelines(['Hello\n','hi\n','Bye'])

#---------------------------------------------------------------------------------------------------------------------------------------------------
'''
Method
           *popen
           *rename
           *remove
'''
'''
1.popen
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# os.popen('SQL.txt','r')


'''
2.Rename
'''

# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# os.rename('SQL.txt','sql.txt')


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# os.rename('sql.txt','SQL.txt')



'''
3.Remove
'''


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# os.remove('SQL.txt')