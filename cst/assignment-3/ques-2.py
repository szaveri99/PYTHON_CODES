l=[]
print("Enter the elements : ")
lst=list(map(int,input().split()))
l=[lst[i:j] for i in range(len(lst)) for j in range(i+1,len(lst)+1)]
print(l)





















