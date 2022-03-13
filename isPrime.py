def isPrime(x):
    cound = 0
    for i in range(2, x):
        if x % i == 0:
            cound += 1
    if cound == 0:
        return True
    else:
        return False
a = int(input())
print(isPrime(a))