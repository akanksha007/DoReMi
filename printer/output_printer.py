class OutputPrinter:
    def invalid_file(self):
        self.__print_with_new_line("Invalid file provided")

    def invalid_date(self):
        self.__print_with_new_line("INVALID_DATE")

    def add_subscription_failed(self):
        self.__print_with_new_line("ADD_SUBSCRIPTION_FAILED")

    def duplicate_category(self):
        self.__print_with_new_line("DUPLICATE_CATEGORY")

    def subscription_not_found(self):
        self.__print_with_new_line("SUBSCRIPTIONS_NOT_FOUND")

    def print_renewal_details(self, message):
        self.__print_with_new_line("RENEWAL_REMINDER" + " " + message)

    def print_renewal_amount(self, renewal_amount):
        self.__print_with_new_line("RENEWAL_AMOUNT" + " " + str(renewal_amount))

    def __print_with_new_line(self, message):
        print(message)
