import unittest
from unittest.mock import patch
from test_double.guess_number import guess_number

class TestGuessNumber(unittest.TestCase):
    
    # ใช้ patch เพื่อล็อกผลลัพธ์ของฟังก์ชัน random.randint
    @patch('test_double.guess_number.random.randint')
    def test_guess_correct_should_return_you_win(self, mock_randint):
        # Arrange: ล็อกผลการสุ่มให้เป็นเลข 5 เสมอ
        mock_randint.return_value = 5
        guess = 5 # เราทายเลข 5 (ตรงกับที่ล็อกไว้)
        
        # Act
        result = guess_number(guess)
        
        # Assert: ทายถูก ต้องได้คำว่า "You win"
        self.assertEqual(result, "You win")