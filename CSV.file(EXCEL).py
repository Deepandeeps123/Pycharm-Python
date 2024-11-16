'''
CSV.reader

              *Reader()
              *Dict Reaader()
'''


# import os
# import csv
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open ('Sample.csv','r') as file:
#     a=csv.reader(file)
#     print(list(a))


#
#
# import os
# import csv
# from csv import DictReader
#
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.csv','r') as file:
#     a=DictReader(file)
#     print(list(a))



#------------------------------------------------------------------------------------------------------------------------------------------------------


'''
2.To write the csv file

               *csv.writer()
               *csv.Dictwritter()
'''

# import os
# import csv
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open ('Sample1.csv','w') as file:
#     row=csv.writer(file)
#     row.writerow(['Name','Age','Gender'])


#
# import os
# import csv
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open ('Sample1.csv','w',newline='') as file:
#     row=csv.writer(file)
#     row.writerows([['Dinga',21,'Male'],['Dingi',22,'Female']])



# import os
# import csv
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample1.csv','w') as file:
#     row=csv.writer(file)
#     row.writerow(['Dinga',21,'Male','200000','Developer'])




'''
example
'''
#
# import os
# import csv
# with open('Sample1.csv','w') as file:
#     row=csv.DictWriter(file,['name','Age','Gender'])
#     row.writerow({'name':'Minga'})






# import os
# import csv
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.csv','w') as file:
#     row=csv.DictWriter(file,['Name','Age','Gender'])
#     # # row=csv.writer(file)
#     # # csv.writeheader()
#     # row.writeheader()
#
#     row=csv.DictWriter(file)
#     print(list(row))







'''
1.wap to point first name and gender
'''
#
# import os
# import csv
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open('Sample.csv','r',newline='') as file:
#     row=csv.reader(file)
#     # next(row)
#     for i in row:
#         print(i[0],i[1])



# import os
# import csv
# os.chdir(r'C:\Users\WELCOME\OneDrive\Desktop')
# with open ('Sample.csv','r') as file:
#     sum1=0
#     row =csv.reader(file)
#     next(row)
#     for i in row:
#         sum1=sum1+int(i[1])
# print(sum1)



# import os
# import csv
# with open('Sample1.csv','a',newline='') as file:
#     row=csv.DictWriter(file,['name','age','gender'])
#     NameError: name 'c' is not defined



# import os
# import csv
# with open('Sample1.csv','w',newline='') as file:
#     row=csv.DictWriter(file,['name','age','gender'])
#     row.writerows([{'name':'dinga','age':32,'gender':'male'},{'name':'dingi','age':22,'gender':'Female'}])

