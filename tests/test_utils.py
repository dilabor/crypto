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

from Crypto.Util import strxor
import unittest

from utils import hex2chr, to_dec_int

__author__ = 'marco'


class TestUtils(unittest.TestCase):
    def test_hex2char(self):
        for i in range(0, 10):
            self.assertEqual(chr(ord('0') + i), hex2chr(i))
        for i in range(10, 16):
            self.assertEqual(chr(ord('a') + i - 10), hex2chr(i))

    def test_to_int(self):
        self.assertEqual(8756, to_dec_int([8, 7, 5, 6]))
        self.assertEqual('0xd7c4', hex(to_dec_int([13, 7, 12, 4], base=16)))
        self.assertEqual(0j, to_dec_int([]))
        self.assertEqual(16, to_dec_int([1, 0], base=16))
        self.assertEqual(10, to_dec_int([0xa], base=16))
