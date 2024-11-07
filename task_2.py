import os

def load(path, file):
    try:
        with open(os.path.join(path, file)) as file:
            loaded_txt = file.read().split()
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f'{e}\nОшибкапри открытии {file}')

def is_palindrome(list_words):
    palindromes = []
    for word in list_words:
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)
    return palindromes

if __name__ == '__main__':
    palindromes = is_palindrome(load('/usr/share/dict', 'words'))
    print(palindromes)
