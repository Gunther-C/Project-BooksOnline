import requests



class FileTreatmentImg:

    def __init__(self, data):

        if not data:
            Ers.ErrorsTreatment("file_treatment")
        else:
            self.data: dict = data
            self.result = False
            self.treatment()

    def treatment(self):

        filename = self.data['link'].split("/")[-1]
        index = filename.rfind('.')
        extension = filename[index:]
        new_path = self.data['path'] + extension

        file_data = requests.get(self.data['link']).content

        try:
            with open(new_path, "wb") as img:
                img.write(file_data)
                self.result = True

        except IOError as er:
            print("Erreur lors de l'ouverture du fichier :", er)

        except UnicodeEncodeError as err:
            print("Erreur D'encodage :", err)
