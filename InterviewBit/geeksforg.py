def strpatte(str,len):
    for i in range(0,len):
        j=len-1-i
        for k in range(0,len):
            if (k==i or k==j):
                print(str[k],end="")
            else:
                print(end=" ")
        print("\n")
# Driver code
str = "geeksforgeeks"
len = len(str)
strpatte(str, len)
