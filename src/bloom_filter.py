class BloomFilter:
    def __init__(self, size=1000):
        self.size = size
        self.bit_array = [0] * size

    def _hash(self, n_gram):
        return hash(n_gram) % self.size

    def add(self, n_gram):
        index = self._hash(n_gram)
        self.bit_array[index] = 1

    def check(self, n_gram):
        index = self._hash(n_gram)
        return self.bit_array[index] == 1