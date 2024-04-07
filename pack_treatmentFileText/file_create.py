from bs4 import BeautifulSoup
import csv
import json




# EN COURS




# if __name__ == '__main__':
url = "https://www.gov.uk/search/news-and-communications"
response = requests.get(url)
page = response.content

soup = BeautifulSoup(page, "html.parser")

title = soup.title

# class_name = "gem-c-document-list__item-link"
titres = soup.find_all("a", class_="govuk-link")
titre_texts = []
for title in titres:
    titre_texts.append(title.string)

descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
description_texts = []
for description in descriptions:
    description_texts.append(description.string)

en_tete = ['titre', 'description']
with open("pack_csv/essai.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete)
    for titre, description in zip(titre_texts, description_texts):
        writer.writerow([titre, description])


        print(title)

        """from urllib.request import urlopen
        from urllib.error import URLError"""

