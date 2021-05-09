#Web scrapping
import requests
from bs4 import BeautifulSoup
url='https://people.aalto.fi/ayushree.ayushree'
#Ping and in response getting the webpage copy
response=requests.get(url)
#parse the html document
soup=BeautifulSoup(response.text,'lxml')
links=soup.find_all('a',class_='clickItem personViewDetailItem')
for link in links:
  print(link.text)
profile=soup.find_all('span',class_='editTitle')
for prof in profile:
  print(prof.text)
keywords=soup.find_all('div',class_='clickItem keyword')
for key in keywords:
  print(key.text)