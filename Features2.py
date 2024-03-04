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

# Calculate effort hour capacity
team_effort_hours, avg_effort_hours_per_person = calculate_effort_hour_capacity(num_sprint_days, team_member_details)

# Output
print("Total Team Effort Hours:", team_effort_hours)
print("Average Available Effort-Hours/Person:", avg_effort_hours_per_person)