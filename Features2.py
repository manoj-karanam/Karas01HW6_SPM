class TeamMember:
    def __init__(self, hours_off=0, hours_committed=0, available_hours=(6, 8)):
        self.hours_off = hours_off
        self.hours_committed = hours_committed
        self.available_hours = available_hours

    def calculate_available_hours(self, sprint_days):
        """
        Calculate available effort-hours for the team member.
        :param sprint_days: Number of sprint days
        :return: Available effort-hours for the team member

        """
        daily_hours_min, daily_hours_max = self.available_hours
        total_available_hours = (sprint_days - self.hours_off) * (daily_hours_max - self.hours_committed)
        return total_available_hours