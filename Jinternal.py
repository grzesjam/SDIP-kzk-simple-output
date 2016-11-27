import urllib.request
from bs4 import BeautifulSoup


autobus = dict()
licz = 0
red = ''
nrlinii = ''
url = "http://sdip.kzkgop.pl/web/ml/line/"
i = 0
print ('{ "linie" :')

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


redd = red.rsplit('\n', 9)[0].split('\n', 3)[-1]
nrlini = nrlinii.split('\n', 1)[-1]


while (i < licz):

    if(i == 0):
        print ("{")
    print ('"l'+str(i+1)+'" : ')
    print ('{ "linia": "'+nrlini.splitlines()[i]+'", "trans": "'+redd.splitlines()[i]+'"}, ')
    i+=1
print ('"ilosc": '+str(i)+"}}")
