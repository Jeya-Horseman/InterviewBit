n=int(input())
if n > 0:
    for i in range(0,n):
        result = 0
        result +=pow(i,3)
        print (result)
else:
    print('must be non-negative number')
