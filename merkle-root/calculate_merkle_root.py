################################################################################
# Calculate Merkle Root                                                        #
################################################################################

import os, sys, traceback
import binascii
import hashlib

################################################################################
# Functions                                                                    #
################################################################################

def double_hash(hex): 
   bin = binascii.unhexlify(hex)
   hash = hashlib.sha256(bin).digest()
   hash2 = hashlib.sha256(hash).digest()
   return binascii.hexlify(hash2)

def calculate_merkle_root(left, right):
    # Convert them in little-endian hex notation
    left  = binascii.hexlify(binascii.unhexlify(left)[::-1])
    right = binascii.hexlify(binascii.unhexlify(right)[::-1])

    # Concatenate the pair
    hex = left + right
    
    # Take double SHA256 hash
    hash = double_hash(hex)
    
    # Convert result to big-endian hex notation
    root = binascii.hexlify(binascii.unhexlify(hash)[::-1])
    root = str(root, "ascii")
    
    return root

def main():
    # Transaction hashes of BTC block # 99997
    h1 = 'b86f5ef1da8ddbdb29ec269b535810ee61289eeac7bf2b2523b494551f03897c'
    h2 = '80c6f121c3e9fe0a59177e49874d8c703cbadee0700a782e4002e87d862373c6'

    merkle_root = calculate_merkle_root(h1, h2)
    print(merkle_root)

################################################################################
# Main                                                                         #
################################################################################

if __name__ == '__main__':
    try:
        main()
    except:
        traceback.print_exc(file=sys.stdout)
