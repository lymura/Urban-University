import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(char, ' ')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                positions[name] = words.index(word) + 1
            else:
                positions[name] = None
        return positions

    def count(self, word):
        word = word.lower()
        counts = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            counts[name] = words.count(word)
        return counts

# Пример использования
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))     # Позиция первого вхождения
print(finder.count('teXT'))    # Количество вхождений
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
