'''
1,Max Element in List
'''
'''
lst=[3,5,7,9,3,2]
a1=[]
a=sorted(lst)
b=a[-1]
print(b)
print(a1.append(b))
       (or)
lst=[3,5,7,9,3,2]
max=0
for i in lst:
    if i>max:
        max=i
print(max)





2,Find the intersection

nums1=[1,2,2,5]
nums2=[2,2]
a=nums1.i
print(a)

   (or)

nums1=[1,2,2,5]
nums2=[2,2]
a=[]
for i in nums1:
    if i in nums2:
        a.append(i)
print(a)


3.Find the unique(dupulicate) number


nums=[1,8,1,2,3,2,4,5,4,5]
a=[]
b=set(nums)
c=list(b)
print(c)


[1, 2, 3, 4, 5, 8]


                   (Or)
                   
                   
nums=[1,8,1,2,3,2,4,5,4,5]
a=[]
for i in nums:
    if i not in a:
        a.append(i)
print(a)


>>>>>[1, 8, 2, 3, 4, 5]


4.output---CAD

s='11101011110'
count=0
for i in s:
    if i=='1':
        count=count+1
    else:
        print(chr(64+count))
        count=0
print(count)


5.43----->4+3====> 7 prime

num=43
res=True
sum=0
i=2
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)
if sum%i==0:
    res=False
i+=1
if res==True:
    print('Prime ')
else:
    print('Not Prime')
'''




'''
import sys

value = int(input("Enter a value: "))

if value > 10:
    print("Value is greater than 10.")
    sys.exit(1)  # Exit with code 1 if value is greater than 10
elif value == 10:
    print("Value is equal to 10.")
    sys.exit(2)  # Exit with code 2 if value is equal to 10
else:
    print("Value is less than 10.")
    sys.exit(3)  # Exit with code 3 if value is less than 10


'''
def example_function(value):
    # Exit early if the value meets a specific condition
    if value == "exit":
        print("Exiting early.")
        return  # Exit the function immediately

    # Continue with other conditions if the early exit condition is not met
    if value == "apple":
        print("The value is apple.")
    elif value == "banana":
        print("The value is banana.")
    elif value == "cherry":
        print("The value is cherry.")
    else:
        print("Unknown value.")

# Test cases
example_function("exit")     # Exits early
example_function("apple")     # Proceeds with conditions
example_function("banana")    # Proceeds with conditions
example_function("grape")     # Proceeds with conditions
