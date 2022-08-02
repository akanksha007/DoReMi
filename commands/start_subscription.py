import utils.util
from commands.command_executor import CommandExecutor


class StartSubscription(CommandExecutor):
    COMMAND_NAME = "START_SUBSCRIPTION"

    def validate(self, command):
        if utils.util.validate_date(command.params):
            return True
        else:
            self._output_printer.invalid_date()

    def execute(self, command):
        self._active_subscription_plan_service.set_date(command)

    def __init__(self, subscription_plan_service, output_printer, active_subscription_plan_service):
        self._subscription_plan_service = subscription_plan_service
        self._output_printer = output_printer
        self._active_subscription_plan_service = active_subscription_plan_service
