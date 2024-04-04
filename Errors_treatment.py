class ErrorsTreatment:
    def __init__(self, error_type: str = "NoError", supp_text: any = None):

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

            case "data_recovery":
                print(f"L'url est absente")

            case "data_recovery1":
                print(f"Échec de l'url")

            case "data_recovery2":
                print(f"Échec lecture de la page")

            case "data_treatment_1":
                print(f"Rentrez une valeur")

            case "data_treatment_2":
                print(f"Le chemin du site n'est pas reconnu")

            case "data_treatment_3":
                print(f"Le chemin du domaine principale n'est pas reconnu")

            case "data_treatment_4":
                print(f"Le premier argument est absent ou incorrect veuillez réessayer")

            case "data_treatment_5":
                print(f"Le chemin du domaine n'a pu être récupéré")

            case "data_treatment_6":
                print(f"Le dossier principale n'a pu être créé")

            case "data_treatment_7":
                print(f"Toutes les valeurs de la catégorie {self.text} n'ont pu être récupérées")

            case "data_treatment_8":
                print(f"Le dossier de la catégorie {self.text} n'a pu être créé")

            case "data_treatment_9":
                print(f"Le nom ({self.text}) ne correspond à aucune catégorie")

            case "data_treatment_10":
                print(f"Le lien de la catégorie ({self.text}) n'est pas reconnu")

            case "data_treatment_11":
                print(f"Aucun dossier catégorie n'a pu être créé")

            case "data_treatment_12":
                print(f"La catégorie n'a pu être créée")

            case "data_treatment_13":
                print(f"Le chemin du domaine catégorie n'est pas reconnu")

            case "data_treatment_14":
                print(f"Le chemin du produit n'est pas reconnu")

            case "data_treatment_15":
                print(f"Le chemin de la page suivante de la catégorie n'est pas reconnu")

            case "data_treatment_16":
                print(f"Le chemin du domaine produit n'est pas reconnu")

            case "data_treatment_17":
                print(f"Le produit n'a pas été identifiée")

            case "data_treatment_18":
                print(f"Erreur création : {self.text}")

            case "data_treatment_19":
                print(f"Erreur création : {self.text}")

            case "data_treatment_20":
                print(f"Le nom ({self.text}) ne correspond à aucun produit")

            case "folder_create-1":
                print(f"Pas d'url pour la création du dossier")

            case "folder_create-2":
                print(f"Erreur le dossier n'a pas pu ètre remplacé")

            case "folder_create-3":
                print(f"Erreur chemin de dossier : {self.text}")

            case "folder_create-4":
                print(f"Syntaxe du nom de dossier incorrecte : {self.text}")

            case _:
                print(f"Erreur veuillez réssayer")

