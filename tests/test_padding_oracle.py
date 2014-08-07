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
from padding_oracle import PaddingOracle, replace

__author__ = 'marco'

import unittest

VALID_CIPHER = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426f" \
               "b515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4".decode('hex')

INVALID_CIPHER = "990bdba6ff29eed7b046d1df9fb7000058b1ffb4288a580f748b4ac714c001bd4a61044426f" \
                 "b515dad3f21f18aa577c0bdf302936266926ff37ac07035d5eeb4".decode('hex')


class PaddingOracleTest(unittest.TestCase):

    URL = "http://crypto-class.appspot.com"

    def setUp(self):
        self.oracle = PaddingOracle(self.URL, prefix="po", query_arg="er")

    def test_valid(self):
        self.assertTrue(self.oracle.is_padding(VALID_CIPHER))

    def test_invalid(self):
        self.assertFalse(self.oracle.is_padding(INVALID_CIPHER))

    def test_replace(self):
        s1 = 'foo'
        self.assertEqual('zoo', replace(s1, 0, 'z'))
        s2 = 'quantunque'
        self.assertEqual('qualunque', replace(replace(s2, 3, 'l'), 4, ''))
