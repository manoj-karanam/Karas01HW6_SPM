import unittest
from FinalSolution import calculate_effort_hour_capacity, get_team_member_details

class TestFeatureBAcceptance(unittest.TestCase):
    def test_happy_path(self):
        # Test with sample team member details
        num_sprint_days = 10
        team_member_details = [
            {'days_off': 1, 'hours_committed_to_ceremonies': 2, 'available_hours_per_day_range': (6, 8)},
            {'days_off': 0, 'hours_committed_to_ceremonies': 1, 'available_hours_per_day_range': (7, 9)}
        ]
        total_hours, avg_hours_per_person = calculate_effort_hour_capacity(num_sprint_days, team_member_details)
        self.assertAlmostEqual(total_hours, 121.0)  # Adjusted expected total effort hours

    def test_empty_input(self):
        # Test with empty team member details
        num_sprint_days = 10
        team_member_details = []
        total_hours, avg_hours_per_person = calculate_effort_hour_capacity(num_sprint_days, team_member_details)
        self.assertEqual(total_hours, 0)  # Expected total effort hours should be 0 for empty team

    def test_happy_path_and_empty_input(self):
        # Test with a combination of sample team member details and empty team member details
        num_sprint_days = 10
        team_member_details = [
            {'days_off': 1, 'hours_committed_to_ceremonies': 2, 'available_hours_per_day_range': (6, 8)},
            {'days_off': 0, 'hours_committed_to_ceremonies': 1, 'available_hours_per_day_range': (7, 9)}
        ]
        total_hours, avg_hours_per_person = calculate_effort_hour_capacity(num_sprint_days, team_member_details)
        self.assertAlmostEqual(total_hours, 121.0)  # Adjusted expected total effort hours

        num_sprint_days = 10
        team_member_details = []
        total_hours, avg_hours_per_person = calculate_effort_hour_capacity(num_sprint_days, team_member_details)
        self.assertEqual(total_hours, 0)  # Expected total effort hours should be 0 for empty team



if __name__ == '__main__':
    unittest.main()
