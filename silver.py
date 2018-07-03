'''
This script can be used to scrape Quandl for the current silver price
and send an SMS message to a personal phone number
'''

import urllib
import json
from twilio.rest import TwilioRestClient

# Link to current prices on Quandl in JSON format
url = 'https://www.quandl.com/api/v1/datasets/LBMA/SILVER.json'

# Get and load the JSON file as a dictionary
response = urllib.urlopen(url)
silverJSON = json.loads(response.read())

# Store the day's current price
price =  silverJSON['data'][0][1]

# Twilio account ID
accountSID = '' # INSERT ACCOUNT ID HERE

# Twilio API key
authToken = '' # INSERT API TOKEN HERE

# Create TwilioRestClient object
smsClient = TwilioRestClient(accountSID, authToken)

# Twilio API number which acts as the sender
twilioNum = '' # INSERT TWILIO GENERATED NUMBER HERE

# My cell number which acts as the receiver
myNum = '' # INSERT PERSONAL CELL HERE

# Body to be sent
message = "Today's price of silver in USD: " + str(price)

# Execute and send SMS to receiving number
sms = smsClient.messages.create(body=message, from_=twilioNum, to=myNum)
