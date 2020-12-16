import io
from Decrypter.Utils import get_frequencies_and_table as get


def words(stringIterable):
    lineStream = iter(stringIterable)
    for line in lineStream:
        for word in line.split():
            yield word


if __name__ == '__main__':
    with io.open(r"C:\Users\user\PycharmProjects\Decrypting-Ciphers-With-Genetic-Algorithm\Moby_Dick.txt", mode="r", encoding="utf-8") as f:
        print(get(f.read().lower())[1][0])


