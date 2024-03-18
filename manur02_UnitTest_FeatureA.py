import unittest
from FinalSolution import calculate_average_velocity

class TestFeatureAMethod(unittest.TestCase):
    def test_calculate_average_velocity_empty_list(self):
        self.assertEqual(calculate_average_velocity([]), 0)

    def test_calculate_average_velocity_non_empty_list(self):
        self.assertEqual(calculate_average_velocity([10, 20, 30]), 20)

    def test_calculate_average_velocity_with_negative_points(self):
        self.assertAlmostEqual(calculate_average_velocity([-10, 20, -30]), -6.67, places=2)

    def test_calculate_average_velocity_with_zero_points(self):
        self.assertEqual(calculate_average_velocity([0, 0, 0]), 0)  # Average of 0, 0, and 0

if __name__ == '__main__':
    unittest.main()
