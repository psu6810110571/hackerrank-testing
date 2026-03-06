import unittest
from coe_number.number_utils import is_prime_list

class PrimeListTest(unittest.TestCase):
    
    def test_give_2_3_5_is_prime(self):
        # Arrange
        prime_list = [2, 3, 5]
        
        # Act
        is_prime = is_prime_list(prime_list)
        
        # Assert
        self.assertTrue(is_prime)

    def test_give_empty_list_should_return_false(self):
        # Arrange: กรณีลิสต์ไม่มีข้อมูลเลย
        prime_list = []
        
        # Act
        is_prime = is_prime_list(prime_list)
        
        # Assert: ต้องได้ผลลัพธ์เป็น False
        self.assertFalse(is_prime)

    def test_give_4_6_8_should_return_false(self):
        # Arrange: กรณีตัวเลขไม่ใช่จำนวนเฉพาะทั้งหมด
        prime_list = [4, 6, 8]
        
        # Act
        is_prime = is_prime_list(prime_list)
        
        # Assert: ต้องได้ผลลัพธ์เป็น False
        self.assertFalse(is_prime)

    def test_give_negative_numbers_should_return_false(self):
        # Arrange: กรณีเป็นเลขติดลบทั้งหมด
        prime_list = [-1, -2, -3]
        
        # Act
        is_prime = is_prime_list(prime_list)
        
        # Assert: ต้องได้ผลลัพธ์เป็น False
        self.assertFalse(is_prime)