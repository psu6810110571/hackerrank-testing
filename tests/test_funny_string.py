import unittest
from hackerrank.funny_string import funnyString

class TestFunnyString(unittest.TestCase):
    
    def test_funny_string_with_acxz_should_return_funny(self):
        # Arrange
        s = "acxz"
        expected_output = "Funny"
        
        # Act
        result = funnyString(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_funny_string_with_bcxz_should_return_not_funny(self):
        # Arrange
        s = "bcxz"
        expected_output = "Not Funny"
        
        # Act
        result = funnyString(s)
        
        # Assert
        self.assertEqual(result, expected_output)