import requests
from bs4 import BeautifulSoup

#date = input("Please enter a date in this format YYYY-MM-DD: ")

date = "2001-08-13"
billboard_url = "https://www.billboard.com/charts/hot-100/"
billboard_url = billboard_url + f"{date}/"

billboard_response = requests.get(url=billboard_url).text

soup = BeautifulSoup(billboard_response, "html.parser")

h3_tags = soup.select(selector="li h3", class_="o-chart-results-list__item")

songs = []

for i in range(0,100):

    songs.append(h3_tags[i].text.strip())

