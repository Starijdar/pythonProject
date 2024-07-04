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
    k = 0
    for k in range(1, n):
        if k == i:
            continue
        else:
            if n % (i + k) == 0:
                result.append(f'{i}{k}')

result_string = str(result)
# result_string.replace("[ ]", "") 12 13 15 111 24 210 39 48 57

print(result_string)
    # if (i + k) % n == 0:




