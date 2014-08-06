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

from Crypto.Cipher import AES
from utils import xor


def solve_q1():
    enc_msg = "20814804c1767293b99f1d9cab3bc3e7ac1e37bfb15599e5f40eef805488281d".decode('hex')
    plaintext = "Pay Bob 100$...."

    block_size = AES.block_size
    iv = enc_msg[:block_size]
    ciphertext = enc_msg[block_size:]
    attacker_plaintext = "Pay Bob 500$...."
    ivp = xor(iv, xor(plaintext, attacker_plaintext))
    print ivp.encode('hex')


def main():
    solve_q1()


if __name__ == "__main__":
    main()
