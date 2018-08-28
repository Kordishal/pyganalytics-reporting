from pyganalytics.utility import dr

from pyganalytics.utility.dateranges import DateRange


class TestDateRange(object):

    def test_last_seven_days(self):
        assert isinstance(dr.last_seven_days, DateRange)

    def test_yearly(self):
        ranges = dr.yearly(2016, 2018)
        assert 3 == len(ranges)
        print(ranges)



