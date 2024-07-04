n = int(input("Число в первой ячейке "))
for i in range(1, n):
    if i > n / 2:
        break
    for k in range(i + 1, n):
        if k == i:
            continue
        else:
            if n % (i + k) == 0:
                print(f'{i}{k}', end="")
