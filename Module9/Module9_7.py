def is_prime(func):
    def wrapper(*args):
        resultat = func(*args)
        z = 0
        for k in range(1, resultat + 1):
            if resultat % k == 0:
                z += 1
        if z == 2:
            print('Простое')
        else:
            print("Составное")
        return resultat
    return wrapper

@is_prime
def sum_three(*args):
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_


result = sum_three(3, 3, 6)
print(result)