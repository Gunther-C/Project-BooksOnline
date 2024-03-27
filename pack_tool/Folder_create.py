import os
import shutil
import Errors_treatment as Ers

class FolderCreate:
    def __init__(self, path: str | None = None) -> None:

        if not path:
            Ers.ErrorsTreatment("folder_create-1")
        else:
            self.path = path
            self.control_create()

    def control_create(self):

        isset_folder = os.path.exists(self.path)
        is_folder = os.path.isdir(self.path)
        if not isset_folder or not is_folder:
            os.mkdir(self.path)
        else:
            shutil.rmtree(self.path)

            isset_folder = os.path.exists(self.path)
            is_folder = os.path.isdir(self.path)
            if not isset_folder or not is_folder:
                os.mkdir(self.path)
            else:
                Ers.ErrorsTreatment("folder_create-2")
