import string
import random


class DNA:
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.encodings = ''.join(random.sample(self.alphabet, len(self.alphabet)))

    def mutate(self):
        first, second = random.sample(range(0, len(self.alphabet)), 2)
        self.encodings = self._swap(self.encodings, first, second)

    @staticmethod
    def _swap(s, i, j):
        s = list(s)
        s[i], s[j] = s[j], s[i]
        return ''.join(s)
