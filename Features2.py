def calculate_effort_hour_capacity(num_sprint_days, team_member_details):
    total_effort_hours = 0
    for member_details in team_member_details:
        days_off = member_details['days_off']
        hours_committed_to_ceremonies = member_details['hours_committed_to_ceremonies']
        min_hours_per_day, max_hours_per_day = member_details['available_hours_per_day_range']
        
        total_available_hours_per_day = (min_hours_per_day + max_hours_per_day) / 2  # Taking average of the range
        available_days = num_sprint_days - days_off - hours_committed_to_ceremonies
        if available_days < 0:
            available_days = 0  # Ensure available days is not negative
        total_effort_hours += available_days * total_available_hours_per_day
    
    return total_effort_hours, total_effort_hours / len(team_member_details)

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

# Input from user
num_sprint_days = int(input("Enter number of sprint days: "))
num_team_members = int(input("Enter number of team members: "))
team_member_details = get_team_member_details(num_team_members)

# Calculate effort hour capacity
team_effort_hours, avg_effort_hours_per_person = calculate_effort_hour_capacity(num_sprint_days, team_member_details)

# Output
print("Total Team Effort Hours:", team_effort_hours)
print("Average Available Effort-Hours/Person:", avg_effort_hours_per_person)
=======
