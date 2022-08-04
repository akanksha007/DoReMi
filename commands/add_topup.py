import utils.util
from commands.command_executor import CommandExecutor


class AddTopup(CommandExecutor):
    COMMAND_NAME = "ADD_TOPUP"
    SUBSCRIPTIONS_NOT_FOUND = "SUBSCRIPTIONS_NOT_FOUND"
    DUPLICATE_TOPUP = "DUPLICATE_TOPUP"

    def validate(self, command):
        date = self._active_subscription_plan_service.get_date()
        plan_type = self._active_subscription_plan_service.get_subscription()
        current_topup = self._active_subscription_plan_service.get_topup()

        if utils.util.subscription_date_not_set(date) or (not bool(plan_type)):
            self._output_printer.add_topup_failed(AddTopup.SUBSCRIPTIONS_NOT_FOUND)
            return False
        elif bool(current_topup):
            self._output_printer.add_topup_failed(AddTopup.DUPLICATE_TOPUP)
            return False
        else:
            return True

    def execute(self, command):
        all_top_up_plans = self._topup_service.get_topup_plan()
        name, months = command.params
        self._active_subscription_plan_service.set_topup(command,all_top_up_plans[name])

    def __init__(self, subscription_plan_service, output_printer, active_subscription_plan_service, topup_service):
        self._subscription_plan_service = subscription_plan_service
        self._output_printer = output_printer
        self._active_subscription_plan_service = active_subscription_plan_service
        self._topup_service = topup_service
