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

__author__ = 'marco'

from utils import xor


# Week 2 - Problem Set
def resolve_q2():
    cost = 200
    brute_speed = 10**9
    spend = 4 * 10**12
    num_cores = spend / cost
    tot_speed = num_cores * brute_speed
    print tot_speed, 'brute force ops / sec'
    time_spent = 2**128 / tot_speed
    years = (time_spent / 3600) / (24 * 365)
    print('{years}BN years'.format(years=years / 10**9))


def resolve_q4():
    lefties = {1: ("7b50baab", "ac343a22"),
               2: ("2d1cfa42", "eea6e3dd"),
               3: ("4af53267", "87a40cfa"),
               4: ("9f970f4e", "6068f0b1")}
    for k in lefties:
        res = strxor.strxor(lefties[k][0].decode('hex'),
                            lefties[k][1].decode('hex'))
        print('{k}: {result}'.format(k=k, result=[ord(c) for c in res]))


def resolve_q8():
    msgs = [
        'We see immediately that one needs little information to begin to break down the process.',
        'The most direct computation would be for the enemy to try all 2^r possible keys, '
        'one by one.',
        'If qualified opinions incline to believe in the exponential conjecture, then I think we '
        'cannot afford not to make use of it.',
        'An enciphering-deciphering machine (in general outline) of my invention has been sent '
        'to your organization.'
    ]
    print 'Estimated len:', 128 - 128/8
    for i, msg in enumerate(msgs):
        print('{i}: {len}'.format(len=len(msg), i=i+1))



def main():
    print('Q2.')
    resolve_q2()
    print('===\nQ4.')
    resolve_q4()
    print('===\nQ8.')
    resolve_q8()


if __name__ == "__main__":
    main()
