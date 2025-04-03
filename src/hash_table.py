class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, n_gram):
        if n_gram in self.table:
            self.table[n_gram] += 1
        else:
            self.table[n_gram] = 1

    def get(self, n_gram):
        return self.table.get(n_gram, 0)

    def keys(self):
        return self.table.keys()