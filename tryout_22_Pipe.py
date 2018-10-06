# The | pipe is used to match one of many possible groups.
import re

batRegex = re.compile('Bat(man|mobile|copter|girl)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())      # O/p: Batmobile

mo = batRegex.search('Badmobilecycle lost wheel')
# print(mo.group())  -AttributeError: 'NoneType' object has no attribute 'group'
# If search() doesn't find pattern in text it returns None, if we call group() on such matched object(none) it throws above error.
if mo == None:
    print('Pattern is not present.')
