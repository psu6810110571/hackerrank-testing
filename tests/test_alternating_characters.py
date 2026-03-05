import unittest
from hackerrank.alternating_characters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):
    
    def test_alternating_characters_with_AAAA_should_return_3(self):
        # Arrange
        s = "AAAA"
        expected_output = 3
        
        # Act
        result = alternatingCharacters(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_alternating_characters_with_ABABABAB_should_return_0(self):
        # Arrange
        s = "ABABABAB"
        expected_output = 0
        
        # Act
        result = alternatingCharacters(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_alternating_characters_with_AAABBB_should_return_4(self):
        # Arrange
        s = "AAABBB"
        expected_output = 4
        
        # Act
        result = alternatingCharacters(s)
        
        # Assert
        self.assertEqual(result, expected_output)