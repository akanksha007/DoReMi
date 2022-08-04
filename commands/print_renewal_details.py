import utils.util
from commands.command_executor import CommandExecutor
from entity.category import Category
from entity.plan_name import PlanName


class PrintRenewalDetails(CommandExecutor):
    COMMAND_NAME = "PRINT_RENEWAL_DETAILS"

    def validate(self, command):
        categories = self._active_subscription_plan_service.get_subscription()
        if not categories:
            self._output_printer.subscription_not_found()
            return False
        else:
            return True

    def execute(self, command):
        active_subscriptions = self._active_subscription_plan_service.get_subscription()
        topup_plan = self._active_subscription_plan_service.get_topup()
        topup_months = self._active_subscription_plan_service.get_topup_months()
        subscription_start_date = self._active_subscription_plan_service.get_date()
        renewal_amount = 0

        for category, plan_name in active_subscriptions.items():
            plan = self.__fetch_duration_for_active_subscription(category, plan_name)
            duration_unit, duration_count, plan_amount = plan.duration_unit, plan.duration_count, plan.amount
            date = utils.util.get_renewal_date(subscription_start_date, duration_unit, duration_count)
            renewal_amount += plan_amount
            self._output_printer.print_renewal_details(category + " " + str(date))
        renewal_amount += self.__get_topup_renewal_amount(topup_plan, topup_months)
        self._output_printer.print_renewal_amount(int(renewal_amount))

    def __fetch_duration_for_active_subscription(self, category, plan_name):
        category, plan_name = Category[category], PlanName[plan_name]
        subscription_plan = self._subscription_plan_service.get_subscription_by_category_and_plan_type(category,
                                                                                                       plan_name)
        return subscription_plan

    def __get_topup_renewal_amount(self, topup_plan, topup_months):
        return topup_plan.amount * utils.util.get_topup_months(topup_plan, topup_months)

    def __init__(self, subscription_plan_service, output_printer, active_subscription_plan_service):
        self._subscription_plan_service = subscription_plan_service
        self._output_printer = output_printer
        self._active_subscription_plan_service = active_subscription_plan_service
