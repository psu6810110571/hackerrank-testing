import unittest
from hackerrank.two_characters import alternate

class TestTwoCharacters(unittest.TestCase):
    
    def test_alternate_with_beabeefeab_should_return_5(self):
        # Arrange
        s = "beabeefeab"
        expected_output = 5
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_alternate_with_abaacdabd_should_return_4(self):
        # Arrange
        s = "abaacdabd"
        expected_output = 4
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_alternate_with_ab_should_return_2(self):
        # Arrange
        s = "ab"
        expected_output = 2
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_alternate_with_aa_should_return_0(self):
        # Arrange
        s = "aa"
        expected_output = 0
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_alternate_with_single_character_should_return_0(self):
        # Arrange
        # Edge Case: มีตัวอักษรเดียว ไม่สามารถสร้าง alternating string ได้ ต้องตอบ 0
        s = "a"
        expected_output = 0
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, expected_output)