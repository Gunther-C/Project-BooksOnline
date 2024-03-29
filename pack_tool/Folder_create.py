import os
import shutil
import Errors_treatment as Ers


class FolderCreate:
    def __init__(self, path: str | None = None) -> None:

        self.error_folder = False

        if not path:
            self.error_folder = True
            Ers.ErrorsTreatment("folder_create-1")

        else:
            self.path = path
            self.control_create()

    def control_create(self):

        try:
            isset_folder = os.path.isdir(self.path)
            # is_foldersAndFiles = os.path.exists(self.path) or not is_folder
            if not isset_folder:
                os.mkdir(self.path)
            else:
                shutil.rmtree(self.path, ignore_errors=False, onerror=None)
                if isset_folder:
                    os.mkdir(self.path)
                else:
                    self.error_folder = True
                    Ers.ErrorsTreatment("folder_create-2")

        except FileNotFoundError as fld:
            self.error_folder = True
            Ers.ErrorsTreatment("folder_create-3", fld)

        except OSError as ose:
            self.error_folder = True
            Ers.ErrorsTreatment("folder_create-4", ose)

