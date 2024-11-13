'''
  #even and positive

a= int(input('Enter:'))
if a > 0:
    if a % 2 == 0:
        print('Even')
    else:
        print('Odd')
else:
    print('Negative')



dic = {'Deepan':[1234],'Dinesh':[2345],'Gokul':[3456],'Monoj':[4567]}
User_name = input('Enter:').lower()
Password = int(input('Password:'))
if User_name in dic:
        if Password == dic.values():
            print('Login')
        else:
            print('Wrong Password')
#else:
            #print('Not User_name')








a= int(input('Enter:'))
b = int(input('Enter:'))
c = int(input('Enter:'))
if a > b and a>c:
    if b>c:
        print(f'b value {b} is the second highest')
    else:
        print(f'c values {c} is the second highest')
elif b > c and b > a:
    if a > c:
        print(f'a values {a} is the second highest')
    else:
        print(f'c values {c} is the second highest')
else:
    if a > b:
        print(f'a values {a} is the second highest')
    else:
        print(f'b values {b} is the second highest')







a=[1,2,3,4,5,6,7,8,9]
i=0
while i<len(a):
    if a[i]%2==0:
        print(a[i],end=' ')
    i+=1




a=[1,2,3,4,[1,2,3]]
b=a
print(b)


'''