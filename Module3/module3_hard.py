sum_ = 0

# def count_all(*args):
#     global sum_
#     for j in range(0, len(args)):
#         for i in args[j]:
#             if isinstance(i, int):
#                 sum_ += i
#             elif isinstance(i, str):
#                 sum_ += len(i)
#             elif isinstance(i, list):
#                 count_all(i)
#             elif isinstance(i, dict):
#                 count_all(*i)
#             elif isinstance(i, set):
#                 count_all(*i)
#             elif isinstance(i, tuple):
#                 for k in i:
#                     if isinstance(k, int):
#                         sum_ += k
#                     elif isinstance(k, str):
#                         sum_ += len(k)
#                     elif isinstance(k, dict):
#                         count_all(*k)
#     return sum_





data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = count_all(data_structure)
print(result)
