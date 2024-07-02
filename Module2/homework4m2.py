numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    test = numbers[i]
    if test == 1:
        continue
    z = 0
    for k in range(1, test + 1):
        if test % k == 0:
            z += 1
        if z > 2:
            break
    if z == 2:
        primes.append(test)
    else:
        not_primes.append(test)
print(primes)
print(not_primes)
