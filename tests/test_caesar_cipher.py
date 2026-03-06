import unittest
from hackerrank.caesar_cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):
    
    def test_caesar_cipher_with_middle_Outz_and_k2_should_return_okffng_Qwvb(self):
        # Arrange
        s = "middle-Outz"
        k = 2
        expected_output = "okffng-Qwvb"
        
        # Act
        result = caesarCipher(s, k)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_caesar_cipher_with_xyz_and_k3_should_return_abc(self):
        # Arrange
        s = "xyz"
        k = 3
        expected_output = "abc"
        
        # Act
        result = caesarCipher(s, k)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_caesar_cipher_with_large_k_should_wrap_correctly(self):
        # Arrange
        # เลื่อนไป 28 ตำแหน่ง มีค่าเท่ากับเลื่อน 2 ตำแหน่ง (28 % 26 = 2)
        s = "Hello-World!"
        k = 28 
        expected_output = "Jgnnq-Yqtnf!"
        
        # Act
        result = caesarCipher(s, k)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_caesar_cipher_with_k_zero_should_return_same_string(self):
        # Arrange
        # Edge Case: ไม่มีการเลื่อน (k=0) ค่าที่ได้ต้องเหมือนเดิม
        s = "abc"
        k = 0
        expected_output = "abc"
        
        # Act
        result = caesarCipher(s, k)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_caesar_cipher_with_symbols_only_should_return_same_symbols(self):
        # Arrange
        # Edge Case: มีแต่เครื่องหมายพิเศษ ล้วนๆ ต้องไม่ถูกเลื่อน
        s = "!@#$%"
        k = 5
        expected_output = "!@#$%"
        
        # Act
        result = caesarCipher(s, k)
        
        # Assert
        self.assertEqual(result, expected_output)