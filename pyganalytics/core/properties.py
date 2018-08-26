import re
import isodate
from dateutil.relativedelta import *
from datetime import date


class BaseProperty(object):
    pass


class DateRange(object):

    @classmethod
    def from_json(cls, date_range):
        return cls(date_range['startDate'], date_range['endDate'])

    @classmethod
    def last_seven_days(cls):
        """The last full seven days (excluding "today"). This is the default used when no date range is specified."""
        today = date.today()
        yesterday = today + relativedelta(days=-1)
        seven_days_ago = today + relativedelta(days=-7)
        return cls(seven_days_ago.isoformat(), yesterday.isoformat())

    @classmethod
    def last_week(cls):
        """The last week from Monday to Sunday."""
        today = date.today()
        last_sunday = today + relativedelta(weekday=SU(-1))
        last_monday = last_sunday + relativedelta(weekday=MO(-1))
        return cls(last_monday.isoformat(), last_sunday.isoformat())

    def __init__(self, start: str, end: str):
        self._start = isodate.parse_date(start)
        self._end = isodate.parse_date(end)

    @property
    def start(self):
        return self._start.isoformat()

    @start.setter
    def start(self, value):
        self._start = isodate.parse_date(value)

    @property
    def end(self):
        return self._end.isoformat()

    @end.setter
    def end(self, value):
        self._end = isodate.parse_date(value)

class Metric(BaseProperty):
    pass