# Copyright AlertAvert.com (c) 2014.  All rights reserved.

__author__ = 'marco'

import os
import unittest

# Unit under test
import hash_blocks


class TestHashes(unittest.TestCase):

    FILE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'test.mp4')
    EXPECTED_HASH = os.path.join(os.path.dirname(__file__), 'data', 'hash.txt')

    def test_hash(self):
        self.assertTrue(os.path.exists(self.FILE_PATH), '{self.FILE_PATH} does not exist'.format(self=self))
        self.assertTrue(os.path.exists(self.EXPECTED_HASH), '{self.EXPECTED_HASH} cannot be found'.format(self=self))
        with open(self.EXPECTED_HASH) as hf:
            expected_hash = hf.read().decode('hex')
        self.assertEqual(expected_hash, hash_blocks.hash_video(self.FILE_PATH))
