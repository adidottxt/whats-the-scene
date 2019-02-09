'''
random util functions
'''
import datetime
from datetime import date


def get_date(date_string):
    '''
    datetime object returner
    '''
    return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()


def get_title(location, count):
    '''
    get week string for playlist creation
    '''
    start, end = get_days(count)
    return str(start.month) + "/" + str(start.day) + " –– " \
        + str(end.month) + "/" + str(end.day) + " in " + location


def get_days(end):
    '''
    return today's date
    '''
    return date.today(), date.today() + datetime.timedelta(end, 0)


def get_three_days():
    '''
    good for weekends, not ideal, will fix later
    '''
    return date.today() + datetime.timedelta(3, 0)


def get_next_week():
    '''
    return date a week from today
    '''
    return date.today() + datetime.timedelta(7, 0)


def get_next_month():
    '''
    return date a month from today
    '''
    return date.today() + datetime.timedelta(30, 0)
