import unittest
from cat_and_mouse.cat_and_mouse import cat_and_mouse

class TestCatAndMouse(unittest.TestCase):
    
    def test_cat_b_catches_mouse(self):
        # Arrange: ตามสไลด์หน้า 21 (x=1, y=2, z=3)
        x = 1
        y = 2
        z = 3
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert: Cat B (ที่ตำแหน่ง 2) ใกล้หนู C (ตำแหน่ง 3) มากกว่า 
        # จึงต้องคืนค่า "Cat B"
        self.assertEqual(result, "Cat B")