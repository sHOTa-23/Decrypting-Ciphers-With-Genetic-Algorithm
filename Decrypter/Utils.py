import numpy as np


def get_frequencies_and_table(text):
    freqs = np.zeros(26)
    table = np.zeros((26, 26), dtype=np.int)
    cnt = 0
    last_ind = 0
    for ch in text:
        ind = ord(ch) - 97
        if ind in range(0, 32):
            freqs[ind] += 1
            if cnt > 0:
                table[last_ind][ind] += 1
            last_ind = ind
            cnt += 1
        else:
            cnt = 0
    return freqs, table
