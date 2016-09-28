"""
TPB Fetch

This script will be used to fetch files from TPB.Once downlaoded, they will be
opened in Tranmission for content retreival.

TO DO:
1. Implement amgent parse
2. Fetch the magent link
3. Download content via Transmission
"""

import os
import sys
import requests
import bs4
import webbrowser

if len(sys.argv) <= 1:
    print("Missing search term")
    exit()
else:
    searchterm = '%20'.join(sys.argv[1:])

hostlink = 'http://www.thepiratebay.org/search/'
searchlink = hostlink + searchterm

request = requests.get(searchlink)
parser = bs4.BeautifulSoup(request.text, "lxml")
magnets = parser.select('a')
