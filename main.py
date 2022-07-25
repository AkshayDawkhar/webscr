from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

#geting input 
url=str(input("Enter the link : "))

#adding .html if not 
if not url.endswith('html'):
    url=url+'.html' if url.endswith('/') else url+'/.html'



#requesting url 
if not url.startswith('http'):
    try:
     print("finding links "+'https://'+url,end=' ---->\n')
     data=requests.get('https://'+url)
    except :
        try:
          print("finding links "+'http://'+url,end=' ---->\n')  
          data=requests.get('http://'+url)
        except :
            pass
else:
    print("finding links "+url,end=' ---->\n')
    data=requests.get(url)

sop=BeautifulSoup(data.content,'html5lib')
table=sop.find_all('a')
 
 #geting domain name to add in the link
domain = urlparse(url).netloc

#making set to store links
links=set()

for i in table:
    links.add(i.get('href'))#geting only href part 

for i in links:
    if i.startswith('https://') or i.startswith('http://'): #formating string 
        print(i)
    else:
        print((url[0:8] if url.startswith('https:') else url[0:7])+domain+i)