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

    def test_give_3_with_star_should_return_staircase(self):
        # Arrange: กรณีเปลี่ยนสัญลักษณ์เป็นตัวอื่น (เช่น *)
        n = 3
        pattern = '*'
        expected_output = \
        "  *\n" + \
        " **\n" + \
        "***"
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_0_should_return_empty_string(self):
        # Arrange: กรณี n=0 ซึ่งไม่อยู่ในเงื่อนไข 0 < n <= 30
        n = 0
        pattern = '#'
        expected_output = ""
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_31_should_return_empty_string(self):
        # Arrange: กรณี n=31 ซึ่งเกินขอบเขต 0 < n <= 30
        n = 31
        pattern = '#'
        expected_output = ""
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output)