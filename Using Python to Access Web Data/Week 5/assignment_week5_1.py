from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
data = urlopen(url, context=ctx).read()

tree = ET.fromstring(data)

sum = 0
comments = tree.findall('.//count')

for comment in comments:
    sum += int(comment.findtext('.'))

print(sum)
