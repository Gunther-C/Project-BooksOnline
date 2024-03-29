from bs4 import BeautifulSoup
from pack_treatmentData import Data_recovery as Recovery
from pack_tool import Format_date as Fd, CleanUp_string as Clean_str, Folder_create as Folder
import Errors_treatment as Ers
import csv
import json
import random
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
            self.Clean_str = Clean_str
            self.dom = None
            self.content_catg = None
            self.site_folder = None
            self.catg_folder = None

            if not self.page.index:
                Ers.ErrorsTreatment("data_treatment_2")
            else:
                self.dom = BeautifulSoup(self.page.index, "html.parser")
                if not self.dom:
                    Ers.ErrorsTreatment("data_treatment_3")
                else:
                    self.data_dom()

    # ___

    def data_dom(self):

        self.content_catg = self.dom.find("ul", class_="nav-list").find('ul').find_all("li")

        if self.content_catg:

            if self.choice == 'directory_N':
                self.data_directory()

            elif self.choice == 'category_N':
                if self.name:
                    self.data_category()
                else:
                    self.data_category_rand()

            elif self.choice == 'product_N':
                if self.name:
                    self.data_product()
                else:
                    self.data_category_rand()

        else:
            Ers.ErrorsTreatment("data_treatment_5")

    # ___

    def data_directory(self):
        title_site = self.dom.find("header", {'class': 'header'}).find('a').string.strip()
        title_site = self.Clean_str.CleanUpString().cleaner_folder_name(title_site)
        if not title_site:
            title_site = "Home"

        self.site_folder = 'pack_stock/' + title_site + '-(' + str(self.date_fr) + ')'
        # result_create = Folder.FolderCreate(self.site_folder)

        if Folder.FolderCreate(self.site_folder).error_folder:
            Ers.ErrorsTreatment("data_treatment_6")
        else:
            for li in self.content_catg:
                element = li.find('a')
                catg_link: str = self.path + element['href']
                catg_name: str = element.string.strip()
                if not catg_name or not catg_link:
                    Ers.ErrorsTreatment("data_treatment_7", catg_name)
                    continue
                else:
                    title_category = self.Clean_str.CleanUpString().cleaner_folder_name(catg_name)
                    self.catg_folder = self.site_folder + '/Catg_' + title_category
                    if Folder.FolderCreate(self.catg_folder).error_folder:
                        Ers.ErrorsTreatment("data_treatment_8", catg_name)
                        continue
                    else:
                        self.treatment_category(catg_link)
                    time.sleep(1)

    # ___

    def data_category(self):
        result_name = False
        error_link = False

        for li in self.content_catg:
            element = li.find('a')
            catg_link: str = self.path + element['href']
            catg_name: str = element.string.strip()
            if catg_name == self.name:
                if not catg_link:
                    error_link = True
                    break
                else:
                    title_category = self.Clean_str.CleanUpString().cleaner_folder_name(catg_name)
                    self.catg_folder = 'pack_stock/Catg_' + title_category + '-(' + str(self.date_fr) + ')'
                    if Folder.FolderCreate(self.catg_folder).error_folder:
                        Ers.ErrorsTreatment("data_treatment_8", catg_name)
                        break
                    else:
                        self.treatment_category(catg_link)
                        result_name = True
                        break

        if not result_name:
            Ers.ErrorsTreatment("data_treatment_9", self.name)
        elif error_link:
            Ers.ErrorsTreatment("data_treatment_10")
        else:
            pass

    # ___

    def data_category_rand(self):
        array_title = []

        for li in self.content_catg:
            element = li.find('a')
            link = self.path + element['href']
            name = element.string.strip()
            if not link or not name:
                continue
            else:
                array_title.append(name + ',' + link)

        if not array_title:
            Ers.ErrorsTreatment("data_treatment_11")
        else:
            category = random.choice(array_title)
            index = category.find(',')
            catg_name: str = category[:index]
            catg_link: str = category[index + 1:]
            if catg_name and catg_link:

                if self.choice == 'category_N':
                    title_category = self.Clean_str.CleanUpString().cleaner_folder_name(catg_name)
                    self.catg_folder = 'pack_stock/Catg_' + title_category + '-(' + str(self.date_fr) + ')'
                    if Folder.FolderCreate(self.catg_folder).error_folder:
                        Ers.ErrorsTreatment("data_treatment_8", catg_name)

                self.treatment_category(catg_link)

            else:
                Ers.ErrorsTreatment("data_treatment_12")

    # ___

    def data_product(self):
        products = self.dom.find("ul", class_="nav-list").find("li").find('a')
        catg_link: str = self.path + products['href']
        if not catg_link:
            Ers.ErrorsTreatment("data_treatment_10", 'tous produits')
        else:
            self.treatment_category(catg_link)

    # ___

    def treatment_category(self, catg_link: any) -> None:

        self.page = Recovery.DataRecovery(catg_link)
        self.dom = BeautifulSoup(self.page.index, 'html.parser')

        if not self.page.index or not self.dom:
            Ers.ErrorsTreatment("data_treatment_13")
        else:

            other_page = self.dom.find('ul', class_='pager')
            if not other_page:
                products = self.dom.find_all('article', class_='product_pod')
                for prd in products:
                    link = prd.find('h3').find('a')
                    link = link['href']
                    if not link:
                        Ers.ErrorsTreatment("data_treatment_14")
                        break
                    else:
                        new_path = self.Clean_str.CleanUpString().cleanup_link(link)
                        prd_link: str = self.path + 'catalogue/' + new_path
                        self.treatment_product(prd_link)
##############
##############
##############
##############
                        print(self.name)
                        print(self.choice + 'a1')
                        if not self.name and self.choice == 'product_N':
                            break
                        else:
                            time.sleep(1)
            else:
                count_page = other_page.find('li', class_='current').string.replace(' ', '').strip()
                index_count = count_page.find('of')
                count_page = int(count_page[index_count + 2:])

                for i in range(count_page):
                    # on laisse passer la page courant
                    if i > 0:
                        index_catg = catg_link.find('index.html')
                        url_catg = catg_link[:index_catg]
                        nbr_page = i + 1
                        extend_path = 'page-' + str(nbr_page) + '.html'
                        next_path = url_catg + extend_path
                        self.page = Recovery.DataRecovery(next_path)
                        self.dom = BeautifulSoup(self.page.index, 'html.parser')

                    if not self.page.index or not self.dom:
                        Ers.ErrorsTreatment("data_treatment_15")
                    else:
                        products = self.dom.find_all('article', class_='product_pod')
                        for prd in products:
                            link = prd.find('h3').find('a')
                            link = link['href']
                            if not link:
                                Ers.ErrorsTreatment("data_treatment_14")
                                break
                            else:
                                new_path = self.Clean_str.CleanUpString().cleanup_link(link)
                                prd_link: str = self.path + 'catalogue/' + new_path
                                self.treatment_product(prd_link)
##############
##############
##############
##############
                                print(self.name)
                                print(self.choice + 'a2')
                                if not self.name and self.choice == 'product_N':
                                    break
                                else:
                                    time.sleep(1)

                    if not self.name and self.choice == 'product_N':
                        break
    # ___

    def treatment_product(self, prd_link=None):

        if not prd_link:
            Ers.ErrorsTreatment("data_treatment_15")
        else:
            self.page = Recovery.DataRecovery(prd_link)
            self.dom = BeautifulSoup(self.page.index, 'html.parser')

            if not self.page.index or not self.dom:
                Ers.ErrorsTreatment("data_treatment_16")
            else:
                product = self.dom.find('div', class_='product_main')
                if not product:
                    Ers.ErrorsTreatment("data_treatment_17")
                else:
                    title_product = product.find('h1').string.strip()
                    title_product = self.Clean_str.CleanUpString().cleaner_folder_name(title_product)
                    print(title_product)

                    if self.choice != 'directory_N' and self.choice != 'category_N':
                        prd_folder = 'pack_stock/' + title_product + '-(' + str(self.date_fr) + ')'
                    else:
                        prd_folder = self.catg_folder + '/' + title_product

                    if Folder.FolderCreate(prd_folder).error_folder:
                        Ers.ErrorsTreatment("data_treatment_18", title_product)
                    else:


                        en_tete = ['Code', 'Lien Description', 'Catégorie', 'Titre', 'Description', 'Prix Ht', 'Prix Ttc',
                               'Lien photo',
                               'Evaluation']



