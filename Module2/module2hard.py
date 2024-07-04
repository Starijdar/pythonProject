# n = int(input("Число в первой ячейке "))
# for i in range(1, n):
#     k = 0
#     for k in range(1, n):
#         if k == i:
#             continue
#         else:
#             if n % (i + k) == 0:
#                 print(i, k)





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
    # if (i + k) % n == 0:

# 20 - 13 14 19 119 23 28 218 37 317 46 416 515 614 713 812 911
#10 - 14 19 23 28 37 46

