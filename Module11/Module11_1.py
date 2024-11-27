import requests
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def add_student(name, meth, phys):
        global students
        new_student_dict = {"student": [name],
                       "meth": [meth],
                       "physics": [phys]}
        students = pd.read_excel('exceldoc.xlsx', index_col=0)
        new_student = pd.DataFrame(new_student_dict)
        students = pd.concat([students, new_student], ignore_index=True)
        students.to_excel('exceldoc.xlsx')



r = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
r.request.headers

print(r.headers)

try:
    with Image.open("exclusive.jpg") as im:
        print("exclusive.jpg", im.format, f"{im.size}x{im.mode}")
except OSError:
    pass

with Image.open("exclusive.jpg") as im:
    (left, upper, right, lower) = (500, 00, 501, 10)
    new_pic = im.crop((left, upper, right, lower))
    new_pic.save("newexclusive.jpg")

try:
    with Image.open("newexclusive.jpg") as im:
        print("newexclusive.jpg", im.format, f"{im.size}x{im.mode}")
except OSError:
    pass

# students_marks_dict = {"student": ["Студент_1", "Студент_2", "Студент_3"],
#                        "meth": [5, 3, 4],
#                        "physics": [4, 5, 5]}
# students = pd.DataFrame(students_marks_dict)
# print(students)

# students.to_json('st.json')
# students.to_excel('exceldoc.xlsx')

# add_student('Anton', 2, 2)

# print(students)
# students.to_excel('exceldoc.xlsx')

students = pd.read_excel('exceldoc.xlsx',
                          index_col=1,
                          parse_dates=False)
students.head()

print(students)

# students = students.cumsum()

students.plot()
# plt.xticks(np.arange(len(students)), students['0]')

plt.show()
