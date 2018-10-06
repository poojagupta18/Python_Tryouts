#Regular expressions are mini-language for specifying text patterns. Writing code to do pattern matching without regular expression is a huge pain.

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

print(isPhoneNumber('123-454-9898'))     # True
print(isPhoneNumber('12-232-909090'))    # False
print(isPhoneNumber('hello'))            # False     
