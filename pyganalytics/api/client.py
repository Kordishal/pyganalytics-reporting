import logging
import json
from typing import List, Union
from pyganalytics.api.reporting import GoogleAnalyticsReportingAPIv4

from pyganalytics.utility import dr
from pyganalytics.core import RequestIterator
from pyganalytics.core.requests import ReportRequest
from pyganalytics.core.report import OutputReport, KeyValueReport


class Client(object):

    def __init__(self, credentials, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.reporting = GoogleAnalyticsReportingAPIv4(credentials,
                                                       retries=kwargs.get('retries', 3),
                                                       logger=kwargs.get('logger', logging.getLogger(__name__)))

    def yearly(self, start: int, end: int,
               base_request: ReportRequest,
               store: Union[str, None] = None,
               output: OutputReport = KeyValueReport) -> List[OutputReport]:
        results = list()
        date_ranges = dr.yearly(start, end)

        for date_range in date_ranges:
            request = base_request.copy(date_range)

            requests = RequestIterator(self)
            requests.add_request(request)

            current = None

            for reports in requests:
                if current is None:
                    current = output(reports[0])
                else:
                    current.append(reports[0])

            results.append(current)

            if isinstance(store, str):
                with open(store.format(date_range.signature), 'w') as fp:
                    json.dump(current, fp, indent='    ', ensure_ascii=False)

        return results



