'''
       1.length more than 8
       2. 2 upper case
       3. 2 lower case
       4. 1 number
       5. 1 special character



password=input('Enter The Password : ')
if len(password)>8:
    u_count=0
    l_count=0
    n_count=0
    sp_count=0
    for i in password:
        if i.isupper():
            u_count+=1
        elif i.islower():
            l_count+=1
        elif i.isdigit():
            n_count+=1
        else:
            sp_count+=1
    if u_count>=2 and l_count>=2 and n_count>=1 and sp_count>=1:
        print('Password Accepted.........')
    else:
        print(f'Password must be contain 2 uppercase.2 lowercase,1 number,1 special character You give onle {password}')
else:
    print(f'Password is incorrect {password} more than 8 letter only given {len(password)}')










           email validation
        1.length must more than 15
        2.  more than 15 lowercase
        3.  1 sp charater


       deepanvinayagam@gmail.com
'''
# email='deepanvinayagam@1411'
# if len(email)>=15:
#     l_count=0
#     sp_count=0
#     count=0
#     for i in email:
#         # if i in '@gmail.com':
#         #     a=str(i)
#         #     print(a,end=' ')
#         if i.islower():
#             l_count+=1
#         else:
#             sp_count+=1
#         for j in email:
#             if j in '@gmail.com':
#                 print(j,end=' ')
#
#     if l_count>=15 and sp_count>=1 :
#         print('correct')
#     else:
#         print('Not Correct')
# else:
#     print('Not')



