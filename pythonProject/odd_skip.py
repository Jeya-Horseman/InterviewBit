arr = [3, 6, 4, 8, 5, 5,7,6]
sum = 0
for i in range(len(arr)):
    # to skip
    if arr[i] % 2 == 1 and arr[i - 1] % 2 == 0:
        continue

    # else add to sum
    else:
        sum += arr[i]

print(sum)
