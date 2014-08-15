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
import datetime

p = gmpy2.mpz('134078079299425970995740249982058461274793658205923933'
              '77723561443721764030073546976801874298166903427690031'
              '858186486050853753882811946569946433649006084171')

g = gmpy2.mpz('11717829880366207009516117596335367088558084999998952205'
              '59997945906392949973658374667057217647146031292859482967'
              '5428279466566527115212748467589894601965568')

h = gmpy2.mpz('323947510405045044356526437872806578864909752095244'
              '952783479245297198197614329255807385693795855318053'
              '2878928001494706097394108577585732452307673444020333')


class DLog(object):

    NUM_BITS = 20
    B = pow(2, NUM_BITS)
    CHECKPOINT = 4096

    def __init__(self, p, g, h, num_bits=NUM_BITS):
        self.p = p
        self.g = g
        self.h = h
        self.B = pow(2, num_bits)
        self.g_B = gmpy2.powmod(g, self.B, p)
        self.lookup_table = {}
        self.log = utils.ProgressReporter()

    def compute(self):
        self.build_table(end=self.B)
        rhs = self.g_B
        for x0 in xrange(1, self.B):
            x1 = self.lookup_table.get(rhs, None)
            if x1:
                res = gmpy2.f_mod(gmpy2.add(gmpy2.mul(x0, self.B), x1), self.p)
                return res
            if x0 and (x0 % self.CHECKPOINT) == 0:
                self.log.print_progress(x0)
            rhs = gmpy2.f_mod(gmpy2.mul(rhs, self.g_B), self.p)

    def calc_right_side(self, x0):
        return gmpy2.powmod(self.g_B, x0, self.p)

    def build_table(self, start=1, end=B):
        g_x1 = gmpy2.powmod(self.g, start, self.p)
        for x1 in xrange(start, end):
            lhs = gmpy2.divm(self.h, g_x1, self.p)
            self.lookup_table[lhs] = x1
            if (x1 % self.CHECKPOINT) == 0:
                self.log.print_progress(x1)
            g_x1 = gmpy2.f_mod(gmpy2.mul(g_x1, self.g), self.p)


def main():
    dlog = DLog(p, g, h)
    print 'Computing dlog:'
    result = dlog.compute()
    diff = gmpy2.sub(h, gmpy2.powmod(g, result, p))
    if not result:
        print "Not found"
    else:
        print "Found value: {}".format(result)
        print "Diff with given solution: {}".format(diff)

if __name__ == '__main__':
    main()
