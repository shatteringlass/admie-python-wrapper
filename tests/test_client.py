import pathlib

from admie_client import AdmieDataCollector


class TestClient:

    def setup_class(self):
        ft = (pathlib.Path(__file__).parent / 'filetypes.json').resolve()
        self.client = AdmieDataCollector(ft)

    def teardown_class(self):
        pass

    def test_file_types(self):
        ftypes = self.client.file_types
        assert isinstance(ftypes, list) and len(ftypes) > 0

    def test_file_list(self):
        flist = self.client.get_file_list(
            'ISP1DayAheadLoadForecast', '2021-11-01', '2021-12-21')
        assert isinstance(flist, list) and len(flist) > 0
