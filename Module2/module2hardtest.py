def motocikl(result, i, k, n):
    for i in range(1, n):
        if i > n / 2:
            break
        for k in range(i + 1, n):
            if k == i:
                continue
            else:
                if n % (i + k) == 0:
                    result.append(f'{i}{k}')
    return result

print()
print()

result = []
i = 0
k = 0
n = int(input("Число в первой ячейке "))


motocikl(result, i, k, n)
print(*result)
