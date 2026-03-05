import unittest
from hackerrank.grid_challenge import gridChallenge

class TestGridChallenge(unittest.TestCase):
    
    def test_grid_challenge_with_sorted_columns_should_return_yes(self):
        # Arrange
        # เราสร้าง "Stub Data" จำลองขึ้นมาเพื่อใช้ทดสอบแทนการรับค่าจากผู้ใช้
        stub_grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expected_output = "YES"
        
        # Act
        result = gridChallenge(stub_grid)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_grid_challenge_with_unsorted_columns_should_return_no(self):
        # Arrange
        # Data Stub สำหรับกรณีที่แนวตั้งเรียงไม่ถูกต้อง
        stub_grid = ['mpxz', 'abcd', 'wlmf']
        expected_output = "NO"
        
        # Act
        result = gridChallenge(stub_grid)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_grid_challenge_with_single_element_should_return_yes(self):
        # Arrange
        # Data Stub สำหรับกรณีตารางมีแค่ตัวเดียว (Edge case)
        stub_grid = ['a']
        expected_output = "YES"
        
        # Act
        result = gridChallenge(stub_grid)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_grid_challenge_with_single_column_multiple_rows_should_return_yes(self):
        # Arrange
        # Edge Case: มีแค่คอลัมน์เดียว เรียงจากบนลงล่างถูกต้อง
        stub_grid = ["a", "b", "c"]
        expected_output = "YES"
        
        # Act
        result = gridChallenge(stub_grid)
        
        # Assert
        self.assertEqual(result, expected_output)