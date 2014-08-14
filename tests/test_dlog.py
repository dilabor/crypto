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

import gmpy2
import unittest

from dlog import DLog


class TestDiscreteLog(unittest.TestCase):

    def test_find_dlog(self):
        num_bits = 10
        # Got p from: http://primes.utm.edu/lists/small/10000.txt
        p = 104659
        g = 12399
        x = 9987
        h = gmpy2.powmod(g, x, p)
        test_dlog = DLog(p, g, h, num_bits)
        result = test_dlog.compute()
        self.assertEqual(x, result)

