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

"""
    This solves the Week 3 Programming Assignment

    Computes the 1k-block hashes of a variable length file and appends the hash of each
    block to the preceding block, going from last block to first, until reaching block B1
    and emitting the H0 hash as the output.

    See the full description of the problem here_.

    .. _here: TODO: Add URL

    The expected result is: ```5b96aece304a1422224f9a41b228416028f9ba26b0d1058f400200f06a589949```
"""

from Crypto.Hash import SHA256
from argparse import ArgumentParser


BLOCK_SIZE = 1024


def hash_(block, prev_block_hash):
    s = SHA256.new()
    s.update(block)
    s.update(prev_block_hash)
    return s.digest()


def hash_video(fname):
    with open(fname, 'rb') as video:
        blocks = []
        bv = video.read(BLOCK_SIZE)
        while bv:
            blocks.append(bv)
            bv = video.read(BLOCK_SIZE)
    # At this point the video blocks are in reversed order, the first block possibly shorter than BLOCK_SIZE
    blocks.reverse()
    # Note that, to complete the assignment, all we need is to compute H0, so we can throw the blocks away once
    # the hash has been computed and appended to the next block
    hh = ''
    for bv in blocks:
        hh = hash_(bv, hh)
    return hh


def parse():
    parser = ArgumentParser(description="Computes the SHA256 of a large video file, chunking it in blocks")
    parser.add_argument('--file', '-f', help="The full path to the file to hash")
    return parser.parse_args()


def main():
    conf = parse()
    full_hash = hash_video(conf.file)
    print full_hash.encode('hex')


if __name__ == '__main__':
    main()
