#if x:
#    a = "Hello World!"

#Apache License // somehow we need to make the 'b' to send in the output.

from datetime import datetime #Imports the datetime function
import hashlib as hasher # Imports the library that generate the cryptohashes
import string
import os.path
import json


#define the class of the blocks in the blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = String #insert data here from grasshopper
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

        #define the class of the blocks in the blockchain



    def __str__(self):
        return 'Block #{}'.format(self.index)


    def hash_block(self):
        sha = hasher.sha256()
        seq = (str(x) for x in ( #potentialy this is where we need to pass a string?
               self.index, self.timestamp, self.data, self.previous_hash))
        sha.update(''.join(seq).encode('utf-8'))
        return sha.hexdigest()

#String from Gh is added to the first genesis block of the blockchain.
def make_genesis_block():
    """Make the first block in a block-chain."""
    block = Block(index=0,
                  timestamp=datetime.now(),
                  data= diff,
                  previous_hash="0")
    return block

#this is where we need input from Gh.
def next_block(last_block, data=''):
    """Return next block in a block chain."""
    idx = last_block.index + 1
    block = Block(index=idx,
                  timestamp=datetime.now(),
                  data='{}{}'.format(data, idx),
                  previous_hash=last_block.hash)
    return block

#this is where the problem lies, in creating blocks, in succession. how can we replace this with a mechanism triggered from GH! on a what -if mechanism.
def test_code():
    """Test creating chain of 20 blocks."""
    blockchain = [make_genesis_block()]
    prev_block = blockchain[0]
    for _ in range(0, nb):
        block = next_block(prev_block, data= String) #for each next block, the String is also added and encoded inside each block.
        blockchain.append(block)
        prev_block = block
        print('{} added to blockchain'.format(block))
        print('Hash: {}\n'.format(block.hash))

b = next_block
a = String #test that string actually receives a value
c = diff #test that diff actually receives the difference of sets.
#c = make_genesis_block [0]
# run the test code
test_code()
