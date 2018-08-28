import yaml

from pyganalytics.api.authorization import authorize
from pyganalytics.core.iterator import RequestIterator
from pyganalytics.core.requests import ReportRequest
from pyganalytics.core.properties import Metric, MetricType

import json


class TestClient(object):

    def setup_class(self):
        self.client = authorize(client_secret='credentials/client_secret.json', credentials_directory='credentials/')
        self.view_id = str(yaml.load(open('data/config.yml', 'r'))['ViewId'])

    def test_yearly(self):
        request = ReportRequest(viewId=self.view_id,
                                dimensions=[{'name': 'ga:pagePath'}],
                                metrics=Metric('Page Views', 'ga:pageviews'))
        result = self.client.yearly(2016, 2018, store='output-{}.json', base_request=request)
        assert len(result) == 3
