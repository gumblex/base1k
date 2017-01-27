#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest

import base1k

class Base1kTestCase(unittest.TestCase):

    def setUp(self):
        random.seed(1024)

    def urandom(self, size):
        return bytes(random.randint(0, 255) for x in range(size))

    def test_b1kendecode(self):
        for l in range(500):
            val = self.urandom(l)
            encoded = base1k.b1kencode(val)
            decoded = base1k.b1kdecode(encoded)
            self.assertEqual(val, decoded, 'encoded value is: ' + encoded)

    def test_b4kendecode(self):
        for l in range(500):
            val = self.urandom(l)
            encoded = base1k.b4kencode(val)
            decoded = base1k.b4kdecode(encoded)
            self.assertEqual(val, decoded, 'encoded value is: ' + encoded)

    def test_b1kconcat(self):
        for j in range(50):
            for k in range(50):
                case = (self.urandom(j), self.urandom(k))
                encoded = ''.join(base1k.b1kencode(val) for val in case)
                decoded = base1k.b1kdecode(encoded)
                self.assertEqual(b''.join(case), decoded, 'encoded value is: ' + encoded)

    def test_b4kconcat(self):
        # cases = ((b'a', b'bc'), (b'abcd', b'efg'))
        for j in range(50):
            for k in range(50):
                case = (self.urandom(j), self.urandom(k))
                encoded = ''.join(base1k.b4kencode(val) for val in case)
                decoded = base1k.b4kdecode(encoded)
                self.assertEqual(b''.join(case), decoded, 'encoded value is: ' + encoded)

if __name__ == '__main__':
    unittest.main()
