from abc import abstractmethod, ABC


class CommandExecutor(ABC):

    @abstractmethod
    def validate(self, command):
        pass

    @abstractmethod
    def execute(self, command):
        pass
