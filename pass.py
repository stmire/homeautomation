'''
16-Character Strong Password Generator

This script will genarate a 16-character password
using a mix of random lowercase letters and numerical digits

Once created, the password will be stored into a text file
with a descriptive label
'''

import os
import random
import string

def passgen():
    passlength = 16
    password = ""
    characters = string.ascii_lowercase + string.digits
    charlength = len(characters)
    for i in range(passlength):
        rnum = random.randrange(0, charlength)
        password = password + characters[rnum]
    return password

def addentry(entry):
    passwrite = open('passes.txt', 'a')
    passwrite.write(entry + '\n')

label = raw_input('Password for: ')
password = passgen()
entry = label + ': ' + password
addentry(entry)
