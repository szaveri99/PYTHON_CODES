#QUESTION 3
n=int(input())
s=0
ini=0

while s < n:
    ini+=1
    s+=ini
    
if s > n: print(ini-1)
if s == n : print(ini)

