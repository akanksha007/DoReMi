import datetime
from dateutil.relativedelta import relativedelta

from entity.duration_unit import DurationUnit

Date_Format = '%d-%m-%Y'


def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, Date_Format)
        return True
    except ValueError:
        return False


def fetch_date_from_date_string(date_text):
    return datetime.datetime.strptime(date_text, Date_Format)


def category_already_subscribed(subscribed_categories, new_subscription_category):
    if new_subscription_category in subscribed_categories:
        return True
    else:
        return False


def subscription_date_not_set(date):
    if date is None:
        return True
    else:
        return False


class Duration:
    pass


def get_renewal_date(subscription_start_date, duration_unit, duration_count):
    # subscription_start_date = datetime.datetime.strptime(subscription_start_date, Date_Format)

    if duration_unit == DurationUnit.DAY:
        renewal_date = subscription_start_date + datetime.timedelta(days=duration_count)
    elif duration_unit == DurationUnit.MONTH:
        renewal_date = subscription_start_date + relativedelta(months=duration_count)
    elif duration_unit == DurationUnit.YEAR:
        renewal_date = subscription_start_date + datetime.timedelta(years=duration_count)
    return renewal_date.date().strftime(Date_Format)


def get_topup_months(topup, months):
    if topup.duration_unit == DurationUnit.MONTH:
        return months / topup.duration_count
