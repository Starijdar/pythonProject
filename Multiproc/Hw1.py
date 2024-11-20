import multiprocessing
from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_info = []
    # print('Процесс пошел')
    with open(name, 'r') as file:
        for x in file:
            line = file.readline()
            all_info.append(line)


filelist = [f'./file {number}.txt' for number in range(1, 5)]

# time1 = datetime.now()
# for i in filelist:
#     read_info(i)
# time2 = datetime.now()
#
# vremia = time2 - time1
# print(vremia)
#
# time1 = datetime.now()
# read_info('file 1.txt')
# read_info('file 2.txt')
# read_info('file 3.txt')
# read_info('file 4.txt')
# time2 = datetime.now()
#
# vremia = time2 - time1
# print(vremia)

time1 = datetime.now()

if __name__ == '__main__':
    with Pool(processes=4) as p:
        p.map(read_info, [name for name in filelist])

    time2 = datetime.now()


    vremia = time2 - time1
    print(vremia)