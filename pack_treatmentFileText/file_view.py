import csv
import json
import Errors_treatment as Ers


# A REFAIRE


class FileView():
    def __init__(self, url: str | None = None, choice: str | None = None, format: str | None = None) -> None:

        self.choice = choice
        self.format = format
        self.path = url

        if not self.path or not self.choice or not self.format:
            Ers.ErrorsTreatment("file1")
        else:
            match self.choice:
                case "dictionary":
                    self.view_dictionary()
                case "lines":
                    self.view_lines()
                case _:
                    Ers.ErrorsTreatment("file_reading")

    def view_dictionary(self):
        match self.format:
            case "csv":
                with open(self.path, mode="r") as file:
                    text_csv = csv.DictReader(file)
                    for line in text_csv:
                        print(line)
            case "json":
                with open(self.path, mode="r") as file:
                    text_json = csv.DictReader(file)
                    for line in text_json:
                        print(line)
            case _:
                Ers.ErrorsTreatment("file_reading")

    def view_lines(self):
        match self.format:
            case "csv":
                with open(self.path, mode="r") as file:
                    # text_csv = csv.reader(file, delimiter=",")
                    text_csv = csv.reader(file, delimiter=',', quotechar='"')
                    for line in text_csv:
                        print(line)
            case "json":
                with open(self.path, mode="r") as file:
                    text_json = json.load(file)
                    for line in text_json:
                        print(line)
            case _:
                Ers.ErrorsTreatment("file_reading")


