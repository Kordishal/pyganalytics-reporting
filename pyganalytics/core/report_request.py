import json
from typing import List, Union
from pyganalytics.utility.enums import *
from pyganalytics.core.properties import Metric
from pyganalytics.utility import dateranges as dr
from pyganalytics.utility.dateranges import DateRange


class ReportRequest(object):

    def __init__(self, view_id: str, dimensions: List[dict], metrics: Metric,  **kwargs):
        self._view_id = view_id
        self._dimensions = dimensions
        self._metrics = metrics
        self._date_ranges = kwargs.get('dateRanges', None)
        self._sampling_level = kwargs.get('samplingLevel', Sampling.DEFAULT)

        self.dimensionFilterClauses = kwargs.get('dimensionFilterClauses', None)
        self.metricFilterClauses = kwargs.get('metricFilterClauses', None)
        self.filtersExpression = kwargs.get('filtersExpression', None)
        self.orderBys = kwargs.get('orderBys', None)
        self.segments = kwargs.get('segments', None)
        self.pivots = kwargs.get('pivots', None)
        self.cohortGroup = kwargs.get('cohortGroup', None)
        self.pageToken = kwargs.get('pageToken', None)
        self.pageSize = kwargs.get('pageSize', 1000)
        self.includeEmptyRows = kwargs.get('includeEmptyRows', False)
        self.hideTotals = kwargs.get('hideTotals', False)
        self.hideValueRanges = kwargs.get('hideValueRanges', False)

    @property
    def view_id(self):
        return self._view_id

    @property
    def date_ranges(self):
        return self._date_ranges

    @date_ranges.setter
    def date_ranges(self, value: Union[List[DateRange], None]):
        if value is None:
            self._date_ranges = [dr.last_seven_days]
        elif len(value) < 2:
            self._date_ranges = value
        else:
            raise ValueError('May not assign more than two date ranges in a single report request.')

    @property
    def sampling_level(self):
        return self._sampling_level

    @sampling_level.setter
    def sampling_level(self, value: Union[Sampling, str]):
        if isinstance(value, Sampling):
            self._sampling_level = value
        else:
            self._sampling_level = Sampling[value]

    def serialize(self):
        return {
            "viewId": self._view_id,
            "dateRanges": self._date_ranges,
            "samplingLevel": self._sampling_level.value,
            "dimensions": self._dimensions,
            "dimensionFilterClauses": self.dimensionFilterClauses,
            "metrics": self._metrics,
            "metricFilterClauses": self.metricFilterClauses,
            "filtersExpression": self.filtersExpression,
            "orderBys": self.orderBys,
            "segments": self.segments,
            "pivots": self.pivots,
            "cohortGroup": self.cohortGroup,
            "pageToken": self.pageToken,
            "pageSize": self.pageSize,
            "includeEmptyRows": self.includeEmptyRows,
            "hideTotals": self.hideTotals,
            "hideValueRanges": self.hideValueRanges,
        }
