import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")

titres = soup.find_all("a", class_="govuk-link")
titre_textes = []
for titre in titres:
    titre_textes.append(titre.string)

descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
description_textes = []
for description in descriptions:
    description_textes.append(description.string)

en_tete = ['title', 'description']
with open('data.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete)
    for titre, description in zip(titre_textes, description_textes):
        writer.writerow([titre, description])