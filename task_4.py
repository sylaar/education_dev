import os

def is_anagramm(path, file):
    try:
        with open(os.path.join(path, file)) as f:
            dict_words = []
            for line in f:
                dict_words.append(line.strip())
            user_input_word = input('Введите слово для проверки анаграмм:\n').lower()
            user_input_word_sort = sorted(user_input_word)
            anagramm = []
            for word in dict_words:
                if word != user_input_word:
                    if sorted(word) == user_input_word_sort:
                        anagramm.append(word)
            return anagramm
    except IOError as e:
        print(f'{e}\nОшибка чтения файла {file}')

if __name__ == '__main__':
    print(*is_anagramm('/usr/share/dict', 'words'), sep='\n')