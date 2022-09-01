def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

num=int(input())
fac=1
while num>=1:
    fac*=num
    num-=1
print(fac)