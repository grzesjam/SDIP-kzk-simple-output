#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import sys
import json

autobus = dict()
licz = 0
red = ''
nrlinii = ''
url = "http://sdip.metropoliaztm.pl/web/ml/line/"
i = 0
arg = str(sys.argv[1])

listalini = [0] * 1000

with urllib.request.urlopen(url) as response:
    html = response.read()

soup = BeautifulSoup(str(html, "utf-8"), "html.parser")
liki = (soup.findAll('li'))
lika = (soup.findAll('a'))
for line in liki:
        nrtmp = (line.findAll('a')[0].text.strip())
        nrlinii = (nrlinii+"\n"+nrtmp)
        licz += 1


for line in lika:
    href = (line.get('href'))
    nron = (href[13:])
    red = (red+"\n"+nron)


redd = red.rsplit('\n', 9)[0].split('\n', 3)[-1] #zawsze liczba
nrlini = nrlinii.split('\n', 1)[-1]


while (i < licz):
    #print(nrlini.splitlines()[i]+" "+redd.splitlines()[i] +' | ')
    #listalini.insert(int(redd.splitlines()[i]), nrlini.splitlines()[i])
    #print(listalini.index(redd.splitlines()[i]))
    #print (listalini)
    #for index, elem in enumerate(listalini):
    #    print(index, elem)
    listalini[int(redd.splitlines()[i])] = (nrlini.splitlines()[i])
    i+=1

argu = str(listalini.index(arg))


##
##
##   tutaj jest KZK.py
##
##


autobusy = dict()
urlbus = dict()
vehicle = dict()
soup = dict()


url = "http://sdip.metropoliaztm.pl/web/map/vehicles/gj/A?route_id="+argu
#print (url)
with urllib.request.urlopen(url) as response:
    html = response.read()
htmlu = str(html, 'utf-8')
data = json.loads(htmlu)

islong = (len(data['features']))

if (islong >= 1):
    for i in range(0, len(data['features'])):
        autobusy[i] = data['features'][i]['id']
        #print ("http://sdip.metropoliaztm.pl/web/ml/map/vehicles/"+str(autobusy[i]))
        urlbus[i] = "http://sdip.metropoliaztm.pl/web/ml/map/vehicles/"+str(autobusy[i])

else:
    print ("False")



# mam ID teraz biore dane

for i in urlbus:
    with urllib.request.urlopen(urlbus[i]) as response:
        vehicle[i] = response.read()
        soup[i] = BeautifulSoup(str(vehicle[i], "utf-8"), "html.parser")


for i in soup:
    localna = (soup[i])
    #print(localna.find_all('td')[1].text), print(localna.find_all('td')[6].text)
    #print(str(localna.find_all("td")[3]), 'utf-8')
    #print(str(localna.find_all("td")[4]), 'utf-8')
   # print (localna)
    try:
        print(localna.findAll('td')[1].text.strip()+" - ")
    except IndexError:
        print ("?linia?"+" - ")
    try:
        print(localna.findAll('td')[3].text.strip()+" / ")
    except IndexError:
        print("?nast przystanek?"+" / ")
    try:
        print(localna.findAll('td')[4].text.strip()+" | ")
    except IndexError:
        print ('?opuźnienie?'+" | ")
