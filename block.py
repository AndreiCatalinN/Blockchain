from hashlib import sha256


class Block():

    def __init__(self, data, prev_block_hash):
        self.data = data
        self.hash = ''
        self.prev_block_hash = prev_block_hash
        self.calculate_hash()

    def __str__(self):
        return self.data + "\t" + self.prev_block_hash

    def is_hash_valid(self, hash):
        return hash.startswith('0' * 3)

    def calculate_hash(self):
        hash = ''
        nonce = 0

        while not self.is_hash_valid(hash):
            temp = self.__str__() + str(nonce)
            hash = sha256(temp.encode()).hexdigest()
            nonce += 1

        self.hash = hash
