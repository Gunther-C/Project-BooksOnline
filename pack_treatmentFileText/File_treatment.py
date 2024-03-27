from pack_treatmentUrl import url_control, url_requestPage
import Errors_treatment as Ers



# EN COURS


class FileTreatment:
    def __init__(self, url: str | None = None) -> None:

        if not url:
            Ers.ErrorsTreatment("file_treatment", url)
        else:
            self.url = url
            # self.request_path()

    def request_path(self):
        control = url_control.UrlControl(self.url)
        if not control:
            return False
        else:
            page = url_requestPage.Request(self.url)
            if not page.result:
                return False
            else:
                return page.newpage


