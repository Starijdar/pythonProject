import os
import time

directory = r'F:\Py\lesson\pythonProject\Module7'

if not os.path.exists('TestFolder1'):
    os.mkdir('TestFolder1')
else:
    print('Папка уже существует')

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.abspath(file)
        filetime = os.stat(file).st_mtime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(file).st_size
        parent_dir = os.path.dirname(root)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')