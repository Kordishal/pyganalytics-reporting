from dateutil.relativedelta import *
from datetime import date
import isodate

from pyganalytics.exceptions import InvalidDateRange


class DateRange(dict):

    def __init__(self, start: str, end: str):
        self._validate_range(isodate.parse_date(start), isodate.parse_date(end))
        super().__init__(startDate=start, endDate=end)

    def __setitem__(self, key: str, value: str):
        if key not in ['startDate', 'endDate']:
            raise KeyError('Only startDate and endDate may be set!')
        else:
            if key == 'startDate':
                self._validate_range(isodate.parse_date(value), isodate.parse_date(self['endDate']))
            elif key == 'endDate':
                self._validate_range(isodate.parse_date(self['startDate']), isodate.parse_date(value))
            super().__setitem__(key, value)

    @staticmethod
    def _validate_range(start, end):
        if start > end:
            raise InvalidDateRange('Start date "{}" cannot be after end date "{}"'.format(start, end))


@property
def today():
    return date.today()


@property
def last_seven_days():
    """The last full seven days (excluding "today"). This is the default used when no date range is specified."""
    yesterday = today + relativedelta(days=-1)
    seven_days_ago = today + relativedelta(days=-7)
    return DateRange(seven_days_ago.isoformat(), yesterday.isoformat())


@property
def last_week():
    """The last week from Monday to Sunday."""
    last_sunday = today + relativedelta(weekday=SU(-1))
    last_monday = last_sunday + relativedelta(weekday=MO(-1))
    return DateRange(last_monday.isoformat(), last_sunday.isoformat())
