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


def hex_decode(hex_str, as_ascii=False):
    """ Converts an hexadecimal string into a sequence of decimal integers, or the ASCII equivalent.

    It assumes the string to be encoded in hex (chars in pairs) and converts them into
    integers in the range [0..255].

    For example, the string ```a4e3``` would be converted into ```[164, 227]```.

    :param hex_str: a sequence of chars in the [0..9a..f] range, padded with a leading
            0 if of odd length.
    :type hex_str: str
    :param as_ascii: if this flag is ```True``` it will instead return the equivalent
            ASCII-encoded string
    :type as_ascii: bool
    :return: the hex decoded sequence of integers, least significant byte first (in other
            words, chars at position (0, 1) in ```hex_str``` will be hex decoded as the
            int at position [0] - or its ASCII equivalent.
    :rtype: list[int] or str
    :see: http://en.wikipedia.org/wiki/Hexadecimal
    """
    if len(filter(lambda x: not is_hex(x), hex_str)) > 0:
        raise ValueError('{} contains an invalid hex char'.format(hex_str))
    if len(hex_str) % 2 != 0:
        hex_str = '0{}'.format(hex_str)
    res = [int(''.join([hex_str[2 * i], hex_str[2 * i + 1]]), 16)
           for i in range(0, len(hex_str) / 2)]
    if as_ascii:
        res = ''.join([chr(i) for i in res])
    return res


def hex_encode(int_seq):
    """ Hexadecimal encoding of a sequence of integers in the [0..256) range or a of ASCII string

        See also ```hex_decode()```

    :param int_seq: a sequence of integers in the 0..255 range
    :return: a string made up of hex chars which, in pairs, represent the hex encoding of the
        sequence of integers; for example, (243, 3, 99) will be encode as ```r'f30363'```
        Integer values less than ```0xF``` will be padded with a leading `0` char; the order is
        maintained: the lowest order byte (int_seq[0]) will be encode as the first pair of chars
        (hex_encode[0],[1])
    :raises ValueError: if any of the numbers in the sequence are outsite the [0..255] range
    """
    if isinstance(int_seq, str):
        int_seq = [ord(c) for c in int_seq]
    res = r''
    for num in int_seq:
        if not isinstance(num, int) or not 0 <= num < 256:
            raise ValueError('{} should be an int in the [0..255] range'.format(num))
        q, r = divmod(num, 16)
        res = r''.join([res, hex2chr(q), hex2chr(r)])
    return res


def to_int(seq, base=10):
    """ Computes the positional representation of a list of integers, in the given base.

    :param seq: a sequence of integers, least significant digit last (in other words,
            ordered from left to right, the same way we'd read the number::

        to_int([3, 4, 5]) == 345
    :type seq: list[int]
    :param base: the base, by default 10
    :type base: int

    :return: the integer value represented by the sequence of digits, in the given base
    :rtype: int
    """
    return reduce(lambda sum, p: (0, base ** p[0] * p[1] + sum[1]), enumerate(reversed(seq)))[1]


def chr2hex(c):
    """Returns the decimal value of the char c representing an hex value (0..9 a..f)"""
    assert len(c) == 1, '{} should be a single hex char'.format(c)
    c = c.lower()
    if not is_hex(c):
        raise ValueError('{} not a valid hex char'.format(c))
    if 47 < ord(c) < 58:
        n = ord(c) - ord('0')
    else:
        n = ord(c) - ord('a') + 10
    return n


def hex2chr(h):
    """Returns the char representation of the hex value [0..16)"""
    if not is_hex(h):
        raise ValueError('{} not a valid hex value'.format(h))
    if h < 10:
        return chr(h + ord('0'))
    else:
        return chr(h - 10 + ord('a'))


def is_hex(c):
    if type(c) == str:
        return c.lower() in '0123456789abcdef'
    elif type(c) == int:
        return 0 <= c < 16
    else:
        return False


def xor(a, b):
    """ Given two hex-encoded sequences, will compute the elementwise XOR of each byte.

    :param a: the first sequence to XOR, hex-encoded
    :type a: str
    :param b: the second sequence to XOR, hex-encoded
    :type b: str
    :return: the hex-encoded string resulting from the byte-wise XOR-ing of ```a``` and ```b```
    :rtype: str
    """
    xor_dec = map(lambda x: x[0] ^ x[1], zip(hex_decode(a), hex_decode(b)))
    return hex_encode(xor_dec)


def random(size=16):
    return open("/dev/urandom").read(size)
