class ErrorsTreatment:
    def __init__(self, error_type: str = "NoError", supp_text: any = None):

        # rtype: str | None

        self.type = error_type
        self.text = supp_text
        self.__str__()

    def __str__(self) -> None:

        match self.type:

            case "NoError":
                print(f"Pas de type erreur")

            case "urlCtrl":
                if len(self.text) > 1:
                    print(f"Échec de la connexion à l'URL {self.text[0]}: {self.text[1]}")
                else:
                    print(f"Échec de la connexion à l'URL")
            case "request_1":
                print(f"Échec de connexion: {self.text}")

            case "request_2":
                print(f"Erreur statut Url réponse: {self.text}")

            case "data_treatment_1":
                print(f"Rentrez un valeur")

            case "data_treatment_2":
                print(f"L'url du site créée une erreur inattendue")

            case "data_treatment_3":
                print(f"Erreur de saisie veuillez réessayer")

            case "data_treatment_4":
                print(f"Le domaine n'a pas pu être téléchargé")

            case "data_treatment_5":
                print(f"Le nom ({self.text}) ne correspond à aucune catégorie")

            case "data_treatment_6":
                print(f"Le nom ({self.text}) ne correspond à aucun produit")

            case "data_treatment_7":
                print(f"L'url catégorie créée une erreur inattendue")

            case "data_treatment_8":
                print(f"Erreur de valeur catégorie")

            case "data_treatment_9":
                print(f"Erreur de valeur produit")

            case "data_treatment_10":
                print(f"L'url d'un produit à créée une erreur inattendue")

            case "data_recovery":
                print(f"Échec lecture de la page")

            case "folder_create-1":
                print(f"Erreur création dossier pas de chemin")

            case "folder_create-2":
                print(f"Erreur création dossier impossible")

            case _:
                print(f"Erreur veuillez réssayer")
