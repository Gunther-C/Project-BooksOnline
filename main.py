from pack_treatmentFileText import File_treatment
from pack_treatmentData import Data_treatment

"""
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
"""


def main():

    Data_treatment.DataTreatment("directory_N")


if __name__ == '__main__':
    main()
