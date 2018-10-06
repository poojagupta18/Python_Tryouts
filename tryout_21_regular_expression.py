#Regular expressions are mini-language for specifying text patterns.
#Writing code to do pattern matching without regular expression is a huge pain.

#We can recognize by observing 415-433-2222 is a canada phone number. But 232,454,9090 is not a phone number.

#Pattern matching without using Regular Expression. 

def isPhoneNumber(text):        # 415-555-2121
    if len(text) != 12:
        return False            # not phone number- sized
    for i in range (0,3):
        if not text[i].isdecimal():
            return False        # no area code
    if text[3] != '-':
        return False            # missing dash
    for i in range (4,7):
        if not text[i].isdecimal():
            return False        # no middle three digit 
    if text[7] != '-':
        return False            # missing second dash
    for i in range (8,12):
        if not text[i].isdecimal():
            return False       #missing last 4 digits
    return True

print(isPhoneNumber('123-454-9898'))     #O/p: True
print(isPhoneNumber('12-232-909090'))    #     False
print(isPhoneNumber('hello'))            #     False     

# If we want to find the phone number from text we will store the whole text in one variable and divide in chunks of 12 digit to recognize whether phone number is present or not.

message = 'call me 415-898-9090 tomorrow, or at 415-292-8989 today'
foundNumber = False
for i in range (len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found : '+ chunk)
        foundNumber = True
if not foundNumber:
    print('Phone number not found!')
# O/p: Phone number found : 415-898-9090
#     Phone number found : 415-292-8989    

#----------------------------------------------------
# Pattern matching using Regular Expression.        
# import the re module first.
# call the re.compile() function to create a regex object.
# call the regex object's search() method to create a match object.
# call the matched object's group() method to get the matched string.
# \d is the regex for a numberic digit character.

import re

message = 'call me 415-898-9090 tomorrow, or at 415-292-8989 today'

# Regex strings often uses \(backslashes), so they are often a raw strings: r'\d'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

# Output: 415-898-9090     It will print for first occurance of phone number pattern.

# findall() method is used for searching all the patterns within the text.
# findall() return the output in list format only so group() is not required.
message = 'call me 415-898-9090 tomorrow, or at 415-292-8989 today'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message))

# Output:   ['415-898-9090', '415-292-8989']

#----------------------------------------
# Groups are craeted in regex strings with paranthesis,
# The 1st set of paranthesis is group 1, the second is 2, and so on.
# calling group() or group(0) returns the full matching string, group(1) returns group 1's matchimg string, and so on.
# Use \(and \) to match literals paranthesis in the regex string.
# The | pipe can match one of many possible groups.

phoneNumRegex = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('call me 415-898-9090 tomorrow, or at 415-292-8989 today')
print(mo.group())  # O/p: 415-898-9090
print(mo.group(1)) #      415
#print(mo.group(2)) #      IndexError: no such group

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('call me 415-898-9090 tomorrow, or at 415-292-8989 today')
print(mo.group())  # O/p: 415-898-9090
print(mo.group(1)) #      415
print(mo.group(2)) #      898-9090

#If your text contains paranthesis, use \ before paranthesis.

phoneNumRegex = re.compile(r'\(\d\d\d\)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('call me (415)-898-9090 tomorrow, or at 415-292-8989 today')
print(mo.group())  # O/p:  (415)-898-9090
print(mo.group(1)) #       898-9090
#print(mo.group(2)) #      898-9090








        
