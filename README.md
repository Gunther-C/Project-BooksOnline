
# Project_BooksOnline

### **_Scraping on books.toscrape_**
Récupérer des infos sur https://books.toscrape.com/ puis les stocker par classifications, dossiers, fichiers.csv

##
## Fonction / Objectif
### Mode de récupération :
- Historique complet du site
- Catégories et ses produits
- Produit


### Récupération :
#### Données de l'article
    1. Code 
    2. Lien 
    3. Catégorie
    4. Nom
    5. Descriptif 
    6. Prix HT
    7. Prix TTC
    8. Evaluation
    9. Lien photo

#### Objet de l'article
    1. Photo  


### Organisation du contenu sélectionné :




![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

##
## Paramètres / Exemples  

#### _Paramètres_ :

Arg_1 =>  Obligatoire

        "directory_N" => Toutes les catégories et leurs produits
                         (Arg_2 = None, il n'est pas nécéssaire)
                      
        "category_N" => Une catégorie et ses produits
                        (Si Arg_2 n'est pas renseigné,  recherche aléatoire)

        "product_N" => un produit 
                       (Si Arg_2 n'est pas renseigné, recherche aléatoire)

Arg_2 =>  Optionel
     
      "Le nom d'un produit (*)" =>
            Arg_1 "product_N" est obligatoire

      "Le nom d'une catégorie" =>
            Arg_1 "category_N" est obligatoire

( * ) =>

        Pour les produits =>
            - Le titre uniquement sans son complément (avant ':' ou ',' )
            - Dans tous les cas ne pas renseigner les parenthèses et leur contenu   
##
#### _Exemples_ : ( Fichier main.py )

Toutes les catégories et leurs produits

        Data_treatment.DataTreatment("directory_N")

Une catégorie et ses produits

        Data_treatment.DataTreatment("category_N")
        ou
        Data_treatment.DataTreatment("category_N", <nom de la catégorie>)

Un produits

        Data_treatment.DataTreatment("product_N")
        ou
        Data_treatment.DataTreatment("product_N", <nom du produit>)
            Voir (*) ci-dessus pour plus d'infos 

##
## Exécution locale

Clone du projet

```bash
  git clone https://github.com/Gunther-C/Project-BooksOnline.git
```

###
## Technologie

**Python 3.12:** Python Objet

**Editeur de texte:** PyCharm

##
### 🔗 Links

[![linkedin](https://www.linkedin.com/in/gunther-chevestrier-813344255?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)
