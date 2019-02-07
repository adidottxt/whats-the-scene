'''
random util functions
'''
import datetime
from datetime import date

def get_week_string():
    '''
    get week string for playlist creation
    '''
    today = date.today()
    week = today + datetime.timedelta(7, 0)
    # 2/7 - 2/14
    return str(today.month) + "/" + str(today.day) + " –– " \
        + str(week.month) + "/" + str(week.day)
