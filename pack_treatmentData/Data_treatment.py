from bs4 import BeautifulSoup
from pack_treatmentData import Data_recovery as Recovery
from pack_tool import Format_date as Fd, CleanUp_string as Clean_str, Folder_create as Folder
from pack_treatmentFile import File_treatment_csv as File_csv, File_treatment_img as File_img
import Errors_treatment as Ers
import random, time, re


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
            self.catg_name = None
            self.catg_title = None
            self.catg_folder = None
            self.catg_link = None

            # self.comparator_text(self.name)

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
                Ers.ErrorsTreatment("data_treatment_4")

        else:
            Ers.ErrorsTreatment("data_treatment_5")

    # ___

    def data_directory(self):
        title_st = self.dom.find("header", {'class': 'header'}).find('a').string.strip()
        title_site = self.Clean_str.CleanUpString().cleaner_folder_name(title_st)
        if not title_site:
            title_site = "Home"

        self.site_folder = 'pack_stock/' + title_site + '-(' + str(self.date_fr) + ')'

        if Folder.FolderCreate(self.site_folder).error_folder:
            Ers.ErrorsTreatment("data_treatment_6")
        else:
            data: dict[str, str] = {
                'action': 'w',
                'path': str(self.site_folder + '/Site.csv'),
                'description': 'Site',
                'prt_name': title_st,
                'prt_lien':  self.path,
                'prd_data': ''
            }

            if not File_csv.FileTreatmentCsv(data).result:
                Ers.ErrorsTreatment("data_treatment_18", 'Fichier Site => ' + title_st)
            else:

                for li in self.content_catg:
                    element = li.find('a')
                    catg_link: str = self.path + element['href']
                    catg_name: str = element.string.strip()
                    if not catg_name or not catg_link:
                        Ers.ErrorsTreatment("data_treatment_7", catg_name)
                        continue
                    else:
                        self.catg_name = catg_name.replace(',', '')
                        self.catg_title = self.Clean_str.CleanUpString().cleaner_folder_name(catg_name)
                        self.catg_folder = self.site_folder + '/Catg_' + self.catg_title
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
                    self.catg_name = catg_name.replace(',', '')
                    self.catg_title = self.Clean_str.CleanUpString().cleaner_folder_name(catg_name)
                    self.catg_folder = 'pack_stock/Catg_' +  self.catg_title + '-(' + str(self.date_fr) + ')'
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
                    self.catg_title = self.Clean_str.CleanUpString().cleaner_folder_name(catg_name)
                    self.catg_folder = 'pack_stock/Catg_' + self.catg_title + '-(' + str(self.date_fr) + ')'
                    if Folder.FolderCreate(self.catg_folder).error_folder:
                        Ers.ErrorsTreatment("data_treatment_8", catg_name)
                        return False

                self.catg_name = catg_name.replace(',', '')
                self.treatment_category(catg_link)

            else:
                Ers.ErrorsTreatment("data_treatment_12")

    # ___

    def data_product(self):
        products = self.dom.find("ul", class_="nav-list").find("li").find('a')
        catg_link: str = self.path + products['href']
        self.catg_name = 'Books'
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
            self.catg_link = catg_link

            dir_data: dict[str, str] = {
                'action': '',
                'path': '',
                'description': 'Categorie',
                'prt_name': self.catg_name,
                'prt_lien': self.catg_link,
                'prd_data': ''
            }

            if self.choice != 'product_N':

                dir_data['action'] = 'w'
                dir_data['path'] = str(self.catg_folder + '/Catg_' + self.catg_title + '.csv')
                if not File_csv.FileTreatmentCsv(dir_data).result:
                    Ers.ErrorsTreatment("data_treatment_18",
                                        'Fichier Catégorie => ' + self.catg_title)

                if self.choice == 'directory_N':
                    dir_data['action'] = 'a'
                    dir_data['path'] = str(self.site_folder + '/Site.csv')
                    if not File_csv.FileTreatmentCsv(dir_data).result:
                        Ers.ErrorsTreatment("data_treatment_18",
                                            'Fichier Site => Catégorie => ' + self.catg_title)

            array_prd = []
            search_name = False
            search = False
            other_page = self.dom.find('ul', class_='pager')
            if not other_page:
                products = self.dom.find_all('article', class_='product_pod')

                if not self.name and self.choice == 'product_N':
                    for prd in products:
                        link = prd.find('h3').find('a')['href']
                        array_prd.append(link)
                else:
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

                        if self.choice == 'product_N':
                            for prd in products:
                                if self.name:
                                    link = prd.find('h3').find('a')['href']
                                    name = prd.find('h3').find('a').string.strip()
                                    name = self.comparator_text(name)
                                    input_name = self.comparator_text(self.name)
                                    if str(name) == str(input_name):
                                        search_name = True
                                        array_prd.append(link)
                                        break
                                    else:
                                        continue
                                else:
                                    link = prd.find('h3').find('a')['href']
                                    array_prd.append(link)
                        else:

                            for prd in products:
                                link = prd.find('h3').find('a')['href']
                                if not link:
                                    Ers.ErrorsTreatment("data_treatment_14")
                                    break
                                else:
                                    new_path = self.Clean_str.CleanUpString().cleanup_link(link)
                                    prd_link: str = self.path + 'catalogue/' + new_path
                                    self.treatment_product(prd_link)
                                    time.sleep(1)
                    if search_name:
                        break

            if self.choice == 'product_N':
                link = ""
                if search_name:
                    link = array_prd[0]
                elif array_prd:
                    link = random.choice(array_prd)
                else:
                    Ers.ErrorsTreatment("data_treatment_20")
                if not link:
                    Ers.ErrorsTreatment("data_treatment_14")
                else:
                    new_path = self.Clean_str.CleanUpString().cleanup_link(link)
                    prd_link: str = self.path + 'catalogue/' + new_path
                    self.treatment_product(prd_link)
                    time.sleep(1)

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
                product = self.dom.find('article', class_='product_page')
                if not product:
                    Ers.ErrorsTreatment("data_treatment_17")
                else:
                    title_prd = product.find('div', class_='product_main').find('h1').string.strip()
                    title_product = self.Clean_str.CleanUpString().cleaner_folder_name(title_prd)

                    if self.choice != 'product_N':
                        prd_folder = self.catg_folder + '/' + title_product
                    else:
                        prd_folder = 'pack_stock/' + title_product + '-(' + str(self.date_fr) + ')'

                    if Folder.FolderCreate(prd_folder).error_folder:
                        Ers.ErrorsTreatment("data_treatment_18", title_product)
                    else:

                        title = title_prd.replace(',', '-')

                        description = product.find_all('p')[3].string
                        if description:
                            new_text = self.Clean_str.CleanUpString().cleaner_order_text_csv(description, 300)
                            if new_text:
                                description = new_text
                            else:
                                description = description.replace(',', ';')
                        else:
                            description = ""

                        data_product = ["Produit", title, prd_link, description]

                        infos_product = product.find('table', class_='table-striped').find_all('tr')
                        for infos in infos_product:
                            key = infos.find('th').string
                            val = infos.find('td').string

                            if key and val:
                                key = key.strip()
                                val = val.strip()

                                if key != 'Product Type' and key != 'Tax':

                                    if key == 'Price (excl. tax)' or key == 'Price (incl. tax)':
                                        devise = val[:1]
                                        val = val[1:]
                                        data_product.append(val)
                                        data_product.append(devise)

                                    elif key == 'Availability':
                                        index = val.find('(')
                                        val = val[index + 1:]
                                        index = val.find('available')
                                        val = val[:index].strip()
                                        data_product.append(val)
                                    else:
                                        data_product.append(val)
                            else:
                                val = ""
                                data_product.append(val)

                        img = product.find('img')['src']
                        new_path = self.Clean_str.CleanUpString().cleanup_link(img)
                        img_link = self.path + new_path
                        data_product.append(img_link)

                        dir_data: dict[str, str] = {
                            'action': '',
                            'path': '',
                            'description': '',
                            'prt_name': '',
                            'prt_lien': '',
                            'prd_data': data_product
                        }

                        if self.choice != 'product_N':
                            dir_data['action'] = 'a'
                            dir_data['path'] = str(self.catg_folder + '/Catg_' + self.catg_title + '.csv')
                            if not File_csv.FileTreatmentCsv(dir_data).result:
                                Ers.ErrorsTreatment("data_treatment_18",
                                                    'Fichier Catégorie => ' + self.catg_title)

                            if self.choice == 'directory_N':
                                dir_data['action'] = 'a'
                                dir_data['path'] = str(self.site_folder + '/Site.csv')
                                if not File_csv.FileTreatmentCsv(dir_data).result:
                                    Ers.ErrorsTreatment("data_treatment_18",
                                                        'Fichier Site => Catégorie => ' + self.catg_title)

                        dir_data['action'] = 'w'
                        dir_data['path'] = str(prd_folder + '/' + title_product + '.csv')
                        dir_data['description'] = 'Categorie'
                        dir_data['prt_name'] = self.catg_name
                        dir_data['prt_lien'] = self.catg_link
                        if not File_csv.FileTreatmentCsv(dir_data).result:
                            Ers.ErrorsTreatment("data_treatment_18",
                                                'Fichier Catégorie => ' + self.catg_name + 'Fichier Produit => '
                                                + title_product)

                        img_data = {
                            'path': str(prd_folder + '/' + title_product),
                            'link': img_link
                        }

                        if not File_img.FileTreatmentImg(img_data).result:
                            Ers.ErrorsTreatment("data_treatment_19",
                                                'Fichier Catégorie => ' + self.catg_name + 'Fichier Produit => '
                                                + title_product + 'Erreur création d\'image')

                        print(title_product)

    def comparator_text(self, value):
        value = str(value)
        value.strip()
        index = value.find('(')
        new_text = value[:index]
        new_text = new_text.replace(' ', '')
        new_text = re.search(r"[a-zA-Z]+", new_text)
        if new_text:
            new_text = new_text.group()
        else:
            new_text = value
        return new_text
