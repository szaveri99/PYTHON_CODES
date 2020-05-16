a=int(input("Enter No. : "))
b=int(input("Enter No. : "))

def gcd1(a,b):
    if a==0 : return b
    else : return gcd1(b%a,a)

def lcm(a,b):
     return (a*b) // gcd1(a,b)

print("GCD of two numbers is : ",gcd1(a,b))
print("LCM of two numbers is : ",lcm(a,b))






















