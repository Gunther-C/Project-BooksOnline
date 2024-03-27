from urllib.request import urlopen
from urllib.error import URLError
import Errors_treatment as Ers


class UrlControl:
    def __init__(self, url):
        self.result = False
        try:
            urlopen(url, timeout=3)
        except URLError as e:
            info = (url, e)
            Ers.ErrorsTreatment("urlCtrl", info)
        else:
            self.result = True

# augmenter timeout de 1 (4) et recommencer 3 fois en rajoutant 1 a chaque passage
# si tjrs pas error
