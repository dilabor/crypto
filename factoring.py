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
import utils

__author__ = 'marco'

import gmpy2
from gmpy2 import mpz, ceil, sqrt, add, sub, mul, floor


class Factoring(object):
    """ Used to factor a large integer N in its prime components p,q

        Solves the Programming Assignment of Week 6:
        https://class.coursera.org/crypto-011/quiz/attempt?quiz_id=100
    """

    def __init__(self, n):
        self.n = n
        self.log = utils.ProgressReporter()

    def _check_sol(self, p, q):
        return sub(self.n, mul(p, q)) < 0.5

    def calc_near(self):
        a = ceil(sqrt(self.n))
        p, q = self._calc_factors(a)
        assert self._check_sol(p, q)
        return p, q

    def calc_brute_force(self):
        a = ceil(sqrt(self.n))
        for n in xrange(1, 2 ** 20):
            p, q = self._calc_factors(add(a, n))
            if self._check_sol(p, q):
                return p, q
            self.log.print_progress(n)
        else:
            raise ValueError("Cannot factor {}".format(self.n))

    @staticmethod
    def solve_quadratic(a, b, c):
        """ Solves the quadratic equation ```a x2 + b x + c = 0```

        :return: the GMP result of solving the quadratic equation usign multi-precision numbers
        """
        bb = sqrt(sub(mul(b, b), mul(mpz(4), mul(a, c))))
        x1 = gmpy2.div(sub(-b, bb), mul(mpz(2), a))
        x2 = gmpy2.div(add(-b, bb), mul(mpz(2), a))
        return x1, x2

    def calc_near6(self):
        def q(p):
            # q = (2A - 3p) / 2
            return mpz(gmpy2.div(sub(mul(mpz(2), A), mul(mpz(3), p)), mpz(2)))
        A = ceil(sqrt(mul(6, self.n)))
        # p is the solution of the quadratic equation: 3/2 p^2 - Ap + N = 0
        # this is solved using the classic (-b +/- sqrt(b^2 - 4ac)/2a)
        a = gmpy2.div(gmpy2.mpfr(3), mpz(2))
        b = -A
        c = self.n
        p1, p2 = self.solve_quadratic(a, b, c)
        if self._check_sol(p1, q(p1)):
            return p1, q(p1)
        elif self._check_sol(p2, q(p2)):
            return p2, q(p2)
        raise ValueError("Cannot factor {}".format(self.n))

    def _calc_factors(self, a):
        x = sqrt(sub(mul(a, a), self.n))
        p = floor(sub(a, x))
        q = floor(add(a, x))
        return mpz(p), mpz(q)


# ############
#
# Challenges:

N1 = '17976931348623159077293051907890247336179769789423065727343008115' \
     '77326758055056206869853794492129829595855013875371640157101398586' \
     '47833778606925583497541085196591615128057575940752635007475935288' \
     '71082364994994077189561705436114947486504671101510156394068052754' \
     '0071584560878577663743040086340742855278549092581'

N2 = '6484558428080716696628242653467722787263437207069762630604390703787' \
    '9730861808111646271401527606141756919558732184025452065542490671989' \
    '2428844841839353281972988531310511738648965962582821502504990264452' \
    '1008852816733037111422964210278402893076574586452336833570778346897' \
    '15838646088239640236866252211790085787877'

N3 = '72006226374735042527956443552558373833808445147399984182665305798191' \
     '63556901883377904234086641876639384851752649940178970835240791356868' \
     '77441155132015188279331812309091996246361896836573643119174094961348' \
     '52463970788523879939683923036467667022162701835329944324119217381272' \
     '9276147530748597302192751375739387929'


def solve_q1():
    num = gmpy2.mpz(N1)
    factor = Factoring(num)
    p, q = factor.calc_near()
    print "Q1: The result is:\np = {},\nq = {}".format(p, q)


def solve_q2():
    num = mpz(N2)
    factor = Factoring(num)
    p, q = factor.calc_brute_force()
    print "Q2: The result is:\np = {},\nq = {}".format(p, q)


def solve_q3():
    num = mpz(N3)
    factor = Factoring(num)
    p, q = factor.calc_near6()
    print "Q3: The result is:\np = {},\nq = {}".format(p, q)


def main():
    num_digits = len(N1)
    print "The required precision is {}".format(2 * num_digits)
    # Configure precision to deal with large integers
    gmpy2.get_context().precision = 2 * num_digits
    solve_q1()
    solve_q2()
    solve_q3()

if __name__ == "__main__":
    main()
