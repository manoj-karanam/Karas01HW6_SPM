class TeamMember:
    def __init__(self, hours_off=0, hours_committed=0, available_hours=(6, 8)):
        self.hours_off = hours_off
        self.hours_committed = hours_committed
        self.available_hours = available_hours