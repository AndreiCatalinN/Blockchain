# coded using https://levelup.gitconnected.com/creating-a-blockchain-from-scratch-9a7b123e1f3e
# Author: Andrei Negura

from blockchain import Blockchain

def oper():
    blockchain = Blockchain()
    for _ in range(10):
        blockchain.add_new_block(str(_) + " block")

    blockchain.__str__()


if __name__ == '__main__':
    oper()