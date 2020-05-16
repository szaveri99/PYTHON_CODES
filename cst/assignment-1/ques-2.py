#QUESTION 2

lst=list(map(int,input().split()))
lst.sort()
s=99
for i in range(len(lst)-1):
    s=min(lst[i]^lst[i+1],s)
print(s)    

