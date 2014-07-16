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

from Crypto.Util.strxor import strxor


def xor(a, b):
    """ Convenience method, truncates the XOR to the shortest of the two strings

        ```Crypto.Util.strxor``` raises ```ValueError``` if the two strings are not of equal lenght: which is probably
        correct, but tiresome: this method simply truncates the XOR to the shortest string

    :return: the XOR of the two byte sequences, truncated to the shortest length string
    :rtype: str
    """
    max_len = min(len(a), len(b))
    return strxor(a[:max_len], b[:max_len])



def to_dec_int(seq, base=10):
    """ Computes the decimal value of the positional representation of a list of integers, in the given base.

    :param seq: a sequence of integers, least significant digit last (in other words,
            ordered from left to right, the same way we'd read the number::

                to_dec_int([3, 4, 5]) == 345
                to_dec_int([0xa, 5, 0xf], base=16) == 2655

    Please note there is no consistency or error checking: this method assumes that the caller
    is taking care of providing a sensible sequence, with one digit per position (in whatever
    ```base``` may be): you will get unexpected results calling it with stuff like this::

                # DON'T DO THIS
                to_dec_int([10, 0xf], base=16)
                to_dec_int([9, 8], base=8)

    :type seq: list[int]
    :param base: the base, by default 10
    :type base: int

    :return: the integer value represented by the sequence of digits, in the given base
    :rtype: int
    """
    if not seq:
        return 0
    return reduce(lambda sum, p: (0, base ** p[0] * p[1] + sum[1]), enumerate(reversed(seq)))[1]


def hex2chr(h):
    """Returns the char representation of the int value [0..16)"""
    if h not in range(0, 16):
        raise ValueError('{} not a valid hex value'.format(h))
    if h < 10:
        return chr(h + ord('0'))
    else:
        return chr(h - 10 + ord('a'))


def is_hex(c):
    """ Validates the single char ```c``` as a vailid hex digit [0..9a..f]

    :param c: a single char
    :return: ```True``` if ```c``` is a valid hex digit
    :rtype: bool
    """
    if isinstance(c, str) and len(c) == 1:
        return c.lower() in '0123456789abcdef'
    else:
        raise ValueError("Must be a single char")


def random(size=16):
    """ Creates a string of random bytes - **not** cryptographically strong

    :param size: the length, in bytes, of the returned string of random hex digits
    :return: a ```size``` bytes long string
    :rtype: str
    """
    return open("/dev/urandom").read(size)
