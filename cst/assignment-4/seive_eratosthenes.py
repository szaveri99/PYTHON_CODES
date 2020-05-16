n=int(input("enter the number : "))
lst_prim=[i for i in range(n+1)]
p=2

while p*p<=n:
        for i in range(p*p,n+1,p):
            lst_prim[i]=0
        p+=1
print("Prime Nos. are : ")        
print(*[lst_prim[i] for i in range(2,n+1) if(lst_prim[i]!=0)])
