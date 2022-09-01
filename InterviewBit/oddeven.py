arr=[2,3,4,6,7,7]
sum=0
for i in range(len(arr)):
	if arr[i]%2==1 and arr[i-1]%2==0: continue
	else:sum+=arr[i]
print(sum)