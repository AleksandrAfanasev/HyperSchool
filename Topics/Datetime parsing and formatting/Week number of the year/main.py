from datetime import datetime


def get_week_number(datetime_obj):
    num = datetime_obj.isocalendar()[1]
    return f"Week number: {num}."
