import unittest
from fizzbuzz.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    
    def test_give_3_should_return_fizz(self):
        # Arrange
        x = 3
        
        # Act
        result = fizzbuzz(x)
        
        # Assert
        self.assertEqual(result, "Fizz")

    def test_give_5_should_return_buzz(self):
        # Arrange
        # กรณีหาร 5 ลงตัว
        x = 5
        
        # Act
        result = fizzbuzz(x)
        
        # Assert
        self.assertEqual(result, "Buzz")

    def test_give_15_should_return_fizzbuzz(self):
        # Arrange
        # กรณีหารลงตัวทั้ง 3 และ 5 (เช่น 15)
        x = 15
        
        # Act
        result = fizzbuzz(x)
        
        # Assert
        self.assertEqual(result, "FizzBuzz")