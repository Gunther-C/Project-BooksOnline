import requests
import Errors_treatment as Ers


class Request:
    def __init__(self, url):
        self.result = False
        self.newpage = None

        try:
            response = requests.get(url, timeout=None)
            # , timeout=3
        except requests.ConnectionError as e:
            Ers.ErrorsTreatment("request_1", e)
        else:
            if response.status_code == 200:
                self.newpage = response.content
                self.result = True
            else:
                Ers.ErrorsTreatment("request_2", response.status_code)

