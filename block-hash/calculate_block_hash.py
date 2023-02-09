################################################################################
# Calculate Block Hash                                                         #
################################################################################

import os, sys, traceback
import binascii
import hashlib

################################################################################
# Functions                                                                    #
################################################################################

def double_hash(hex_str): 
   bin = binascii.unhexlify(hex_str)
   hash = hashlib.sha256(bin).digest()
   hash2 = hashlib.sha256(hash).digest()
   return binascii.hexlify(hash2)

def calculate_block_hash(ver, prev_block, mrkl_root, time, bits, nonce):
    # Convert them in little-endian hex notation
    ver        = binascii.hexlify(ver.to_bytes(4, 'little'))
    prev_block = binascii.hexlify(binascii.unhexlify(prev_block)[::-1])
    mrkl_root  = binascii.hexlify(binascii.unhexlify(mrkl_root)[::-1])
    time       = binascii.hexlify(time.to_bytes(4, 'little'))
    bits       = binascii.hexlify(bits.to_bytes(4, 'little'))
    nonce      = binascii.hexlify(nonce.to_bytes(4, 'little'))
    print(ver)
    print(prev_block)
    print(mrkl_root)
    print(time)
    print(bits)
    print(nonce)

    # Concatenate the pair
    hex_str = ver + prev_block + mrkl_root + time + bits + nonce
    print(hex_str)
    
    # Take double SHA256 hash
    hash = double_hash(hex_str)
    print(hash)
    
    # Convert result to big-endian hex notation
    block_hash = binascii.hexlify(binascii.unhexlify(hash)[::-1])
    block_hash = str(block_hash, "ascii")
    
    return block_hash

def main():
    # Transaction hashes of BTC block # 99997
    ver        = 1
    prev_block = '000000000002b18ac1956a1388ce19d7be29532c2b79104ec172e38bd990be2f'
    mrkl_root  = '5140e5972f672bf8e81bc189894c55a410723b095716eaeec845490aed785f0e'
    time       = 1293623406
    bits       = 453281356
    nonce      = 459819282

    block_hash = calculate_block_hash(ver, prev_block, mrkl_root, time, bits, nonce)
    print(block_hash)

################################################################################
# Main                                                                         #
################################################################################

if __name__ == '__main__':
    try:
        main()
    except:
        traceback.print_exc(file=sys.stdout)
