#QUESTION 1
a=int(input("Enter A :"))
b=int(input("Enter B :"))
c=int(input("Enter C :"))
cnt=0
for i in range(1,a+1):
    if i%b==0 and i%c==0:
        cnt+=1        
print("total count is : ",cnt)        
