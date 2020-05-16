# Core Modules
import datetime 
from datetime import date
import time 
from time import time 

# Pip Modules 

from camelcase import CamelCase

# import custom modules 
import validator
from validator import validate_email

# today = datetime.date.today()

today = date.today()

timeStamp = time()

c = CamelCase()
# print(c.hump('hello there world'))


email = 'test#test.com'
if validate_email(email):
    print("Email is valid")
else:
    print('Email is bad')

