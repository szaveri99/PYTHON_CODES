
#QUESTION 1

from collections import Counter

lst=list(map(int,input().split()))
d=Counter(lst)
print(dict(zip(d.values(),d.keys()))[1])
