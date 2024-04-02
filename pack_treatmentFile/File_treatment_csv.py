from pack_treatmentUrl import url_control, url_requestPage
import Errors_treatment as Ers
import csv, sys


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
            # open(self.data['path'], 'r') as infile,
            with open(self.data['path'], self.data['action'], encoding="utf-8-sig", newline="") as file:
                writer = csv.writer(file, delimiter=",", dialect="excel", lineterminator="\n")
                try:

                    if self.data['action'] == 'w':
                        writer.writerow(["Descriptions", "Titres", "Liens", "Description", "Code",
                                         "Prix Ht", "Dev.", "Prix Ttc", "Dev.", "Stock", "Evaluation",
                                         "Lien photo"])

                    if self.data['description'] == 'Categorie' and self.data['action'] == 'a':
                        writer.writerow("")

                    if self.data['description'] and self.data['prt_name'] and self.data['prt_lien']:
                        writer.writerow([self.data['description'], self.data['prt_name'], self.data['prt_lien']])

                    if self.data['prd_data']:
                        writer.writerow(self.data['prd_data'])

                    self.result = True
                except csv.Error as e:
                    sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

        except IOError as er:
            print("Erreur lors de l'ouverture du fichier :", er)

        except UnicodeEncodeError as err:
            print("Erreur D'encodage :", err)
