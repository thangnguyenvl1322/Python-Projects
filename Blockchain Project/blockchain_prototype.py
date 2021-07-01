from hashlib import sha256
import datetime

class Block:

    def __init__(self, transaction_details, previous_hash, nonce = 0):
        self.transaction_details = transaction_details
        self.timestamp = datetime.datetime.now()
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def print_block_details(self):
        block_transaction_details = self.transaction_details
        print('Transaction Details: {}'.format(block_transaction_details))
        print('Time-stamp: ',self.timestamp)
        print('Previous Hash: ',self.previous_hash)
        print('Block\'s Hash: ',self.hash)
        print('Nonce: ',self.nonce)

    def generate_hash(self):
        block_contents = str(self.transaction_details) + str(self.timestamp) + str(self.previous_hash) + str(self.nonce)
        hash = sha256(block_contents.encode())
        return hash.hexdigest()

class Blockchain:

    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        genesis_block = Block([],0)
        self.chain.append(genesis_block)
        return self.chain

    def print_blockchain(self):

        #These lines of code will iterate through the number of blocks in the chain
        #and for each block, it will call the 'print_block_details' methods that is
        #part of the 'Block' class.

        for x in range(len(self.chain)):
            block = self.chain[x]
            print('_____________________________')
            print('Block {}: {}'.format(x,block))
            print()
            block.print_block_details()

    def add_block(self, transaction_details):
        previous_block_hash = self.chain[-1].hash
        new_block = Block(transaction_details, previous_block_hash)
        proof = self.proof_of_work(new_block, 9)

        self.chain.append(new_block)
        return proof, new_block


    def validate_blockchain(self):

        for x in range(1,len(self.chain)):
            current_block_validation = self.chain[i]
            previous_block_validation = self.chain[i-1]

            if current_block_validation.hash != current_block_validation.generate_hash():
                print("Current hash does not equal generated hash")
                print('This is the hash that was generated: ', current_block_validation.generate_hash())
                print('This is the current hash: ', current_block_validation.hash)
                return False

            if current_block_validation.previous_hash != previous_block_validation.generate_hash():
                print("Previous block's hash got changed")

            return 'True'

    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while str(proof[0:difficulty]) != '0'*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
            print(proof)
        print('________________________________________________________________________________')
        print('FINAL PROOF: ',proof)
        print('FINAL NONCE: ', block.nonce)
        print()
        print('Proof-Of-Work has been done, Block is added!')



blockchain_beta = Blockchain()


while True:

    Enter_new_block = input('''
Enter 'y' to create a transaction
Enter 'view' to view the blockchain
''')

    if Enter_new_block == 'y':
        Done_with_sender = False
        Done_with_recipient = False
        Done_with_amount = False
        while Done_with_sender is False:
            Sender = input('Enter your name as the sender: ')
            if Sender == 'Back':
                break
            else:
                Done_with_sender = True
                while Done_with_recipient is False:
                    Recipient = input('Enter the name of the recipient: ')
                    if Recipient == 'Back':
                        Done_with_sender is False
                        break
                    else:
                        Done_with_recipient = True
                        while Done_with_amount is False:
                            Amount = input('Enter the amount of Bitcoin you wish to send: ')
                            if Amount == 'Back':
                                Done_with_sender = False
                                break
                            try:

                                Amount = float(Amount)
                                print('''
Transaction Detail:
Sender: {}
Recipient: {}
Amount: {} Bitcoin
'''.format(Sender,Recipient,Amount))

                            except:
                                print('Please enter positive numerical values only')
                                continue

                            confirmation_of_transaction = input('Enter Y to confirm, N to cancel: ')

                            if confirmation_of_transaction == 'Y':
                                Done_with_amount = True
                                new_block_transaction_details = {
                                    'Sender': Sender,
                                    'Recipient': Recipient,
                                    'Amount': Amount
                                }
                                blockchain_beta.add_block(new_block_transaction_details)
                                break
                            elif confirmation_of_transaction == 'N':
                                continue
                            else:
                                continue




    elif Enter_new_block == 'view':
        blockchain_beta.print_blockchain()

    else:
        continue

blockchain.print_blockchain()

































def nothing():
    pass
