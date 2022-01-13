import logging
import requests
import json


class AdmieDataCollector():

    def __init__(self, filetypes=None, ssl_verify=False):

        # API query variables
        self._baseurl = 'https://www.admie.gr'
        self._session = requests.Session()
        self._session.verify = ssl_verify

        if not(filetypes):
            self.get_file_types(filetypes)
        else:
            try:
                with open(filetypes, 'r', encoding='utf8') as fp:
                    self._file_types = json.load(fp)
                    logging.debug("Loaded file types from static file.")
            except Exception as e:
                raise(e)

    @property
    def session(self):
        return self._session

    @property
    def baseurl(self):
        return self._baseurl

    @property
    def file_types(self,):
        return self._file_types

    def get_file_types(self, fpath):
        logging.debug("Loading file types from the Internet.")
        self._file_types = self.session.get(
            self._baseurl + '/getFiletypeInfoEN').json()
        with open(fpath, 'w', encoding='utf8') as fp:
            json.dump(self._file_types, fp)

    def get_file_list(self, file_type, date_start, date_end):
        params = {'dateStart': date_start,
                  'dateEnd': date_end,
                  'FileCategory': file_type}
        res = self.session.get(self.baseurl+'/getOperationMarketFilewRange',
                               params=params)
        return res.json()

    def downloadFiles(self, file_type, date_start, date_end):
        fl = self.get_file_list(file_type, date_start, date_end)
        pass
