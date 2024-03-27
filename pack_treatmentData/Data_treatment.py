from bs4 import BeautifulSoup
from pack_treatmentData import Data_recovery as Recovery
from pack_tool import Format_date as Fd, CleanUp_string as Clean_str, Folder_create as Folder
import Errors_treatment as Ers
import csv
import json
import time


class DataTreatment:
    def __init__(self, choice: str | None = None, name: str | None = None) -> None:

        self.name = None

        if not choice:
            Ers.ErrorsTreatment("data_treatment_1")
        else:
            if name:
                self.name = name.strip()
            self.choice = choice.strip()
            self.page = Recovery.DataRecovery("https://books.toscrape.com/index.html")
            self.path = str("https://books.toscrape.com/")
            self.date_fr = Fd.FrenchDate().format_fr
            self.dom = None
            self.site_folder = None
            self.catg_folder = None

            self.data_treatment()

    # ___

    def data_treatment(self):

        if not self.page.index:
            Ers.ErrorsTreatment("data_treatment_2")
        else:

            self.dom = BeautifulSoup(self.page.index, "html.parser")

            if self.choice == 'directory_N':
                self.folder_directory()

            elif self.name and self.choice == 'category_N':
                self.gestion_category()

            elif self.name and self.choice == 'product_N':
                self.gestion_product()

            else:
                Ers.ErrorsTreatment("data_treatment_3")

    # ___

    def gestion_category(self):
        if not self.dom:
            Ers.ErrorsTreatment("data_treatment_4")
        else:
            result = False
            content_catg = self.dom.find("ul", class_="nav-list").find('ul').find_all("li")
            for li in content_catg:
                element = li.find('a')
                catg_link: str = self.path + element['href']
                catg_name: str = element.string.strip()

                if catg_name == self.name:
                    self.folder_category(catg_link, catg_name)
                    result = True
                    break

            if not result:
                Ers.ErrorsTreatment("data_treatment_5", self.name)

    # ___

    def gestion_product(self):
        if not self.dom:
            Ers.ErrorsTreatment("data_treatment_4")
        else:
            products = self.dom.find("ul", class_="nav-list").find("li").find('a')
            catg_link: str = self.path + products['href']
            catg_name: str = products.string.strip()
            self.folder_category(catg_link, catg_name)

    # ___

    def folder_directory(self):

        if not self.dom:
            Ers.ErrorsTreatment("data_treatment_4")
        else:
            title_site = self.dom.find("header", {'class': 'header'}).find('a').string.strip()
            title_site = self.cleaner_folder_name(title_site)
            self.site_folder = 'pack_stock/' + title_site + '-(' + str(self.date_fr) + ')'
            Folder.FolderCreate(self.site_folder)

            content_catg = self.dom.find("ul", class_="nav-list").find('ul').find_all("li")
            for li in content_catg:
                element = li.find('a')
                catg_link: str = self.path + element['href']
                catg_name: str = element.string.strip()
                self.folder_category(catg_link, catg_name)
                time.sleep(1)

    # ___

    def folder_category(self, catg_link: any, catg_name: any) -> None:

        if not catg_link or not catg_name:
            Ers.ErrorsTreatment('data_treatment_7')
        else:
            self.page = Recovery.DataRecovery(catg_link)
            self.dom = BeautifulSoup(self.page.index, 'html.parser')

            if not self.page.index or not self.dom:
                Ers.ErrorsTreatment('data_treatment_8')
            else:
                title_category = self.cleaner_folder_name(catg_name)

                if self.choice == 'directory_N':
                    self.catg_folder = self.site_folder + '/Catg_' + title_category
                    Folder.FolderCreate(self.catg_folder)
                elif self.choice == 'category_N':
                    self.catg_folder = 'pack_stock/Catg_' + title_category + '-(' + str(self.date_fr) + ')'
                    Folder.FolderCreate(self.catg_folder)
                else:
                    pass

                other_page = self.dom.find('ul', class_='pager')
                if not other_page:
                    products = self.dom.find_all('article', class_='product_pod')
                    for prd in products:
                        link = prd.find('h3').find('a')
                        link = link['href']
                        new_path = self.cleanup_link(link)
                        prd_link: str = self.path + 'catalogue/' + new_path
                        self.folder_product(prd_link)
                        time.sleep(1)

                else:
                    count_page = other_page.find('li', class_='current').string.replace(' ', '').strip()
                    if self.choice == 'product_N':
                        count_page = int(count_page[-2])
                    else:
                        count_page = int(count_page[-1])

                    for i in range(count_page):
                        if i > 0:
                            index_catg = catg_link.find('index.html')
                            url_catg = catg_link[:index_catg]
                            nbr_page = i + 1
                            extend_path = 'page-' + str(nbr_page) + '.html'
                            next_path = url_catg + extend_path
                            self.page = Recovery.DataRecovery(next_path)
                            self.dom = BeautifulSoup(self.page.index, 'html.parser')

                        if not self.page.index or not self.dom:
                            Ers.ErrorsTreatment('data_treatment_8')
                        else:
                            products = self.dom.find_all('article', class_='product_pod')
                            for prd in products:
                                link = prd.find('h3').find('a')
                                link = link['href']
                                new_path = self.cleanup_link(link)
                                prd_link: str = self.path + 'catalogue/' + new_path
                                self.folder_product(prd_link)
                                time.sleep(1)

    # ___

    def folder_product(self, prd_link=None):

        if not prd_link:
            Ers.ErrorsTreatment('data_treatment_9')
        else:
            self.page = Recovery.DataRecovery(prd_link)
            self.dom = BeautifulSoup(self.page.index, 'html.parser')

            if not self.page.index or not self.dom:
                Ers.ErrorsTreatment('data_treatment_10')
            else:
                product = self.dom.find('div', class_='product_main')
                title_product = product.find('h1').string.strip()
                title_product = self.cleaner_folder_name(title_product)
                print(title_product)

# Mettre un tableau pour récup les memes nom et rajouter vol1 etc a voir

                """
                if self.choice != 'directory_N' and self.choice != 'category_N':
                    prd_folder = 'pack_stock/' + title_product + '-(' + str(self.date_fr) + ')'
                else:
                    prd_folder = self.catg_folder + '/' + title_product
    
                Folder.FolderCreate(prd_folder)"""

                en_tete = ['Code', 'Lien Description', 'Catégorie', 'Titre', 'Description', 'Prix Ht', 'Prix Ttc',
                           'Lien photo',
                           'Evaluation']

    def cleaner_folder_name(self, value):

# voir plutot avec un split
        folder_name_format = ['/', '\\', '|', '*', '"', '?', '<', '>']

        for oc in folder_name_format:
            value = value.replace(oc, '')

        bracket_before = value.find('(')
        bracket_after = value.find(')')
        if bracket_before != -1:
            text_before = value[:bracket_before]
            if bracket_after != -1:
                text_after = value[bracket_after:]
                text_after = text_after.replace(')', '')
                value = text_before + text_after

        point = value.find(':')
        if point != -1:
            value = value[:point]
        # .replace(' ', '-')
        value = value.strip()

        return value


    def cleanup_link(self, new_path):
        for x in new_path:
            if x != '.' and x != '/':
                nbr_key = new_path.find(x)
                index = new_path.find(new_path[nbr_key])
                new_path = new_path[index:]
                break
        return new_path
