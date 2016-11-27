import json
import urllib.request
import sys
from bs4 import BeautifulSoup

autobus = dict()
urlbus = dict()
vehicle = dict()
soup = dict()
arg = str(sys.argv[1])

url = "http://sdip.kzkgop.pl/web/map/vehicles/gj/A?route_id="+arg
#print (url)
with urllib.request.urlopen(url) as response:
    html = response.read()
htmlu = str(html, 'utf-8')
data = json.loads(htmlu)

islong = (len(data['features']))

if (islong >= 1):
    for i in range(0, len(data['features'])):
        autobus[i] = data['features'][i]['id']
        #print ("http://sdip.kzkgop.pl/web/ml/map/vehicles/"+str(autobus[i]))
        urlbus[i] = "http://sdip.kzkgop.pl/web/ml/map/vehicles/"+str(autobus[i])

else:
    print ("False")



# mam ID teraz biore dane

for i in urlbus:
    with urllib.request.urlopen(urlbus[i]) as response:
        vehicle[i] = response.read()
        soup[i] = BeautifulSoup(str(vehicle[i], "utf-8"), "html.parser")


# for i in vehicle:
#    print ("|")
#    print (str(vehicle[i],'utf-8').split(">",33)[33].rsplit("<", 5)[0].strip())
for i in soup:
    localna = (soup[i])
    #print(localna.find_all('td')[1].text), print(localna.find_all('td')[6].text)
    #print(str(localna.find_all("td")[3]), 'utf-8')
    #print(str(localna.find_all("td")[4]), 'utf-8')
    print(localna.findAll('td')[1].text.strip()+" - ")
    print(localna.findAll('td')[3].text.strip()+" / ")
    print(localna.findAll('td')[4].text.strip()+" | ")


