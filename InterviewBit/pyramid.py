def pypart(x):
    if x==0:
        return
    else:
        pypart(x-1)
        print("*"*x)

n=6
pypart(6)