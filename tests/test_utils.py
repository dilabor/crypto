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
from utils import hex_encode, chr2hex, hex2chr, hex_decode, xor, to_int

__author__ = 'marco'

import unittest


class TestUtils(unittest.TestCase):
    def test_hex_encode(self):
        self.assertIs('', hex_encode(()))
        self.assertEqual(r'ff', hex_encode((255,)))
        self.assertEqual(r'6c73d5240a948c86981bc294814d',
                         hex_encode([108, 115, 213, 36, 10, 148,
                                     140, 134, 152, 27, 194, 148, 129, 77]))
        self.assertEqual(r'0a331f', hex_encode((10, 51, 31)))

    def test_raises_out_of_range(self):
        with self.assertRaises(ValueError):
            hex_encode((22, 343, 12))

        with self.assertRaises(ValueError):
            hex_encode((-1,))

    def test_chr2hex(self):
        self.assertEqual(10, chr2hex('a'))
        self.assertEqual(9, chr2hex('9'))
        self.assertEqual(15, chr2hex('f'))

    def test_chr2hex_raises(self):
        with self.assertRaises(AssertionError):
            chr2hex('abcd')

        with self.assertRaises(ValueError):
            chr2hex('z')

    def test_hex2char_back(self):
        for i in range(0, 16):
            self.assertEqual(i, chr2hex(hex2chr(i)))

    def test_to_int(self):
        self.assertEqual(8756, to_int([8, 7, 5, 6]))
        self.assertEqual('0xd7c4', hex(to_int([13, 7, 12, 4], base=16)))

    def test_hex_decode(self):
        self.assertEqual([], hex_decode(''))
        self.assertEqual([0], hex_decode('0'))
        self.assertEqual([9], hex_decode('9'))
        self.assertEqual([255, 0], hex_decode('ff00'))
        self.assertEqual([], hex_decode(''))
        self.assertEqual('0x55f3', hex(to_int(hex_decode('55f3'), base=256)))

    def test_encode_decode(self):
        self.assertEqual(r'12e45fa304e0', hex_encode(hex_decode(r'12e45fa304e0')))
        self.assertSequenceEqual((253, 16, 2, 99, 108, 225, 36, 98, 221, 12, 13, 8, 7, 10),
                                 hex_decode(hex_encode((253, 16, 2, 99, 108, 225, 36, 98, 221, 12,
                                                        13, 8, 7, 10))))


class TestConstructs(unittest.TestCase):
    def test_xor(self):
        self.assertEqual('0af3', xor('12c', xor('af3', '12c')))

