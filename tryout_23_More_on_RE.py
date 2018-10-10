# This tryout is performed on Python Idle(Note: >>> shows commands performed on Idle)
# ? (Zero or one)

# The ? says the group matches zero or one times.

>>> import re
>>> 
>>> batRegex = re.compile(r'Batman|Batwoman')
>>> mo = batRegex.search('Batman')
>>> mo.group()
'Batman'
>>> 

#Above same example Using ?

>>> batRegex = re.compile(r'Bat(wo)?man') # ? says wo can appear zero or one times.
>>> mo = batRegex.search('Batwoman')
>>> mo.group()
'Batwoman'
>>> mo = batRegex.search('Batman')
>>> mo.group()
'Batman'
>>>
>>> mo = batRegex.search('Adventure of Batman')
>>> mo.group()
'Batman'
>>> mo = batRegex.search('Adventure of Batwowowwoman')
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo == None
True
>>>
# Lets consider the example of phone number which doesn't contain area code.
>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d')  #(\d\d\d-)? It says, preceding group is optional.
>>> mo = phoneRegex.search('My phone number is 245-222-2222')
>>> mo.group()
'245-222-222'

>>> mo = phoneRegex.search('My phone number is 222-2222. Call me Tomorrow.')
>>> mo.group()
'222-222'
>>> 

# The + says the group matches one or more times.
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> batRegex.search('The adventure of Batwoman')
<re.Match object; span=(17, 25), match='Batwoman'>
>>> batRegex.search('The adventure of Batwowowoman')
<re.Match object; span=(17, 29), match='Batwowowoman'>
>>> batRegex.search('The adventure of Batman')
>>> mo = batRegex.search('The adventure of Batman')
>>> mo == None
True
>>> 

# The * says the group matches zero or more times.
>>> 
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> batRegex.search('The adventure of Batman')
<re.Match object; span=(17, 23), match='Batman'>
>>> batRegex.search('The adventure of Batwoman')
<re.Match object; span=(17, 25), match='Batwoman'>
>>> batRegex.search('The adventure of Batwowowoman')
<re.Match object; span=(17, 29), match='Batwowowoman'>
>>>

# Escaping ? * +  (preceed the ? * + by \)

>>> regex = re.compile(r'\+\*\?')
>>> regex.search('I learned about +*? regex syntax')
<re.Match object; span=(16, 19), match='+*?'>
>>>
>>> regex = re.compile(r'(\+\*\?)+')
>>> regex.search('I learned about +*?+*?+*? regex syntax')
<re.Match object; span=(16, 25), match='+*?+*?+*?'>
>>> 

# The curly braces can match a specific number of times. ({x})

>>> haRegex = re.compile(r'(HaHaHa)')
>>> haRegex.search('He said "HaHaHaHa"')
<re.Match object; span=(9, 15), match='HaHaHa'>
>>>

# Above same example using {}:

>>> haRegex = re.compile(r'(Ha){3}')
>>> haRegex.search('He said "HaHaHaHa"')
<re.Match object; span=(9, 15), match='HaHaHa'>
>>> 
>>> phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
>>> phoneRegex.search('My Numbers are 456-2222,222-333-1212 111-121-2121')
>>> phoneRegex.search('My Numbers are 456-2222,222-333-1212,111-121-2121')
<re.Match object; span=(15, 49), match='456-2222,222-333-1212,111-121-2121'>
>>>

# {X,Y} at least X, at most Y  It will return match between 3 and 5, even if we write string matched more than 5, it will return 5 times only.
>>> haRegex = re.compile(r'(Ha){3,5}')
>>> haRegex.search('He said "HaHaHaHa"')
<re.Match object; span=(9, 17), match='HaHaHaHa'>
>>> haRegex.search('He said "HaHaHa"')
<re.Match object; span=(9, 15), match='HaHaHa'>
>>> haRegex.search('He said "HaHaHaHaHaHaHaHa"')
<re.Match object; span=(9, 19), match='HaHaHaHaHa'> #returns match 5 times.
>>> 
# The curly braces with two numbers matches a minimum and maximum number of times.
# Leaving out the first or second number in the curly braces says there is no minimum or maximum.
# Greedy match (by default match is greedy, returns max. length match)
>>> digitRegex = re.compile(r'\d{3,5}')
>>> digitRegex.search('1234567890')
<re.Match object; span=(0, 5), match='12345'>

# un-greedy match (uses ? and returns smallest length match) 
>>> digitRegex = re.compile(r'\d{3,5}?')
>>> digitRegex.search('1234567890')
<re.Match object; span=(0, 3), match='123'>
>>> 
