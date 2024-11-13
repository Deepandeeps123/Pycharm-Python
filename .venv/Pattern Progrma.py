'''
Pattern Program
'''

'''

1...



n=int(input('Enter:'))
for j in range(n):
    print('*',end=' ')


2...


n=10
for i in range(n-5):
    for j in range(n):
        print('*',end=' ')





3........


n=10
for i in range(n-5):
    for j in range(n):
        print('*',end=' ')
    print()


4................


n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()




5.


n=5
for i in range(n):
    for j in range(n):
        print('&',end=' ')
    print()



6.


n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()



7.


n=5
a=1
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print(f'--->{a}')
    a+=1




8...

n=5
a=1
for i in range(n):
    for j in range(n):
        print(f'-->{a}')
        print('*',end=' ')

    a+=1



9.....

n=5
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n-1 or j==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




10...


a=5
for i in range(a):
    for j in range(a):
        if j==0:
            print('*',end=' ')
    print()



11...


n=5
for i in range(n):
    for j in range(n):
        if i==0:
            print('*',end=' ')
    print()




12...


n=5
for i in range(n):
    for j in range(n):
        if j==n-1:
            print('*',end='')
        else:
            print(' ',end=' ')
    print()



13....


n=5
for i in range(n):
    for j in range(n):
        if i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



14...


n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



15....(number)



n=5
a=1
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1  or i==0 or j==n-1:
            print(f'{a}',end=' ')
            a+=1
        else:
           print(' ',end=' ')
    print()





16....(+)


n=5
for i in range(n):
    for j in range(n):
        if i==2 or j==2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



17...(-)



n=5
for i in range(n):
    for j in range(n):
        if i==n//2:
            print('*',end=' ')
    print()




18.....(*)


n=5
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 or i==j or i+j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



19....(%)


n=5
for i in range(n):
    for j in range(n):
        if i+j==n-1 or (i==1 and j==1) or (i==3 and j==3):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




20...

(wrong)



n=5
for i in range(n):
    for j in range(n):
        if j>n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




21..



n=5
for i in range(n):
    for j in range(n):
        if i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




22....(/)


n=5
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




23........(*)



n=11
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==n//2 or j==n//2 or i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



24...(triangle)



n=5
for i in range(n):
    for j in range(n):
        if j==0 or i>=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



25...(Right angle Triangle)



n=5
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



1....(A)





n=10
n1=5
for i in range(n):
    for j in range(n1):
        if j==0 or i==0 or i==n//2 or (j==n-1 and n//2<=j):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
    
2...(B) 


a=7
for i in range(a):
    for j in range(a):
        if j==0 or i==0 or j==a-1 or i==a//2 or i==a-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




3...(C)


n=5
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




4....(D)


n=5
for i in range(n):
    for j in range(n):
        if j==1 or i==0 or j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



5...(E)


n=7
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




6..(F)


n=6
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




7...(G)(No code wrong)


n=5
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i+j==n+1 or(i==n//2 or j==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




8...(H)




n=5
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




9...(I)


n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()
    

10..(J)


n=5
for i in range(n):
    for j in range(n):
        if j==n//2 or (i==4 and j==0 or j==1) or i==0:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()






11...(K)


n=5
for i in range(n):
    for j in range(n):
        if j==0 or i+j==n//2 or (i>j and i+j==n-1 or (i+j==n+1 and i>j)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



12....(L)

n=5
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




13...(M)


n=7
for i in range(n):
    for j in range(n):
        if j==0 or (i==j and i<3 and j<3) or (i+j==n-1 and i<=j ) or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()





14..(N)


n=5
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()






15..(O)




n=5
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




16...(P) (no proper code)


n=5
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n//2 or (j==n-1 and j<=n-1 and i==n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




17.(Q)


n=5
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n-1 or j==n-1 or (i+j==n and i>j) or (i==j and i==n-2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



18....(R)
n=5
for i in range(n):
    for j in range(n):
        if 









19...(S)

n=5
for i in range(n):
    for j in range(n):
        if i==0 or (j==0 and i<=n//2) or i==n//2 or i==n-1 or (j==n-1 and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
    
    
20...(T)

n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
    
    
    
21....(U)
n=5
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
    
    
    
    
    
    
22...(V)


n=5
n1=5
for i in range(n):
    for j in range(n1):
        if (i==j and i<=n//2 and j<=n//2) or (i+j==n-1 and i+j==n-1 and i<=j) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



23....(W)




n=5
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i+j==n-1 and i>=j) or (i==j and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()





24....(X)




n=5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



25...(Y)





n=5
n1=5
for i in range(n):
    for j in range(n1):
        if (i==j and i<=n//2 and j<=n//2) or (i+j==n-1 or i==n//2 and j==n//2) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()






26.....(Z)

n=5
for i in range(n):
    for j in range(n):
        if i==0 or i+j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




New Method..........................................




1,,,

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()




2...




n=5
for i in range(n):
    for j in range(n):
        if i>=j:
            print(f'{i}',end=' ')
        else:
            print(' ',end=' ')
    print()







n=5
for i in range(n):
    for j in range(n):
        if i<=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()






n=5
a1='a'
for i in range(n):
    for j in range(n):
        if i>=j:
            print(a1,end=' ')
            a1=chr(ord(a1)+1)
        else:
          print(' ',end=' ')
          a1 = chr(ord(a1) + 1)
    print()


1................Special Character_______________________

------------------------------------------------------------------------------------------------------------------------------------------------



n=5
a1=' '
for i in range(n):
    for j in range(n):
        if i>=j:
            print(a1,end=' ')
            a1=chr(ord(a1)+1)
        else:
            print(' ',end=' ')
    print()






n=5
for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(97+i),end=' ')
        else:
            print(' ',end=' ')
    print()





n=5
for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(j+97),end=' ')
        else:
            print(' ',end=' ')
    print()







n=5
for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(97+i),end=' ')
        else:
            print(' ',end=' ')
    print()





n=5
for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(j+97) , (chr(j+65)),end=' ',sep='')
        else:
            print(' ',end=' ')
    print()






n=7
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()










1...........(O)----Coreect -------> O



n=5
for i in range(n):
    for j in range(n):
        if (i==0 and j!=n-1 and j!=0 or j==0 and i!=0 and i!=n-1 or i==n-1 and j!=0 and j!=n-1 or j==n-1 and i!=0 and i!=n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()





2.....(C)


n=5
for i in range(n):
    for j in range(n):
        if j==0 and i!=n-1 and i!=0 or i==0 and j!=0 and j!=n-1  or i==n-1 and j!=0 and j!=n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



3.....(J)


n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==n-2 or (i==n-1 and n>0 and j!=0 and i!=j) or (i>=j and i+j==n-1 and i!=j and i!=  n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




4............(P)

n=5
for i in range(n):
    for j in range(n):
        if j==0  or i==0 and j!=0 and j!=n-1 or i==n//2 and j!=0 and j>=n//2 or (j==n-1  and i<=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



4.....(P)

n=5
for i in range(n):
    for j in range(n):
        if i==0 and j!=n-1 or j==0 or j==n//2 and i!=0 or i==n//2 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



5.....(B)


n=5
for i in range(n):
    for j in range(n):
        if i==0 and j!=n-1 or j==0 or i==n-1 and j!=n-1  or j==n-1 and i!=n-1 and i!=n//2 and i!=0 or i==n//2 and j!=n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()






n=5

for i in range(n):
    for j in range(n):
        if i==0 and j!=0 or j==0 and i!=0 or i==n-1 and j!=n-1 and j!=0:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

































































