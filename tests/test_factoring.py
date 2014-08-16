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
from gmpy2 import *


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

    def test_quadratic(self):
        a = mpz(123548902598275948)
        b = mpz(8978998897899876549987)
        c = mpz(387998734987)
        for x in factoring.Factoring.solve_quadratic(a, b, c):
            self.assertEqual(mpz(0),
                             mpz(add(add(mul(a, mul(x, x)), mul(b, x)), c)))

    def test_quadratic2(self):
        a = mpz('219098495924755330922739885315839558989821760933449290300994235841272120781260'
                '69429518044884213613626482453553075027958556832'
                '091384453881473705130824935695')
        b = mpz('256814353335698750589939869928128336663223103505953676235815945426095063894809'
                '6659915373324470180370635997105217841972803838'
                '7531982294661893643859138843591165215071865701681358627984')
        c = mpz('091384453881473705130824935695'
                '7531982294661893643859138843591165215071865701681358627984')
        for x in factoring.Factoring.solve_quadratic(a, b, c):
            self.assertEqual(mpz(0),
                             mpz(add(add(mul(a, mul(x, x)), mul(b, x)), c)))
