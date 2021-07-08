import uuid


class Wallet:

    def __init__(self):
        self.unique_id = self.generate_unique_id

    

    @staticmethod
    def generate_unique_id():
        uuidOne = uuid.uuid1()
        print ("ID unique = ")
        print(uuidOne)
        return uuidOne
