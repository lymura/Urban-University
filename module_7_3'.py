import string
import os


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = set(string.punctuation + ' -')

        for file_name in self.file_names:
            file_name = os.path.abspath(file_name)
            print(f"Checking file: {file_name}")  # Выводим путь для проверки
            if not os.path.isfile(file_name):
                raise FileNotFoundError(f"The file {file_name} does not exist.")

            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    line = ''.join(ch if ch not in punctuation else ' ' for ch in line)
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))


