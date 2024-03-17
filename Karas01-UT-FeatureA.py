# import unittest

# from FinalSolution import calculate_average_velocity

# class TestCalculateAverageVelocity(unittest.TestCase):
#     def test_calculate_average_velocity(self):
#         # Test case with non-empty list
#         result = calculate_average_velocity([10, 20, 30])
#         self.assertEqual(result, 20)  # Average of 10, 20, 30 is 20
        
#         # Test case with empty list
#         result = calculate_average_velocity([])
#         self.assertEqual(result, 0)  # Empty list should return 0

# if __name__ == '__main__':
#     unittest.main()


import unittest
from FinalSolution import calculate_average_velocity

class TestCalculateAverageVelocity(unittest.TestCase):
    def test_calculate_average_velocity_happy_path(self):
        # Test case with non-empty list
        result = calculate_average_velocity([10, 20, 30])
        self.assertEqual(result, 20)  # Average of 10, 20, 30 is 20
        
    def test_calculate_average_velocity_empty_list(self):
        # Test case with empty list
        result = calculate_average_velocity([])
        self.assertEqual(result, 0)  # Empty list should return 0

    def test_calculate_average_velocity_unhappy_path(self):
        # Test case with negative points
        result = calculate_average_velocity([-10, 20, 30])
        self.assertEqual(result, 13.333333333333334)  # Expected average for negative points

if __name__ == '__main__':
    unittest.main()