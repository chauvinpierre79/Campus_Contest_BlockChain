import hashlib
import os
import random

from classes.block import Block


class Chain:

    def __init__(self, blocks, lastTransaction):
        self.blocks = blocks
        self.last_transaction_number = lastTransaction

    def generate_hash(self):
        global hash
        valid_hash = False
        i = 88400
        while valid_hash == False:
            i += 1
            hash = hashlib.sha256(str(i).encode()).hexdigest()
            if self.check_hash(str(hash)):
                valid_hash = True
        return hash, i

    def check_hash(self, verify_hash):

        file_exist = os.path.exists('content/blocs/' + verify_hash + '.json')
        if file_exist:
            return False
        else:
            first = verify_hash[0:4]
            if first == '0000':
                return True
            else:
                return False

    def add_block(self):
        dir = os.listdir('content/blocs/')
        ale = random.randint(0, len(dir)-1)
        result = self.generate_hash()
        instance_blocs = Block(result[0], str(result[1]), dir[ale].split('.')[0])
        instance_blocs.save()

    @staticmethod
    def get_block(hash):
        instance_blocs = Block(hash)
        a = {
            "hash": instance_blocs.hash,
            "base_hash": instance_blocs.base_hash,
            "parent_hash": instance_blocs.parent_hash,
            "transactions": instance_blocs.list_transaction
        }
        print(a)
        return a

    def add_transaction(self):
        instance_blocs = Block()

