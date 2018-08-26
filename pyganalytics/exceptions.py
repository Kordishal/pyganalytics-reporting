

class PyGAnalyticsError(Exception):
    pass


class InvalidDateRange(PyGAnalyticsError):
    """The defined date range is invalid."""
