import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')

while True:
    if len(url) < 1: break

    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print('Retrieved', len(data), 'characters')
    js = json.loads(data)

    sum = 0
    for comment in js['comments']:
        sum += int(comment['count'])

    print('Sum =', sum)
    break
