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
        self.assertEqual(result, "Cat B")

    def test_mouse_escapes(self):
        # Arrange: ตามสไลด์หน้า 21 (x=1, y=3, z=2)
        # แมวทั้งสองตัวอยู่ห่างจากหนูเท่ากัน (ระยะทาง = 1)
        x = 1
        y = 3
        z = 2
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert: หนูรอด เพราะแมวมาถึงพร้อมกันและตีกันเอง (ต้องคืนค่า "Mouse C")
        self.assertEqual(result, "Mouse C")

    def test_cat_a_catches_mouse(self):
        # Arrange: กำหนดให้แมว A อยู่ใกล้หนูมากกว่าแมว B
        # แมว A อยู่ตำแหน่ง 2, แมว B อยู่ 5, หนูอยู่ 3
        # ระยะห่าง แมว A ถึงหนู = 1, แมว B ถึงหนู = 2
        x = 2
        y = 5
        z = 3
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert: แมว A ใกล้กว่า จึงต้องคืนค่า "Cat A"
        self.assertEqual(result, "Cat A")

    def test_all_at_same_position_should_return_mouse_c(self):
        # Arrange: Edge Case กรณีแมวและหนูอยู่ที่จุดเดียวกันทั้งหมด (x=1, y=1, z=1)
        # ระยะห่างคือ 0 เท่ากัน
        x = 1
        y = 1
        z = 1
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert: แมวถึงพร้อมกัน (ตั้งแต่เริ่ม) หนูต้องรอด
        self.assertEqual(result, "Mouse C")

    def test_negative_positions_should_work_correctly(self):
        # Arrange: Edge Case กรณีตำแหน่งติดลบ
        # แมว A อยู่ -5, แมว B อยู่ -2, หนูอยู่ -4
        # แมว A ห่างหนู 1, แมว B ห่างหนู 2
        x = -5
        y = -2
        z = -4
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert: แมว A ใกล้กว่า (ห่าง 1) ต้องได้ "Cat A"
        self.assertEqual(result, "Cat A")