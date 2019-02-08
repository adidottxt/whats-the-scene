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

def get_week():
    '''
    get week string for playlist creation
    '''
    today = get_today()
    week = get_next_week()
    return str(today.month) + "/" + str(today.day) + " –– " \
        + str(week.month) + "/" + str(week.day)

def get_today():
    '''
    return today's date
    '''
    return date.today()

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
