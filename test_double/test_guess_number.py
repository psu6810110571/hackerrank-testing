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

    @patch('test_double.guess_number.random.randint')
    def test_guess_too_low_should_return_too_low(self, mock_randint):
        # Arrange: ล็อกผลการสุ่มให้เป็นเลข 5 เสมอ
        mock_randint.return_value = 5
        guess = 3 # เราทายเลข 3 ซึ่งน้อยกว่าเลขที่สุ่มได้
        
        # Act
        result = guess_number(guess)
        
        # Assert: ทายน้อยไป ต้องได้คำว่า "Too low"
        self.assertEqual(result, "Too low")

    @patch('test_double.guess_number.random.randint')
    def test_guess_too_high_should_return_too_high(self, mock_randint):
        # Arrange: ล็อกผลการสุ่มให้เป็นเลข 5 เสมอ
        mock_randint.return_value = 5
        guess = 8 # เราทายเลข 8 ซึ่งมากกว่าเลขที่สุ่มได้
        
        # Act
        result = guess_number(guess)
        
        # Assert: ทายมากไป ต้องได้คำว่า "Too high"
        self.assertEqual(result, "Too high")

    @patch('test_double.guess_number.random.randint')
    def test_guess_boundary_low_correct_should_return_you_win(self, mock_randint):
        # Arrange: ล็อกผลการสุ่มให้เป็นเลข 1 (ขอบเขตล่างสุด)
        mock_randint.return_value = 1
        guess = 1 
        
        # Act
        result = guess_number(guess)
        
        # Assert: ทายถูกที่ขอบเขตล่างสุด
        self.assertEqual(result, "You win")