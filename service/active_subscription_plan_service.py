from utils.util import fetch_date_from_date_string


class ActiveSubscriptionPlanService:
    def __init__(self):
        self.date = None
        self.active_subscription = {}

    def set_date(self, date):
        self.date = fetch_date_from_date_string(date)

    def get_date(self):
        return self.date

    def get_subscription(self):
        return self.active_subscription

    def set_subscription(self, command):
        category, plan_type = command.params
        self.active_subscription[category] = plan_type
