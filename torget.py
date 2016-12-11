"""
TPB Fetch

This script will be used to fetch files from TPB. Once downloaded, they will be
opened in Tranmission for content retreival.
"""

import subprocess
import requests
import sys
import bs4
import re

# Get command line args and store into search string
# Exit if amount if arguments is insufficient
if len(sys.argv) <= 1:
    print("Missing search term")
    exit()
else:
    search_term = '%20'.join(sys.argv[1:])

# Link to Pirate Bay search utlity
url_base = 'http://www.thepiratebay.org/search/'

# Create full search URL
search_url = url_base + search_term

# Regex which will be used to only scrape for magent links
magnetRegex = re.compile(r'^magnet+')

# Scrape the entire search results table for all links/URLs
request = requests.get(search_url)
parser = bs4.BeautifulSoup(request.text, "lxml")
magnets = parser.find_all('a', href=True)

# Iterate through URL list and store magnet links to another list
matches = []
for magnet in magnets:
    if(magnetRegex.search(magnet['href'])):
        matches.append(magnet)

# Print first magnet link
print(matches[0]['href'])

# Use the first magnet link with Transmission-CLI to download the contents
# of the torrented link
subprocess.call('transmission-cli ' + matches[0]['href'], shell=True)
