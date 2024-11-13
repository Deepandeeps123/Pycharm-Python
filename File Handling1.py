'''
1.Without using context Manager
2.with using context Manager

'''

'''
1.Without using context Manager
'''


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# print(os.getcwd())
# # os.popen('Sample.txt','r')
# # os.popen('Sample.txt','w')
# a=open('Sample.txt','r')


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('Sample.txt','r')
# print(a.read())

# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('SQL.txt','r')
# print(a.read())





'''
2.With context manager
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#       print(file.read())





#-------------------------------------------------------------------------------------------------------------------------------------------------

# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#     pass
# print(file)

# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('Sample.txt','r')
# print(a.read())
# print(a.readline())
# print(a.readline())
# print(a.readlines())


'''
Brand Size Price
Addidas  9 10000
Puma     8 7000
                
Hike     7 5000
'''

'''
Brand Size Price

Addidas  9 10000

'''

# ['Brand Size Price\n', 'Addidas  9 10000\n', 'Puma     8 7000\n', '                \n', 'Hike     7 5000']




# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#     for i in file:
#         lst=i.split()
#         print(lst[0],lst[-1])



# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('Sample.txt','r')
# print(a.read())
# print(a.readline())
# print(a.readlines())


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# a=open('Sample.txt','r')
# print(a.read())
# # print(a.readline())
# # print(a.readlines())
# a.close()
# a.closed


#
#
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#       print(file.read())


#
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#     for i in file:
#         lst=i.split()
#         print(lst[0],lst[-1])




# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#     for i in file:
#         if i.strip():
#             lst=i.split()
#             print(lst[0],lst[-1])



# import  os
# no=int(input('Enter:'))
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#     if 1==no:
#         print(file.readline())
#     elif 2==no:
#         print(file.readline())
#         print(file.readline())
#     else:
#         print(file.readline())
#         print(file.readline())





# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# no=int(input('Enter:'))
# with open('Sample.txt','r') as file:
#     for i,j in enumerate(file):
#         if i==no:
#             print(j)



# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r'):
#     pass

# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample1.txt','x'):
#     pass



# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#     print(file.read())

#
#
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','w') as file:
#     # file.write('Hello')
#     # file.writelines(['Hello','hi','bye'])
#     file.writelines({'hello\n','hi\n','bye'})

#
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','a') as file:
#      file.write('Hello ')
#      file.write('Hi ')
#      file.write('Bye ')



# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','w') as file:
#     file.write('Brand ')
#     file.write('Size ')
#     file.write('Price\n')
#     file.write('Addidas ')
#     file.write('10 ')
#     file.write('10000\n')
#     file.writelines(['Puma ','10 ','7000'])





# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#     print(file.read())



'''
1.wap to copy the data one file to another
'''

# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.txt','r') as file:
#     with open('Copied.txt','w') as f1:
#         for i in file:
#             f1.write(i)




# --------------------------------------------------------------------------------------------------------------------------
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Copied.txt','r') as file:
#    print( file.read())



#
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Copied.txt','w') as file:
#     file.writelines(['Brand\t','Size\t','Color\t','Price\n'])
#     file.writelines(['Addidas\t','10\t','Red\t','10000\n'])
#     file.writelines(['Puma\t','9\t','Blue\t','9000\n'])
#     file.writelines(['    \t','    \t','    \t','     \n'])
#     file.writelines(['nike\t','9\t','Yellow\t','5000'])




# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Copied.txt','r') as file:
#     print(file.read())


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Copied.txt','r') as file:
#     with open('Copied1.txt','w') as C1:
#         for i in file:
#             C1.write(i)





'''
2.Wap to copy only colour from copied.txt
'''
# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Copied.txt','r') as file:
#     with open('Copied1.txt','w') as C1:
#         for i in file:
#             if i.strip():
#                 a=i.split()
#                 C1.write(f'{a[2]}\n')





'''

Other Method 
'''


# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Copied.txt','r') as file:
#     with open('Copied1.txt','w') as C1:
#         for i in file:
#             C1.write(i)




# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Copied1.txt','r+') as file:
#     # print(file.read())
#     file.write('Hello')




# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Copied1.txt','w+') as file:
#     file.write('Hello')
#     file.seek(0)
#     print(file.read())



# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Copied1.txt','a+') as file:
#     file.write('Hello')
#     file.seek(0)
#     print(file.read())




# import os
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Copied.txt','r') as file:
#     with open('Copied1.txt','w') as C1:
#         for i in file:
#             C1.write(i)