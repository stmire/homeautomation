"""
TPB Fetch

This script will be used to fetch files from TPB.Once downlaoded, they will be
opened in Tranmission for content retreival.

TO DO:
1. Implement magnet parse
2. Fetch the magent link
3. Download content via Transmission
"""

import subprocess
import sys
import requests
import bs4
import webbrowser
import re

if len(sys.argv) <= 1:
    print("Missing search term")
    exit()
else:
    searchterm = '%20'.join(sys.argv[1:])

hostlink = 'http://www.thepiratebay.org/search/'
searchlink = hostlink + searchterm

magnetRegex = re.compile(r'^magnet+')

request = requests.get(searchlink)
parser = bs4.BeautifulSoup(request.text, "lxml")
magnets = parser.find_all('a', href=True)

matches = []
for magnet in magnets:
    if(magnetRegex.search(magnet['href'])):
        matches.append(magnet)

#print(matches[0]['href'])

subprocess.call(['transmission-cli '+matches[0]['href']], shell=True)
