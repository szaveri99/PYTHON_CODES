n=input("Enter a No. : ")
n=" ".join(n)
l=list(map(int,n.split(" ")))

while len(str(sum(l))) > 1:
    n=str(sum(l))
    n=" ".join(n)
    l=[]
    l=list(map(int,n.split(" ")))

    if sum(l) == 1:
        print("Its a magic Nunber with sum ",sum(l))
        break
else :
    print("Not a magic number..")
'''    






















