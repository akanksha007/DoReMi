from abc import abstractmethod, ABC


class Mode(ABC):
    @abstractmethod
    def process(self):
        pass

    def process_command(self, command):
        pass
