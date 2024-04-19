import Errors_treatment as Ers
import csv
import sys


class FileTreatmentCsv:
    def __init__(self, data):

        if not data:
            Ers.ErrorsTreatment("file_treatment")
        else:
            self.data: dict = data
            self.result = False
            self.treatment()

    def treatment(self):
        try:
            with open(self.data['path'], self.data['action'], encoding="utf-8-sig", newline="") as file:
                writer = csv.writer(file, delimiter=",", dialect="excel", lineterminator="\n")
                try:
                    if self.data['action'] == 'w':
                        writer.writerow(["Catégorie", "Titre", "Lien", "Description", "Code",
                                         "Prix Ht", "Dev.", "Prix Ttc", "Dev.", "Stock", "Evaluation",
                                         "Lien photo"])

                    if self.data['prd_data']:
                        writer.writerow(self.data['prd_data'])

                    self.result = True
                except csv.Error as e:
                    sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
        except IOError as er:
            print("Erreur lors de l'ouverture du fichier :", er)
        except UnicodeEncodeError as err:
            print("Erreur D'encodage :", err)
