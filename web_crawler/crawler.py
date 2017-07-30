#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs


print('enter the website..')
web = input()
print(web)

r = requests.get(web)
# print the status code
print(r.status_code)

# if the website exists
if r.status_code == 200:
    # take all pictures from the website
    code = r.text
    soup = bs(code, "html.parser")
    for image in soup.findAll('img'):
        print('{}'.format(web, image.get('src')))
