import utils.util
from commands.command_executor import CommandExecutor


class StartSubscription(CommandExecutor):
    COMMAND_NAME = "START_SUBSCRIPTION"

    def validate(self, command):
        if utils.util.validate_date(self.__fetch_date(command)):
            return True
        else:
            self._output_printer.invalid_date()
            return False

    def execute(self, command):
        self._active_subscription_plan_service.set_date(self.__fetch_date(command))

    def __init__(self, subscription_plan_service, output_printer, active_subscription_plan_service):
        self._subscription_plan_service = subscription_plan_service
        self._output_printer = output_printer
        self._active_subscription_plan_service = active_subscription_plan_service

    def __fetch_date(self, command):
        return next(iter(command.params), None)
