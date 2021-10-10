from block import Block


class Blockchain:

    def __init__(self):
        self.blocks = []
        self.set_genesys_block()

    def __str__(self):
        for block in self.blocks:
            print(block.__str__())

    def set_genesys_block(self):
        self.blocks.append(Block("Genesis\t", '0'*64))

    def add_new_block(self, data):
        # self.blocks[-1].hash is the hash of the previous block
        self.blocks.append(Block(data, self.blocks[-1].hash))