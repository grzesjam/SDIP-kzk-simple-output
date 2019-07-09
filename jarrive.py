import urllib.request
from bs4 import BeautifulSoup
import sys
import datetime

i = 0
arg = str(sys.argv[1])

now = datetime.datetime.now()


with urllib.request.urlopen("http://sdip.metropoliaztm.pl/web/ml/timetable/journey/"+arg) as response:
    respo = response.read()
    soupa = BeautifulSoup(str(respo, "utf-8"), "html.parser")
    likea = (soupa.findAll('tr', style=False))

print ('{ "przyja": {')


if (i != 0): print (",")

nu = int(0)
for line in likea:
    locl= str(line.text)
    if ((str(line).splitlines()[2][:6]) == "<span>"):
        continue
    if (nu != 0):
        dodtime = locl.splitlines()[5][:2]
        try:
            dodaczas = int(dodtime)
        except ValueError:
            dodaczas = int(0)
        dodane = now + datetime.timedelta(minutes = dodaczas)
        print('"przystanek'+str(nu)+'": "'+locl.splitlines()[2]+'", "czas'+str(nu)+'": "' + str(dodane.strftime("%H"))+":"+str(dodane.strftime("%M"))+'",')
    nu += 1
print ('"liczba": "'+ str(nu-1) + '"}}')
