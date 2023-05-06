from datetime import datetime


def format_time(datetime_obj):
    print('24h', datetime.strftime(datetime_obj, '%H:%M'))
    print('12h', datetime.strftime(datetime_obj, '%I:%M'))
