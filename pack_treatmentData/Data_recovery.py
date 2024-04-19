from pack_treatmentUrl import Url_control, Url_requestPage
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
        control = Url_control.UrlControl(self.url)
        if not control:
            Ers.ErrorsTreatment("data_recovery", self.url)

        else:
            page = Url_requestPage.Request(self.url)
            if not page.result:
                Ers.ErrorsTreatment("data_recovery", self.url)
            else:
                self.index = page.newpage

