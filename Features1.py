def main():
    num_previous_sprints = int(input("Enter the number of previous sprints: "))
    previous_sprint_points = []
    for i in range(num_previous_sprints):
        points_completed = int(input(f"Enter points completed for sprint {i+1}: "))
        previous_sprint_points.append(points_completed)

if __name__ == "__main__":
    main()






