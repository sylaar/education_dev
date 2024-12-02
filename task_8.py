chipertext = '16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19'
chipertext = chipertext.split()
ROWS = 5
COLS = 4
KEY = '-1 2 -3 4'
key_int = [int(x) for x in KEY.split()]
translation_matrix = [None] * COLS
start = 0
stop = ROWS
for i in range(COLS):
    translation_matrix[i] = chipertext[start:stop]
    start = stop 
    stop += ROWS
print(*translation_matrix, sep='\n')
print()
for idx, key in enumerate(key_int):
    if key < 0:
        translation_matrix[idx] = translation_matrix[idx][::-1]
print(*translation_matrix, sep='\n')

result_text = ''
for i in range(COLS):
    for item in translation_matrix:
        word = item[i]
        result_text += word + ' '
print(result_text)