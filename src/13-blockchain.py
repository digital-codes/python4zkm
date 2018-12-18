import hashlib
import struct

import pytest

# the hash generator: sha256
# reference hash, create via sha256hmac -u  :
refString = u"ottos mops trotzt\n"
refHash = "bc607eac3d2c0949cfa2fd01a32788eec5be5b1cabb4e108326f205099349cc1"
#

# target difficulty. Add more "0" to make it harder
difficulty = "000"
# max number of tries to solve the difficulty
mx = 10000000

# hash function with variation of nonce to solve difficulty
def calc(s):
    for nonce in range(mx):
        # add a number between 1 .. 4000000000 as 32 bit string value
        # to the input data
        nc = struct.pack("<LL", 32, nonce)
        #print(nc)
        # binary hash
        # create a new hash generator every time to start clean
        hg = hashlib.sha256()
        hg.update(bytes(s,"utf-8") + nc)
        # hash as hex value (text)
        hash = hg.hexdigest()
        #print(hash)
        if hash.startswith(difficulty):
            break
        # next nonce value
        nonce += 1
    # check nonce
    if nonce == mx:
        print("... too hard to compute")
        return "0", 0
    return hash, nonce


s = u"This is an example for bitcoin style proof-of-work"
for i in range (4):
    data = str(i + 1000)
    if i > 0:
        data += "+" + h
    print("Encoding: ", data)
    h,n = calc(data)
    print("Hash: ", h)
    print("Nonce: ", n,"\n")

# Note the output values and verify that a small change in an early step
# change the output of all subsequent steps
# this feature is used to verify the operations in a block chain
# you can test this in the python shell

########## test #############
def test_hash():
	hg = hashlib.sha256()
	print("String:",refString)
	s = bytes(refString,"utf-8")
	hg.update(s)
	h = hg.hexdigest()
	assert refHash == h

