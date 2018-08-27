import yaml

from pyganalytics.api.authorization import authorize
from pyganalytics.api.client import Client
from pyganalytics.core.report_request import ReportRequest
from pyganalytics.core.properties import Metric, MetricType


class TestReportingAPI(object):

    def setup_class(self):
        self.client = authorize(client_secret='credentials/client_secret.json', credentials_directory='credentials/')
        self.view_id = str(yaml.load(open('data/config.yml', 'r'))['ViewId'])
        self.report_request = ReportRequest(self.view_id,
                                            dimensions=[{'name': 'ga:country'}],
                                            metrics=Metric('Sessions', 'ga:sessions',
                                                           formattingType=MetricType.INTEGER))

    def test_authorization(self):
        assert isinstance(self.client, Client)

    def test_reporting(self):
        response = self.client.reporting.batch_get(report_request=self.report_request)
        assert 'reports' in response

