from classes.block import Block


from classes.wallet import Wallet


wallet1 = Wallet()



wallet1.load("4eb2e20a-dff4-11eb-906f-acde48001122")
print(wallet1.balance)
print(wallet1.history)



#wallet1.add_balance(10)


#block1 = Block("dsgfffdd","aze","")
#block1.load("0000a456e7b5a5eb059e721fb431436883143101275c4077f83fe70298f5623d")












#block1.add_transaction('4eb2e20a-dff4-11eb-906f-acde48001122', '6a269023-dff4-11eb-a50f-acde48001122', 100)
# instanceBlocs.add_transaction('dsfdsfscdsc', 'fddsfsdfds', 30)

#a = Block.check_hash('aze')
#print(a)
