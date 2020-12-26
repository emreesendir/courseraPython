import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['key'] = api_key
    parms['address'] = address
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print('place_id =', js['results'][0]['place_id'])
