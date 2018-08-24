import yaml

from pyganalytics.api.authorization import authorize
from pyganalytics.api.client import Client


class TestReportingAPI(object):

    def setup_class(self):
        self.client = authorize(client_secret='credentials/client_secret.json', credentials_directory='credentials/')
        self.view_id = str(yaml.load(open('data/config.yml', 'r'))['ViewId'])

    def test_authorization(self):
        assert isinstance(self.client, Client)

    def test_reporting(self):
        response = self.client.reporting.get_report(self.view_id)
        assert 'reports' in response
