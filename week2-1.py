#!/usr/bin/env python

from Crypto import Random
from Crypto.Cipher import AES
import Crypto.Util.Counter

from utils import hex_encode, hex_decode


def aes_cbc_decrypt(key, cipher):
    """AES, CBC mode: Decrypts the Hex-encoded cipher, using the Hex-encoded key"""
    key = hex_decode(key, as_ascii=True)
    cipher = hex_decode(cipher, as_ascii=True)
    iv = cipher[:AES.block_size]
    enc = AES.new(key, AES.MODE_CBC, iv)
    return enc.decrypt(cipher[AES.block_size:]).rstrip('\x08')


def aes_ctr_decrypt(key, cipher):
    """AES, CTR mode: Decrypts the Hex-encoded cipher, using the Hex-encoded key"""
    key = hex_decode(key, as_ascii=True)
    cipher_ascii = hex_decode(cipher[AES.block_size * 2:], as_ascii=True)
    iv = long(cipher[:AES.block_size * 2], 16)
    ctr = Crypto.Util.Counter.new(AES.block_size * 8, initial_value=iv)
    enc = Crypto.Cipher.AES.new(key, mode=AES.MODE_CTR, counter=ctr)
    return enc.decrypt(cipher_ascii)


####
# AES CBC Block cipher
# Q. 1
KEY_1 = '140b41b22a29beb4061bda66b6747e14'
CIPHER_1 ='4ca00ff4c898d61e1edbf1800618fb2828a226d160dad078' \
          '83d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daa' \
          'fb94ffe0c5da05d9476be028ad7c1d81'

# Q. 2
KEY_2 = '140b41b22a29beb4061bda66b6747e14'
CIPHER_2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48' \
           'e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
####
# AES CTR Block cipher
# Q. 3
KEY_3 = '36f18357be4dbd77f050515c73fcf9f2'
CIPHER_3 = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc3' \
           '88d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f' \
           '5f51eeca32eabedd9afa9329'

# Q. 4
KEY_4 = '36f18357be4dbd77f050515c73fcf9f2'
CIPHER_4 = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45fa' \
           'a8952aa0e311bde9d4e01726d3184c34451'

if __name__ == "__main__":
    print "Q. 1 solution: ", aes_cbc_decrypt(KEY_1, CIPHER_1)
    print "Q. 2 solution: ", aes_cbc_decrypt(KEY_2, CIPHER_2)
    print "Q. 3 solution: ", aes_ctr_decrypt(KEY_3, CIPHER_3)
    print "Q. 4 solution: ", aes_ctr_decrypt(KEY_4, CIPHER_4)
