import unittest
from bmw_prime import isPrime
from bmw_prime import printPrime


class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(isPrime(5))

    def test_is_four_non_prime(self):
	    """Is four correctly determined not to be prime?"""
	    self.assertFalse(isPrime(4), msg='Four is not prime!')   

    def test_is_zero_not_prime(self):
	    """Is zero correctly determined not to be prime?"""
	    self.assertFalse(isPrime(0))

    # def test_negative_number(self):
	   #  """Is a negative number correctly determined not to be prime?"""
	   #  self.assertFalse(isPrime(-1))
	   #  self.assertFalse(isPrime(-2))
	   #  self.assertFalse(isPrime(-3))
	   #  self.assertFalse(isPrime(-4))
	   #  self.assertFalse(isPrime(-5))
	   #  self.assertFalse(isPrime(-6))
	   #  self.assertFalse(isPrime(-7))
	   #  self.assertFalse(isPrime(-8))
	   #  self.assertFalse(isPrime(-9))			
	


if __name__ == '__main__':
    unittest.main()