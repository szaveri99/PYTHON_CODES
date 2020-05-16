a=int(input("Enter a no. : "))
b=int(input("Enter a no. : "))
cnt=0

sign= (-1 if ((a<0) ^ (b<0)) else 1)

a=abs(a)
b=abs(b)

while a>=b:
        a=a-b
        cnt+=1
print("Quotient is : ",sign*cnt)        
        
