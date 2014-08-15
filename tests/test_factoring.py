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


import factoring
import gmpy2
import unittest


class FactoringTest(unittest.TestCase):

    def setUp(self):
        gmpy2.get_context().precision = 800

    def test_factors(self):
        p = 92387
        q = 92399
        n = p * q
        factor = factoring.Factoring(n)
        pc, qc = factor.calc_near()
        self.assertEqual(p, pc)
        self.assertEqual(q, qc)
        self.assertEqual(n, pc * qc)

    def test_factors2(self):
        p = gmpy2.mpz('776531419')
        q = gmpy2.mpz('776531479')
        n = gmpy2.mul(p, q)
        factor = factoring.Factoring(n)
        pc, qc = factor.calc_near()
        self.assertEquals(p, pc)
        self.assertEquals(q, qc)
        self.assertEquals(n, gmpy2.mul(pc, qc))
