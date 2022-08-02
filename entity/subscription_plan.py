class SubscriptionPlan:
    def __init__(self, name, duration_unit, duration_count, category_type, amount):
        self._name = name
        self._duration_unit = duration_unit
        self._duration_count = duration_count
        self._category_type = category_type
        self._amount = amount

    @property
    def name(self):
        return  self._name

    @property
    def duration_unit(self):
        return self._duration_unit

    @property
    def category_type(self):
        return self._category_type

    @property
    def amount(self):
        return self._amount

    @property
    def duration_count(self):
        return self._duration_count


