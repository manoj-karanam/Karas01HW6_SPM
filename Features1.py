def calculate_average_velocity(previous_sprint_points):
    total_points_completed = sum(previous_sprint_points)
    num_previous_sprints = len(previous_sprint_points)
    average_velocity = total_points_completed / num_previous_sprints
    return average_velocity

def main():
    num_previous_sprints = int(input("Enter the number of previous sprints: "))
    previous_sprint_points = []
    for i in range(num_previous_sprints):
        points_completed = int(input(f"Enter points completed for sprint {i+1}: "))
        previous_sprint_points.append(points_completed)
    average_velocity = calculate_average_velocity(previous_sprint_points)
    print("Average Velocity:", average_velocity)    

if __name__ == "__main__":
    main()






