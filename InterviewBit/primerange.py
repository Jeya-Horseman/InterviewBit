n=int(input("Enter the number"))
l=int(input("Enter the last number"))
for num in range(n,l+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
