#QUESTION 1
'''
a=int(input("Enter A :"))
b=int(input("Enter B :"))
c=int(input("Enter C :"))
cnt=0
for i in range(1,a+1):
    if i%b==0 and i%c==0:
        cnt+=1        
print("total count is : ",cnt)        
'''

##OUTPUT 1: 
'''
Enter A :12
Enter B :3
Enter C :2
total count is :  2
>>>
'''

##OUTPUT 2: 
'''
Enter A :6
Enter B :4
Enter C :1
total count is :  1
>>> 
'''


#QUESTION 2
'''
a=int(input("Enter a 1st no. : "))
b=int(input("Enter a 2nd no. : "))

def gcd2(a,b):
    if b==0: return a
    else: return gcd2(b,a%b)

print("GCD of 2 nos. is : ",gcd2(a,b))
'''
##OUTPUT 1: 
'''
Enter a 1st no. : 60
Enter a 2nd no. : 48
GCD of 2 nos. is :  12
>>>
'''

##OUTPUT 2: 
'''
Enter a 1st no. : 3
Enter a 2nd no. : 1
GCD of 2 nos. is :  1
>>>
'''

