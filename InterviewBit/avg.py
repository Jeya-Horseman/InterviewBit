n=int(input("Number of elements"))
l=[]

for i in range(1,n+1):
    s=int(input("Enter the element"))
    l.append(s)
avg=sum(l)/2
print(avg)