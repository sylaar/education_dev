chipertext = '16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19'
chipertext = chipertext.split()
ROWS = 5
COLS = 4
KEY = '-1 2 -3 4'
translation_matrix = [None] * COLS
start = 0
stop = ROWS
for i in range(COLS):
    translation_matrix[i] = chipertext[start:stop]
    start = stop 
    stop += ROWS
print(translation_matrix)