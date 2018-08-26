import json
from typing import List
from pyganalytics.utility.enums import *
from pyganalytics.core.properties import DateRange


class ReportRequest(object):

    def __init__(self, view_id: str, metrics: List[Metrics],
                 date_ranges: List[DateRange] = None):
        self._view_id = view_id
        self.date_ranges = date_ranges
        self._sampling_level = Sampling.DEFAULT

    @property
    def view_id(self):
        return self._view_id

    @property
    def date_ranges(self):
        return self._date_ranges

    @date_ranges.setter
    def date_ranges(self, value: List[DateRange]):
        if value is None:
            self._date_ranges = [DateRange.last_seven_days()]
        elif len(value) < 2:
            self._date_ranges = value
        else:
            raise ValueError('May not assign more than two date ranges in a single report request.')

    def serialize(self):
        return {
            "viewId": self._view_id,
            "dateRanges": self._date_ranges,
  "samplingLevel": enum(Sampling),
  "dimensions": [
    {
      object(Dimension)
    }
  ],
  "dimensionFilterClauses": [
    {
      object(DimensionFilterClause)
    }
  ],
  "metrics": [
    {
      object(Metric)
    }
  ],
  "metricFilterClauses": [
    {
      object(MetricFilterClause)
    }
  ],
  "filtersExpression": string,
  "orderBys": [
    {
      object(OrderBy)
    }
  ],
  "segments": [
    {
      object(Segment)
    }
  ],
  "pivots": [
    {
      object(Pivot)
    }
  ],
  "cohortGroup": {
    object(CohortGroup)
  },
  "pageToken": string,
  "pageSize": number,
  "includeEmptyRows": boolean,
  "hideTotals": boolean,
  "hideValueRanges": boolean,
}