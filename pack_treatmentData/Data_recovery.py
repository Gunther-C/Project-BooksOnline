from pack_treatmentUrl import url_control, url_requestPage
import Errors_treatment as Ers


class DataRecovery:
    def __init__(self, url: str | None = None) -> None:

        if not url:
            Ers.ErrorsTreatment("data_recovery", url)
        else:
            self.url = url
            self.index = None
            self.request_path()

    def request_path(self):
        control = url_control.UrlControl(self.url)
        if not control:
            Ers.ErrorsTreatment("data_recovery1", self.url)

        else:
            page = url_requestPage.Request(self.url)
            if not page.result:
                Ers.ErrorsTreatment("data_recovery2", self.url)
            else:
                self.index = page.newpage

