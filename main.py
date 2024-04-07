from pack_treatmentData import Data_treatment

"""
def main():
    Data_treatment.DataTreatment("product_N", 'The Coming Woman: A ...')
main()
"""
if __name__ == '__main__':

    print(" Arg_1 =>  Obligatoire \n"
          "\n"
          " 'directory_N' => Toutes les catégories et leurs produits\n"
          "                  (Arg_2 = None, il n'est pas nécéssaire)\n"
          "\n"
          " 'category_N' => Une catégorie et ses produits\n"
          "                 (Si Arg_2 n'est pas renseigné,  recherche aléatoire)\n"
          "\n"
          " product_N' => un produit\n"
          "               (Si Arg_2 n'est pas renseigné, recherche aléatoire)\n"
          "\n"
          "\n"
          "Arg_2 =>  Optionel\n"
          "\n"
          " 'Le nom d'un produit (*)' =>\n"
          "     Arg_1 'product_N' est obligatoire\n"
          "\n"
          " 'Le nom d'une catégorie' =>\n"
          "     Arg_1 'category_N' est obligatoire\n"
          "\n"
          "\n"
          "( * ) =>\n"
          "\n"
          "Pour les produits =>\n"
          "   - Inutile de mettre plus que les 4 premiers mots du titre\n"
          "   - Dans tous les cas ne pas renseigner les parenthèses et leur contenu "
          "\n"
          "\n")

    value1 = input('Arg_1 = ')
    value2 = input('Arg_2 = ')
    Data_treatment.DataTreatment(value1, value2)
