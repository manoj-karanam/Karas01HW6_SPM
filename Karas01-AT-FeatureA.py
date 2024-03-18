import unittest
from FinalSolution import calculate_average_velocity

class TestFeatureAAcceptance(unittest.TestCase):
    def test_happy_path(self):
        # Test with non-empty previous_sprint_points
        previous_sprint_points = [10, 20, 30]
        average_velocity = calculate_average_velocity(previous_sprint_points)
        self.assertEqual(average_velocity, 20)  # Expected average velocity for the given points

    def test_empty_input(self):
        # Test with empty previous_sprint_points
        previous_sprint_points = []
        average_velocity = calculate_average_velocity(previous_sprint_points)
        self.assertEqual(average_velocity, 0)  # Expected average velocity should be 0 for empty points list

    def test_happy_path_and_empty_input(self):
        # Test with a combination of non-empty and empty previous_sprint_points
        previous_sprint_points = [10, 20, 30]
        average_velocity = calculate_average_velocity(previous_sprint_points)
        self.assertEqual(average_velocity, 20)  # Expected average velocity for the given points

        previous_sprint_points = []
        average_velocity = calculate_average_velocity(previous_sprint_points)
        self.assertEqual(average_velocity, 0)  # Expected average velocity should be 0 for empty points list


if __name__ == '__main__':
    unittest.main()
