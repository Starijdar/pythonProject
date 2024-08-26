def custom_write(file_name, strings):
    string_positions = {}
    string_numb = 1
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        string_positions[(string_numb, file.tell())] = i
        file.write(f'{i}\n')
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
