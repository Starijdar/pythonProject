from datetime import datetime
from threading import Thread
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for x in range(1, word_count + 1):
            file.write(f'Какое то слово № {x} \n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.now()

result_time = end_time - start_time
print(result_time)

start_time = datetime.now()

thr_one = Thread(target=write_words, args=(10, 'example5.txt'))
thr_two = Thread(target=write_words, args=(30, 'example6.txt'))
thr_three = Thread(target=write_words, args=(200, 'example7.txt'))
thr_four = Thread(target=write_words, args=(100, 'example8.txt'))

thr_one.start()
thr_two.start()
thr_three.start()
thr_four.start()

thr_one.join()
thr_two.join()
thr_three.join()
thr_four.join()

end_time = datetime.now()

result_time = end_time - start_time
print(result_time)
