l=[1,2,3,4,5,6,7,8,9,10,11,12,6]
mid=len(l)//2
output=[]

for i in l:
    if i<mid+1:
        output.append(i)
        continue
    else:
        for j in l[::-1]:
            if l[j]!=l[i]:
                output.append(j)
                continue
            break
    break
print(output)




