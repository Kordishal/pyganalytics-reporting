

class PyGAnalyticsError(Exception):
    pass


class InvalidDateRange(PyGAnalyticsError):
    """The defined date range is invalid."""


class DateBeyondPresent(PyGAnalyticsError):
    """Dates beyond present cannot be used."""
