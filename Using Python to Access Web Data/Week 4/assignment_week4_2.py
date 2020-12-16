from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
position = int(input('Enter position - '))
repeat = int(input('Enter repeat - '))

print ('Retrieving:',url)

while repeat > 0:

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    count = 1

    tags = soup('a')
    for tag in tags:
        if count == position:
            url = tag['href']
            break
        count += 1

    print ('Retrieving:',url)

    repeat -=1
