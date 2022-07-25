from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

url=str(input("Enter the link : "))
if not url.endswith('html'):
    url=url+'.html' if url.endswith('/') else url+'/.html'

print("finding links "+url,end=' ---->\n')
data=requests.get(url)
sop=BeautifulSoup(data.content,'html5lib')
table=sop.find_all('a')

domain = urlparse(url).netloc
links=set()

for i in table:
    links.add(i.get('href'))

for i in links:
    if i.startswith('https://') or i.startswith('http://'):  
        print(i)
    else:
        print((url[0:8] if url.startswith('https:') else url[0:7])+domain+i)