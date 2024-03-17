

# # def calculate_average_velocity(previous_sprint_points):
# #     total_points_completed = sum(previous_sprint_points)
# #     num_previous_sprints = len(previous_sprint_points)
# #     average_velocity = total_points_completed / num_previous_sprints
# #     return average_velocity

# def calculate_effort_hour_capacity(num_sprint_days, team_member_details):
#     total_effort_hours = 0
#     for member_details in team_member_details:
#         days_off = member_details['days_off']
#         hours_committed_to_ceremonies = member_details['hours_committed_to_ceremonies']
#         min_hours_per_day, max_hours_per_day = member_details['available_hours_per_day_range']
        
#         total_available_hours_per_day = (min_hours_per_day + max_hours_per_day) / 2  # Taking average of the range
#         available_days = num_sprint_days - days_off - hours_committed_to_ceremonies
#         if available_days < 0:
#             available_days = 0  # Ensure available days is not negative
#         total_effort_hours += available_days * total_available_hours_per_day
    
#     return total_effort_hours, total_effort_hours / len(team_member_details)

# def get_team_member_details(num_team_members):
#     team_member_details = []
#     for i in range(num_team_members):
#         member_name = input(f"Enter name of team member {i+1}: ")
#         days_off = int(input(f"Enter days off for {member_name}: "))
#         hours_committed_to_ceremonies = int(input(f"Enter hours committed to ceremonies for {member_name}: "))
#         min_hours_per_day = int(input(f"Enter minimum hours available per day for {member_name}: "))
#         max_hours_per_day = int(input(f"Enter maximum hours available per day for {member_name}: "))
        
#         member_details = {
#             'name': member_name,
#             'days_off': days_off,
#             'hours_committed_to_ceremonies': hours_committed_to_ceremonies,
#             'available_hours_per_day_range': (min_hours_per_day, max_hours_per_day)
#         }
#         team_member_details.append(member_details)
#     return team_member_details

# def main():
#     print("Choose an option:")
#     print("1. Calculate Average Velocity")
#     print("2. Calculate Effort Hour Capacity")
#     choice = input("Enter your choice (1 or 2): ")

#     if choice == '1':
#         num_previous_sprints = int(input("Enter the number of previous sprints: "))
#         previous_sprint_points = []
#         for i in range(num_previous_sprints):
#             points_completed = int(input(f"Enter points completed for sprint {i+1}: "))
#             previous_sprint_points.append(points_completed)
#         average_velocity = calculate_average_velocity(previous_sprint_points)
#         print("Average Velocity:", average_velocity)
#     elif choice == '2':
#         num_sprint_days = int(input("Enter number of sprint days: "))
#         num_team_members = int(input("Enter number of team members: "))
#         team_member_details = get_team_member_details(num_team_members)
#         team_effort_hours, avg_effort_hours_per_person = calculate_effort_hour_capacity(num_sprint_days, team_member_details)
#         print("Total Team Effort Hours:", team_effort_hours)
#         print("Average Available Effort-Hours/Person:", avg_effort_hours_per_person)
#     else:
#         print("Invalid choice")

# if __name__ == "__main__":
#     main()




# def calculate_average_velocity(previous_sprint_points):
#     if not previous_sprint_points:
#         return 0  # Return 0 if the list is empty to avoid division by zero
#     total_points_completed = sum(previous_sprint_points)
#     num_previous_sprints = len(previous_sprint_points)
#     average_velocity = total_points_completed / num_previous_sprints
#     return average_velocity



def calculate_average_velocity(previous_sprint_points):
    if not previous_sprint_points:
        return 0  # Return 0 if the list is empty to avoid division by zero
    total_points_completed = sum(previous_sprint_points)
    num_previous_sprints = len(previous_sprint_points)
    average_velocity = total_points_completed / num_previous_sprints
    return average_velocity


def calculate_effort_hour_capacity(num_sprint_days, team_member_details):
    total_effort_hours = 0
    if team_member_details:  # Check if team_member_details is not empty
        for member_details in team_member_details:
            days_off = member_details['days_off']
            hours_committed_to_ceremonies = member_details['hours_committed_to_ceremonies']
            min_hours_per_day, max_hours_per_day = member_details['available_hours_per_day_range']
            
            total_available_hours_per_day = (min_hours_per_day + max_hours_per_day) / 2  # Taking average of the range
            available_days = num_sprint_days - days_off - hours_committed_to_ceremonies
            if available_days < 0:
                available_days = 0  # Ensure available days is not negative
            total_effort_hours += available_days * total_available_hours_per_day
    
    avg_effort_hours_per_person = total_effort_hours / len(team_member_details) if team_member_details else 0  # Handle division by zero
    return total_effort_hours, avg_effort_hours_per_person


def get_team_member_details(num_team_members):
    team_member_details = []
    for i in range(num_team_members):
        member_name = input(f"Enter name of team member {i+1}: ")
        days_off = int(input(f"Enter days off for {member_name}: "))
        hours_committed_to_ceremonies = int(input(f"Enter hours committed to ceremonies for {member_name}: "))
        min_hours_per_day = int(input(f"Enter minimum hours available per day for {member_name}: "))
        max_hours_per_day = int(input(f"Enter maximum hours available per day for {member_name}: "))
        
        member_details = {
            'name': member_name,
            'days_off': days_off,
            'hours_committed_to_ceremonies': hours_committed_to_ceremonies,
            'available_hours_per_day_range': (min_hours_per_day, max_hours_per_day)
        }
        team_member_details.append(member_details)
    return team_member_details

def main():
    print("Choose an option:")
    print("1. Calculate Average Velocity")
    print("2. Calculate Effort Hour Capacity")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        num_previous_sprints = int(input("Enter the number of previous sprints: "))
        previous_sprint_points = []
        for i in range(num_previous_sprints):
            points_completed = int(input(f"Enter points completed for sprint {i+1}: "))
            previous_sprint_points.append(points_completed)
        average_velocity = calculate_average_velocity(previous_sprint_points)
        print("Average Velocity:", average_velocity)
    elif choice == '2':
        num_sprint_days = int(input("Enter number of sprint days: "))
        num_team_members = int(input("Enter number of team members: "))
        team_member_details = get_team_member_details(num_team_members)
        team_effort_hours, avg_effort_hours_per_person = calculate_effort_hour_capacity(num_sprint_days, team_member_details)
        print("Total Team Effort Hours:", team_effort_hours)
        print("Average Available Effort-Hours/Person:", avg_effort_hours_per_person)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
