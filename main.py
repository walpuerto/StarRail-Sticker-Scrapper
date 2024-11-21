import urllib.request as UrlRequest
import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://honkai-star-rail.fandom.com/wiki/Pom-Pom_Gallery').text
html_text = BeautifulSoup(html_text, 'lxml')
stickers = html_text.find_all("div", class_ = "wikia-gallery-item")

saveLocation = "C:/Users/Winsor/Documents/GitHub/StarRail-Sticker-Scrapper/stickers"

print("Downloading Stickers...")

links = []
for sticker in stickers:
    parsedLink = str(sticker.find("img")["src"])
    newLink = parsedLink[:len(parsedLink)-57]

    links.append(newLink)

for eachLink in links:
    UrlRequest.urlretrieve(eachLink, f"{saveLocation}/sticker_{links.index(eachLink)}.png")
    print(f"Percent: {int(links.index(eachLink)/len(links)*100)}%", end="\r")

print("")
print("Download Complete!")