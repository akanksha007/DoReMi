from commands.add_subscription import AddSubscription
from commands.add_topup import AddTopup
from commands.print_renewal_details import PrintRenewalDetails
from commands.start_subscription import StartSubscription


class CommandExecutorFactory:

    def __init__(self, subscription_plan_service, output_printer, active_subscription_plan_service, topup_service):
        self._subscription_plan_service = subscription_plan_service
        self._output_printer = output_printer
        self.active_subscription_plan_service = active_subscription_plan_service
        self.command_mapping = {
            StartSubscription.COMMAND_NAME: StartSubscription(subscription_plan_service,
                                                              output_printer, active_subscription_plan_service),
            AddSubscription.COMMAND_NAME: AddSubscription(subscription_plan_service,
                                                          output_printer, active_subscription_plan_service),
            PrintRenewalDetails.COMMAND_NAME: PrintRenewalDetails(subscription_plan_service,
                                                                  output_printer, active_subscription_plan_service),
            AddTopup.COMMAND_NAME: AddTopup(subscription_plan_service,
                                            output_printer, active_subscription_plan_service, topup_service)}

    def get_command_executor(self, command):
        return self.command_mapping[command.name]

