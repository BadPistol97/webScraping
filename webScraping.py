from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://www.askhargapedia.com/"
html=urlopen(url)
	
page = BeautifulSoup(html,'lxml')

test = page.select(".media-logo a")

aFile = open("theLinks.txt","w+")

for x in test:
	aFile.write(x.get("href"))
	aFile.write("\n")

aFile.close()