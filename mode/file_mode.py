from commands import command_executor_factory
from entity.command import Command
from mode.mode import Mode


class FileMode(Mode):
    def __init__(self, output_printer, command_executor_factory, active_subscription_plan_service, file_name):
        self.output_printer = output_printer
        self.command_executor_factory = command_executor_factory
        self.active_subscription_plan_service = active_subscription_plan_service
        self.file_name = file_name

    def process(self):
        try:
            with open(self.file_name) as file:
                for line in file.readlines():
                    processed_line = line.strip()
                    command = Command(processed_line)
                    self.__process_command(command)

        except IOError:
            self.output_printer.invalid_file()

    def __process_command(self, command):
        command_executor = self.command_executor_factory.get_command_executor(command)
        if command_executor.validate(command):
            command_executor.execute(command)
