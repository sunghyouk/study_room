import unittest

import ch_36_2


class TestPrime(unittest.TestCase):
    def test_prime_5(self):
        isprime = ch_36_2.is_prime(5)
        self.assertEqual(isprime, True)

    def test_prime_4(self):
        isprime = ch_36_2.is_prime(4)
        self.assertEqual(isprime, False)

    def test_prime_10000(self):
        isprime = ch_36_2.is_prime(10000)
        self.assertEqual(isprime, False)


class TestAbs(unittest.TestCase):
    def test_abs_5(self):
        absolute = ch_36_2.absolute_value(5)
        self.assertEqual(absolute, 5)

    def test_abs_neg5(self):
        absolute = ch_36_2.absolute_value(-5)
        self.assertEqual(absolute, 5)

    def test_abs_0(self):
        absolute = ch_36_2.absolute_value(0)
        self.assertEqual(absolute, 0)


unittest.main()
