from commands.command_executor_factory import CommandExecutorFactory
from mode.file_mode import FileMode
from printer.output_printer import OutputPrinter
from service.active_subscription_plan_service import ActiveSubscriptionPlanService
from service.subscription_plan_service import SubscriptionPlanService
import sys


def main():
    # subscription_plan_service, output_printer, active_subscription_plan_service
    subscription_plan_service = SubscriptionPlanService()
    output_printer = OutputPrinter()
    active_subscription_plan_service = ActiveSubscriptionPlanService()
    command_executor_factory = CommandExecutorFactory(subscription_plan_service, output_printer,
                                                      active_subscription_plan_service)
    file_name = sys.argv[-1]
    FileMode(output_printer, command_executor_factory, active_subscription_plan_service, file_name).process()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
