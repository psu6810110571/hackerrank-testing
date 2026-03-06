import unittest
from staircase.staircase import staircase

class TestStaircase(unittest.TestCase):
    
    def test_give_2_with_hash_should_be_hh(self):
        # Arrange
        n = 2
        pattern = '#'
        expected_output = \
        " #\n" + \
        "##"
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')