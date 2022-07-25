from urllib.parse import urlparse

 # --> www.example.test

url='https://www.codewithharry.com/tutorial/css-home.html'
# print(len(url))

domain = urlparse(url).netloc
print(domain)
