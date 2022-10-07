import math
def maxPrimeFactors(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n /=2  # equivalent to n /= 2
    j=int(math.sqrt(n)) + 1
    for i in range(3, j, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)
# Driver code to test above function
n = 120
print(maxPrimeFactors(n))

