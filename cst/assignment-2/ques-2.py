#QUESTION 2
a=int(input("Enter a 1st no. : "))
b=int(input("Enter a 2nd no. : "))

def gcd2(a,b):
    if b==0: return a
    else: return gcd2(b,a%b)

print("GCD of 2 nos. is : ",gcd2(a,b))

