# ^ means the string must start with the pattern.

# $ means the string must end with the pattern.

# Both means the entire string must match the pattern.

>>> import re
>>> beginWithHelloRegex = re.compile(r'^Hello')
>>> beginWithHelloRegex.search('Hello there!')
<re.Match object; span=(0, 5), match='Hello'>
>>> beginWithHelloRegex.search('He said "Hello!"')
>>> beginWithHelloRegex.search('He said "Hello"') == None
True
>>> endsWithWorldregex = re.compile(r'world!$')
>>> endsWithWorldregex.search('Hello world!')
<re.Match object; span=(6, 12), match='world!'>
>>> endsWithWorldregex.search('Hello world! hiiii')
>>> endsWithWorldregex.search('Hello world! hiiii') == None
True
>>>

# Following pattern suggests it is of digits only.

>>> allDigitRegex = re.compile(r'^\d+$')
>>> allDigitRegex.search('233218977443')
<re.Match object; span=(0, 12), match='233218977443'>
>>> 

>>> allDigitRegex.search('233218n977443') == None
True

# . means anything except newline.
>>> atRegex = re.compile(r'.at')
>>> atRegex.findall('The cat in the Hat sat on the flat mat')
['cat', 'Hat', 'sat', 'lat', 'mat']
>>> 

# Here f of flat is not outputted as . shows for only one character. So, .{1,2} is used for 1 or 2 character.

>>> atRegex = re.compile(r'.{1,2}at')
>>> atRegex.findall('The cat in the Hat sat on the flat mat')
[' cat', ' Hat', ' sat', 'flat', ' mat']
>>> 
