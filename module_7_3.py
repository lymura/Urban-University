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


# Пример использования
finder2 = WordsFinder('/Users/user/PycharmProjects/Urban_Module_5/pythonProject/test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
