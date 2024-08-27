import io


class WordsFinder:
    file_names = []
    ignore_list = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *name):


        for i in name:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            word_list = []
            with open(i, encoding='utf-8') as file:
                for line in file:
                    for char in self.ignore_list:
                        if char in line:
                            line = line.replace(char, '')
                    for j in line.split():
                        word_list.append(j.lower())
                all_words[i] = word_list
        return all_words

    def find(self, word):
        finder = self.get_all_words()
        new_dict = {}
        for name, words in finder.items():
            pos = 0
            for i in words:
                pos += 1
                if i == word.lower():
                    break
            new_dict[name] = pos
        return new_dict

    def count(self, word):
        new_dict = {}
        counter = self.get_all_words()
        for name, words in counter.items():
            count = 0
            for i in words:
                if i == word.lower():
                    count += 1
            new_dict[name] = count
        return new_dict


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))



# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# # print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

print(finder1.file_names)
