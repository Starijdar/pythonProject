grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

studentsl = list(students)
studentsl.sort()
dict_ = {}

for i in range(len(grades)):
    dict_[studentsl[i]] = sum(grades[i]) / len(grades[i])


# gradesm[0] = sum(grades[0]) / len(grades[0])
# gradesm[1] = sum(grades[1]) / len(grades[1])
# gradesm[2] = sum(grades[2]) / len(grades[2])
# gradesm[3] = sum(grades[3]) / len(grades[3])
# gradesm[4] = sum(grades[4]) / len(grades[4])
#
#
# print(studentsl)
#
# dict_ = dict(zip(studentsl, gradesm))
print(dict_)