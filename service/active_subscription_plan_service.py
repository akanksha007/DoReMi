from utils.util import fetch_date_from_date_string


class ActiveSubscriptionPlanService:
    def __init__(self):
        self.date = None
        self.active_subscription = {}

    def set_date(self, command):
        self.date = fetch_date_from_date_string(command.params)

