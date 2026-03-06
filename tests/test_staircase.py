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

    def test_give_4_with_hash_should_return_staircase(self):
        # Arrange: กรณีบันได 4 ขั้น ตามสไลด์หน้า 13
        n = 4
        pattern = '#'
        expected_output = \
        "   #\n" + \
        "  ##\n" + \
        " ###\n" + \
        "####"
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output)