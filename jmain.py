import json
import sys
import urllib.request

from bs4 import BeautifulSoup

autobus = dict()
licz = 0
red = ''
nrlinii = ''
url = "http://sdip.kzkgop.pl/web/ml/line/"
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


url = "http://sdip.kzkgop.pl/web/map/vehicles/gj/A?route_id="+argu
#print (url)
with urllib.request.urlopen(url) as response:
    html = response.read()
htmlu = str(html, 'utf-8')
data = json.loads(htmlu)

islong = (len(data['features']))

if (islong >= 1):
    for i in range(0, len(data['features'])):
        autobusy[i] = data['features'][i]['id']
        #print ("http://sdip.kzkgop.pl/web/ml/map/vehicles/"+str(autobusy[i]))
        urlbus[i] = "http://sdip.kzkgop.pl/web/ml/map/vehicles/"+str(autobusy[i])

else:
    print ("False")



# mam ID teraz biore dane

for i in urlbus:
    with urllib.request.urlopen(urlbus[i]) as response:
        vehicle[i] = response.read()
        soup[i] = BeautifulSoup(str(vehicle[i], "utf-8"), "html.parser")

print ('{ "autobusy": {')
for i in soup:
    na=0
    localna = (soup[i])
    idk = i + 1
    if (i!=0):
        print (",")
    print ('"a'+str(idk)+'": {')
    #print (localna)
    try:
        print('"linia": "'+localna.findAll('td')[na+1].text.strip()+'",')
    except IndexError:
        print ("<tr><td> ?linia? </td>")
        na= na - 1
    try:
        print('"nastprzy": "'+localna.findAll('td')[na+3].text.strip()+'",')
    except IndexError:
        print("<td> ?nast przystanek? </td>")
        na = na - 1

    ####### OSTATNI PRZYSANEK ######
    aa = localna.encode("utf-8")
    ab = str(aa, "utf-8")
    bb = (ab[200:])
    bc = BeautifulSoup(bb, "html.parser")
    for link in bc.findAll('a'):
        hrefy = (link.get('href'))
        ulrk = ("http://sdip.kzkgop.pl" + hrefy)
        with urllib.request.urlopen(ulrk) as response:
            html = response.read()
            soupy = BeautifulSoup(str(html, "utf-8"), "html.parser")

        for linki in soupy.findAll('span'):
            spany = (linki.get('span'))
            print('"ostprzy": "'+ str(linki)[6:-7] + '",')
            break

    ###### KONIEC ######


    try:
        print('"opu": "'+localna.findAll('th')[na+4].text.strip()+' '+localna.findAll('td')[na+4].text.strip()+'",')
    except IndexError:
        print('"opu": "?opóźnienie?",')
        na = na - 1

        #### tutaj częsc do kiedy ###

    journ = (localna.findAll('a'))
    for linee in journ:
        href = (linee.get('href'))
        nron = (href[0:])
    print('"kiedyid": "'+nron[26:]+'"}')

print ('}, "ilosc":'+str(idk)+'}')







