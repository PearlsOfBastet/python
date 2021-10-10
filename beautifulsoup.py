# pip install beautifulsoup4 eklentisini yüklemeliyiz.
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?sort=ir,desc&mode=simple&page=1"

html = requests.get(url).content
#content = response.content

soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {"class" : "lister-list"}).find_all("tr", limit=250)
count = 0
for tr in list:
    title = tr.find("td", {"class" : "titleColumn"}).find("a").text
    #print(title)
    year = tr.find("td", {"class" : "titleColumn"}).find("span").text.strip("()")
    #print(title,year)
    rating = tr.find("td", {"class" : "ratingColumn imdbRating"}).find("strong").text
    #print(title, year, rating)
    print(f"{count}- film: {title.ljust(100)} yıl: {year} değerlendirme: {rating}")
    count +=1

#print(html)
#print(list)