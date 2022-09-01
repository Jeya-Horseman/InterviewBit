def largestNumber(array):
    if len(array) == 1:
        return str(array[0])
    for i in range(len(array)):
        array[i] = str(array[i])
    for i in range(len(array)):
        for j in range(1 + i, len(array)):
            #[54, 546, 548, 60]
            x=array[j]+array[i]
            y=array[i]+array[j]
            if x > y:
                array[i], array[j] = array[j], array[i]
    result = ''.join(array)
    if (result == '0' * len(result)):
        return '0'
    else:
        return result
a = [54, 546, 548, 60]
print(largestNumber(a))
