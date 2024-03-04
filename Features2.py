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
