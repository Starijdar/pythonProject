def count_all(*args):
    global sum_
    for i in args:
        if isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, int):
            sum_ += i
        elif isinstance(i, list) or isinstance(i, set) or isinstance(i, tuple):
            for j in i:
                if isinstance(j, str):
                    sum_ += len(j)
                elif isinstance(j, int):
                    sum_ += j
                elif isinstance(j, dict):
                    for c, d in j.items():
                        sum_ += len(c)
                        sum_ += d
                elif isinstance(j, tuple):
                    count_all(*j)
                elif isinstance(j, list):
                    count_all(*j)
                # if isinstance(j, int):
                #     sum_ += j
                # elif isinstance(j, str):
                #     sum_ += len(j)
                # elif isinstance(j, dict):
                #     for c, d in j.items():
                #         sum_ += len(c)
                #         sum_ += d

        elif isinstance(i, dict):
            for c, d in i.items():
                sum_ += len(c)
                sum_ += d
    return sum_

sum_ = 0

data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = count_all(*data_structure)
print(result)
