l=[1,2,3,4,5,6,7,8,9,10]
mid=len(l)//2
output=[]

for i in range(1,len(l)):
    if i<mid+1:
        output.append(i)
        continue
    else:
        for j in l[::-1]:
            if j!=mid:
                output.append(j)
                continue
            break
    break
print(output)    




