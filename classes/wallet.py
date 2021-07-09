import json
import os
import uuid


class Wallet:

    def __init__(self, id="", balance=100, history=[]):

        if id == "":
            self.unique_id = self.generate_unique_id()
            self.balance = balance
            self.history = history
            self.save()
        else:
            self.load(id)
            self.unique_id = id

    def generate_unique_id(self):
        uniqueId = uuid.uuid1()
        uniqueId = str(uniqueId)
        fileExist = os.path.exists('content/wallets/' + uniqueId + '.json')
        if fileExist:
            self.generate_unique_id()
        else:
            return uniqueId

    def add_balance(self, addPrice):
        if isinstance(addPrice, int):
            self.balance += addPrice
        else:
            print('is not Integer')
        print(self.balance)

    def sub_balance(self, lessPrice):
        if isinstance(lessPrice, int):
            if self.balance - lessPrice < 0:
                return False
            else:
                self.balance -= lessPrice
                return True
        else:
            return False

    def send(self, transation, montant, role):

        if role == 'emmetteur':
            if not self.sub_balance(montant):
                return False
        elif role == 'recepteur':
            self.add_balance(montant)

        self.history.append(transation)
        self.save()

    def save(self):
        data = {
            'unique_id': self.unique_id,
            'balance': self.balance,
            'history': self.history
        }

        pathToFile = 'content/wallets/' + self.unique_id + '.json'

        with open(pathToFile, 'w+') as outfile:
            str_ = json.dumps(data,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)

    def load(self, fileJson):
        with open("content/wallets/" + fileJson + ".json") as file:
            dataWalletUnique = json.load(file)
        self.balance = dataWalletUnique['balance']
        self.history = dataWalletUnique['history']
