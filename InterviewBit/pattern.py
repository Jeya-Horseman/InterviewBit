def patter(n):
    for i in range(0,n):
        for j in range(0,i):
            print("*",end=" ")
        print("")


n=8
patter(n)