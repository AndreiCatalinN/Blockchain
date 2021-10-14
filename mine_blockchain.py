# Coded using https://www.youtube.com/watch?v=ZhnJ1bkIWWk
# Author: Andrei Catalin Negura

from time import time
from hashlib import sha256

MAX_NONCE = 10 ** 11  # 100 billion


def hash(text):
    return sha256(text.encode('ascii')).hexdigest()


def mine(block_num, transactions, prev_hash, prefix_zeroes):
    start_time = time()
    prefix_str = '0' * prefix_zeroes
    for nonce in range(MAX_NONCE):
        text = str(block_num) + transactions + prev_hash + str(nonce)
        new_hash = hash(text)
        if new_hash.startswith(prefix_str):
            print(f'You successfully mined a block after: {nonce}')
            print(f"--- {time() - start_time} seconds ---")
            print(new_hash)
            return new_hash
    raise BaseException(f"could not find correct hash after trying {MAX_NONCE} times")


if __name__ == '__main__':
    transactions = '''
    Andrei -> Catalin -> 20
    Mando -> Cara -> 15
    '''

    difficulty = 4
    new_hash = mine(1, transactions, '0000000000000000000cc7df042a9aa37285977afd21dcdbaddbbc50cf1c01b6', difficulty)
