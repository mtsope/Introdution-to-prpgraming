from ast import Num
import re

phoneNumber = "800-555-1212  #This is my phone number"

phoneNumberClean = re.sub(r'#.*$', "", phoneNumber)
print(phoneNumberClean)

num = re.sub(r'\D', "", phoneNumber)
print(num)