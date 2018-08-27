from datetime import date

import isodate
from dateutil.relativedelta import *
from pyganalytics.utility.dateranges import DateRange


if __name__ == '__main__':

    day = date.today()
    print(day.isoformat())
    print(date.weekday(day))

    tomorrow = isodate.parse_date('2018-08-27')
    print(tomorrow.weekday())

    today = date.today()

    today = isodate.parse_date('2018-08-27')

    last_sunday = today + relativedelta(weekday=SU(-1))
    last_monday = last_sunday + relativedelta(weekday=MO(-1))
    print(last_sunday.isoformat())
    print(last_monday.isoformat())

    today = date.today()
    seven_days_ago = today + relativedelta(days=-7)
    print(today)
    print(seven_days_ago.isoformat())

    dr = DateRange('2018-08-20', '2018-08-27')
    start = dr['startDate']
    dr['endDate'] = '2018-09-30'

    print(start)
    print(dr['endDate'])
    print()

