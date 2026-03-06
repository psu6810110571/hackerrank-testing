import unittest
from coe_number.number_utils import is_prime_list

class PrimeListTest(unittest.TestCase):
    
    def test_give_2_3_5_is_prime(self):
        # Arrange
        prime_list = [2, 3, 5]
        
        # Act
        is_prime = is_prime_list(prime_list)
        
        # Assert
        self.assertTrue(is_prime)