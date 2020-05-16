print("Enter the Elements : ")
lst=list(map(int,input().split()))

a=[i for i in lst if i%2]
b=[i for i in lst if i%2!=0]

if  len(a) < len(b): print("No.s are : ",a)
else : print("No.s are",b)    










