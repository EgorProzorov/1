count = 0
a = 0
def isPrime(x):
    cound = 0
    for i in range(2, x):
        if x % i == 0:
            cound += 1
    if cound == 0:
        return True
    else:
        return False
for x in range(351627, 428763):
    for y in range(2, x):
        a = 0
        if x % y == 0 and isPrime(y) == True:
            a = int(x / y)
            if isPrime(a) == True and a != 0 and a != y:
                count+=1
                a = 0
                break
            break

print(count)
