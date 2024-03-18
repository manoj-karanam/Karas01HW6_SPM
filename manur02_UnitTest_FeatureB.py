import unittest
from FinalSolution import calculate_effort_hour_capacity

class TestFeatureBMethod(unittest.TestCase):
    def test_calculate_effort_hour_capacity_empty_team(self):
        self.assertEqual(calculate_effort_hour_capacity(10, []), (0, 0))

    def test_calculate_effort_hour_capacity_with_team_members(self):
        team_members = [
            {
                'days_off': 1,
                'hours_committed_to_ceremonies': 2,
                'available_hours_per_day_range': (6, 8)
            },
            {
                'days_off': 2,
                'hours_committed_to_ceremonies': 1,
                'available_hours_per_day_range': (7, 9)
            }
        ]
        total_hours, avg_hours_per_person = calculate_effort_hour_capacity(10, team_members)
        expected_total_hours = 105.0  # Adjusted calculation for total hours for two team members
        self.assertEqual(total_hours, expected_total_hours)
        self.assertEqual(avg_hours_per_person, 52.5)  # (180 / 2)



    def test_calculate_effort_hour_capacity_with_zero_days(self):
        team_members = [
            {
                'days_off': 1,
                'hours_committed_to_ceremonies': 2,
                'available_hours_per_day_range': (6, 8)
            }
        ]
        self.assertEqual(calculate_effort_hour_capacity(0, team_members), (0, 0))

    def test_calculate_effort_hour_capacity_with_negative_days_off(self):
        team_members = [
            {
                'days_off': -1,
                'hours_committed_to_ceremonies': 2,
                'available_hours_per_day_range': (6, 8)
            }
        ]
        total_hours, avg_hours_per_person = calculate_effort_hour_capacity(10, team_members)
        self.assertEqual(total_hours, 63.0)
        self.assertEqual(avg_hours_per_person, 63.0)






if __name__ == '__main__':
    unittest.main()
