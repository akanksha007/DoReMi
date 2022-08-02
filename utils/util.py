import datetime

Date_Format = '%d-%m-%Y'


def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, Date_Format)
        return True
    except ValueError:
        return False


def fetch_date_from_date_string(date_text):
    return datetime.datetime.strptime(date_text, Date_Format)
