from dateutil.relativedelta import *
from datetime import date
import isodate

from typing import List

from pyganalytics.exceptions import InvalidDateRange, DateBeyondPresent

__all__ = ['dr']


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
    def signature(self):
        return self['startDate'] + '-' + self['endDate']


class DateRangeUtility(object):

    @property
    def today(self) -> date:
        return date.today()

    @property
    def last_seven_days(self):
        """The last full seven days (excluding "today"). This is the default used when no date range is specified."""
        yesterday = self.today + relativedelta(days=-1)
        seven_days_ago = self.today + relativedelta(days=-7)
        return DateRange(seven_days_ago.isoformat(), yesterday.isoformat())


    @property
    def last_week(self):
        """The last week from Monday to Sunday."""
        last_sunday = self.today + relativedelta(weekday=SU(-1))
        last_monday = last_sunday + relativedelta(weekday=MO(-1))
        return DateRange(last_monday.isoformat(), last_sunday.isoformat())

    def year(self, year) -> DateRange:
        if year == self.today.year:
            end_data = self.today.isoformat()
        else:
            end_data = '{}-12-31'.format(year)

        start_date = '{}-01-01'.format(year)

        return DateRange(start_date, end_data)

    def yearly(self, start: int, end: int) -> List[DateRange]:
        if end > self.today.year:
            raise DateBeyondPresent('EndDate is beyond current year: {}'.format(end))

        if start > end:
            raise InvalidDateRange('Start date needs to be before the end date.')

        ranges = list()
        for year in range(start, end + 1):
            ranges.append(self.year(year))
        return ranges


dr = DateRangeUtility()