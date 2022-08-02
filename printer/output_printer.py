class OutputPrinter:
    def invalid_file(self):
        self.__print_with_new_line("Invalid file provided")

    def invalid_date(self):
        self.__print_with_new_line("INVALID_DATE")

    def __print_with_new_line(self, message):
        print(message)
