class Topup:
    def __init__(self, name, max_device_count, duration_unit, duration_count, amount):
        self._name = name
        self._max_device_count = max_device_count
        self._duration_unit = duration_unit
        self._duration_count = duration_count
        self._amount = amount

    @property
    def name(self):
        return self._name

    @property
    def duration_unit(self):
        return self._duration_unit

    @property
    def max_device_count(self):
        return self._max_device_count

    @property
    def amount(self):
        return self._amount

    @property
    def duration_count(self):
        return self._duration_count
