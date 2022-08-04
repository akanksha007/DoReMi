import utils.util
from commands.command_executor import CommandExecutor


class AddSubscription(CommandExecutor):
    COMMAND_NAME = "ADD_SUBSCRIPTION"
    INVALID_DATE = "INVALID_DATE"
    DUPLICATE_CATEGORY = "DUPLICATE_CATEGORY"

    def validate(self, command):
        date = self._active_subscription_plan_service.get_date()
        categories = self._active_subscription_plan_service.get_subscription()
        category, plan_type = command.params
        if utils.util.subscription_date_not_set(date):
            self._output_printer.add_subscription_failed(AddSubscription.INVALID_DATE)
            return False
        elif utils.util.category_already_subscribed(categories, category):
            self._output_printer.add_subscription_failed(AddSubscription.DUPLICATE_CATEGORY)
            return False
        else:
            return True

    def execute(self, command):
        self._active_subscription_plan_service.set_subscription(command)

    def __init__(self, subscription_plan_service, output_printer, active_subscription_plan_service):
        self._subscription_plan_service = subscription_plan_service
        self._output_printer = output_printer
        self._active_subscription_plan_service = active_subscription_plan_service
