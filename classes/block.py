import hashlib
import json
import os
import uuid

from classes.wallet import Wallet


class Block:

    def __init__(self, hash="", base_hash="", parent_hash=""):
        self.hash = hash

        if self.check_hash(base_hash):
            if not os.path.exists('content/blocs/' + hash + '.json'):
                self.list_transaction = {}
                self.base_hash = base_hash
                self.parent_hash = parent_hash
        elif os.path.exists('content/blocs/' + hash + '.json') and base_hash == "":
            self.load(hash)
        else:
            print('Une erreur est survenue')

    def createHash(self, password):
        hash = hashlib.sha256(password.encode()).hexdigest()
        return hash

    def check_hash(self, password_verify):
        if self.createHash(password_verify) == self.hash:
            return True
        else:
            return False

    def add_transaction(self, emetteur, recepteur, montant):
        WalletEmetteur = Wallet(emetteur)
        WalletRecepteur = Wallet(recepteur)
        t = uuid.uuid1()
        transation = str(t)
        a = {
            transation: {
                "walletEmetteur": emetteur,
                "walletRecepteur": recepteur,
                "montant": montant
            }
        }
        test = WalletEmetteur.send(a, montant, 'emmetteur')
        if test == False:
            print('echec')
            return
        else:
            WalletRecepteur.send(a, montant, 'recepteur')
            self.list_transaction.update(a)
            self.save()

    def get_transaction(self, transaction):
        return self.list_transaction[transaction]

    def get_weight(self):
        path = 'content/blocs/' + self.hash + '.json'
        return os.stat(path).st_size

    def save(self):

        data = {
            'name': self.hash,
            'base_hash': self.base_hash,
            'parent_hash': self.parent_hash,
            'transactions': self.list_transaction
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
        self.list_transaction = dataBlocsUnique['transactions']
