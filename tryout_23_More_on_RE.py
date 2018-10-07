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
# The * says the group matches zero or more times.
# The curly braces can match a specific number of times.
# The curly braces with two numbers matches a minimum and maximum number of times.
# Leaving out the first or second number in the curly braces says there is no minimum or maximum.
# This tryout is performed on Python Idle(Note: >>> shows commands performed on Idle)
# ? (Zero or one)
