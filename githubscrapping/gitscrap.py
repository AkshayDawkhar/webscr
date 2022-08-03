import  requests
from bs4 import BeautifulSoup

def getlan(lin):
    data=requests.get("https://github.com/"+lin)
    sop=BeautifulSoup(data.content,'html5lib')
    table=sop.find_all("span",{"class":"color-fg-default text-bold mr-1"})
    links=set()
    for i in table:
        links.add(i.text)
    return links



data=requests.get("https://github.com/AkshayDawkhar?tab=repositories")
# print(data.text)
sop=BeautifulSoup(data.content,'html5lib')
table=sop.find_all("a",{"itemprop":"name codeRepository"})

links=set()
datai=[]
# print(table)
for i in table:
    links.add(i.get('href'))
for i in links:
    d={'name':i,"language":getlan(i)}
    datai.append(d)

print("number of repo - ",len(datai))
for i in datai:
    print("name - ",i['name'])
    print("language -",i['language'])
