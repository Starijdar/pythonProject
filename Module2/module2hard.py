result = []

n = int(input("Число в первой ячейке "))
for i in range(1, n):
    if i > n / 2:
        break
    for k in range(i + 1, n):
        if k == i:
            continue
        else:
            if n % (i + k) == 0:
                result.append(f'{i}{k}')

# result_string.replace("[ ]", "") 12 13 15 111 24 210 39 48 57

print(*result)

result_string = str(result).translate({ord(i): None for i in ", '[]"})
print(result_string)  #Приведение к результату примера
