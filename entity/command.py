class Command:
    def __init__(self, input_line):
        self._name, *self._params = input_line.split(' ')
    @property
    def name(self):
        return self._name

    @property
    def params(self):
        return self._params
