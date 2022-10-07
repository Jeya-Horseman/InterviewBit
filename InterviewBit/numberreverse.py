n=int(input("Enter the number: "))
reverse=0
while(n>0):
    s=n%10
    reverse=reverse*10+s
    n=n//10
print(reverse)