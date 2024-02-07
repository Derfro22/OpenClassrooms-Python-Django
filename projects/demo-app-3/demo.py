import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.hotmail.com')
soup = BeautifulSoup(r.text, features="html.parser")
print(soup.text)