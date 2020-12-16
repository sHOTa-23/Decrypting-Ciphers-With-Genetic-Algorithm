from Decrypter.Cell import Cell


class PopulationManager:
    def __init__(self, n_cells, cipher,n_children,freqs,table):
        self.n_cells = n_cells
        self.cipher = cipher
        self.n_children = n_children
        self.freqs = freqs
        self.table = table
        self.cells = [Cell() for _ in range(len(self.n_cells))]

    def breed(self):
        pass

    def fit_test(self):
        pass

