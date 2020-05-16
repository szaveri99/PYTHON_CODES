ar=list(map(int,input("Enter the array elements : ").split()))
res=0
n=len(ar)
for i in range(0, 32): 
      count=0
      for j in range(0,n): 
            if ( (ar[j] & (1 << i)) ): 
                count+=1
                print(count)          
      res +=(count*(n - count)*2); 
print("sum is : ",res)      
