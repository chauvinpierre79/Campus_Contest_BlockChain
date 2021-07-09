import hashlib
import json
import os
import uuid

from classes.wallet import Wallet


class Block:

    def __init__(self, size, baseHash, parentHash, transations):
        self.hash = self.createHash(baseHash)
        fileExist = os.path.exists('content/blocs/' + self.hash + '.json')
        if not fileExist:
            self.size = size
            self.listTransaction = {}
            self.base_hash = baseHash
            self.parent_hash = parentHash
            self.transations = transations
            self.save()
        else:
            self.load(self.hash)
            self.size = size
            self.transations = transations

    def createHash(self, password):
        hash = hashlib.sha256(str(password).encode())
        hashCreate = hash.hexdigest()
        return hashCreate

    def check_hash(self, passwordVerify):
        if self.createHash(passwordVerify) == self.hash:
            return True
        else:
            return False

    def add_transaction(self, emetteur, recepteur, montant):
        WalletEmetteur = Wallet(emetteur)
        WalletRecepteur = Wallet(recepteur)
        t = uuid.uuid1()
        self.transations = str(t)
        a = {
            self.transations: {
                "walletEmetteur": emetteur,
                "walletRecepteur": recepteur,
                "montant": montant
            }
        }

        test = WalletEmetteur.send(a, montant, 'emmetteur')

        print(test)
        if test == False:
            print('echec')
            return
        else:
            WalletRecepteur.send(a, montant, 'recepteur')
            self.listTransaction.append(a)
            self.save()

    def get_transaction(self, transaction):
        return self.transactions[transaction]

    def get_weight(self):
        path = 'content/blocs/' + self.hash + '.json'
        return os.stat(path).st_size

    def save(self):

        data = {
            'name': self.hash,
            'base_hash': self.base_hash,
            'parent_hash': self.parent_hash,
            'transactions': self.listTransaction
        }

        pathToFile = 'content/blocs/' + self.hash + '.json'

        with open(pathToFile, 'w+') as outfile:
            str_ = json.dumps(data,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)

    def load(self, fileJson):
        with open("content/blocs/" + fileJson + ".json") as file:
            dataBlocsUnique = json.load(file)
        self.hash = dataBlocsUnique['name']
        self.base_hash = dataBlocsUnique['base_hash']
        self.parent_hash = dataBlocsUnique['parent_hash']
        self.listTransaction = dataBlocsUnique['transactions']
