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

# Twilio API key
accountSID = "AC1c552895cf6c584a0579d209995c59da"

# Twilio API token
authToken = "5b6bd8b5e4b33c6e8d73c371f03bfe45"

# Create TwilioRestClient object
smsClient = TwilioRestClient(accountSID, authToken)

# Twilio API number which acts as the sender
twilioNum = '+12512200158'

# My cell number which acts as the receiver
myNum = '+19176917636'

# Body to be sent
message = "Today's price of silver in USD: " + str(price)

# Execute and send SMS to receiving number
sms = smsClient.messages.create(body=message, from_=twilioNum, to=myNum)
