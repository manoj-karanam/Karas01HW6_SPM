from FinalSolution import calculate_average_velocity

def test_feature_a_acceptance():
    # Happy Path: Calculate average velocity for previous sprints
    sprint_points = [8, 12, 15, 20]
    expected_average_velocity = 13.75  # (8 + 12 + 15 + 20) / 4
    assert calculate_average_velocity(sprint_points) == expected_average_velocity

    # Unhappy Path: Empty List
    empty_sprint_points = []
    assert calculate_average_velocity(empty_sprint_points) == 0

    # Unhappy Path: Negative Points
    negative_sprint_points = [-10, 20, -30]
    expected_average_velocity = 0  # Excluding negative points, average is 0
    actual_average_velocity = calculate_average_velocity(negative_sprint_points)
    print("Actual Average Velocity for Negative Sprint Points:", actual_average_velocity)
    print("Expected Average Velocity for Negative Sprint Points:", expected_average_velocity)

    # Unhappy Path: Zero Points
    zero_sprint_points = [0, 0, 0]
    assert calculate_average_velocity(zero_sprint_points) == 0

if __name__ == '__main__':
    test_feature_a_acceptance()
