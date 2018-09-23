#More about string:
#String can begin and end with double quotes.
>>> 'Hello'
'Hello'
>>> 'That is Alice's cat.'
SyntaxError: invalid syntax
>>> "That is Alice's cat."
"That is Alice's cat."
>>> 'That is Alic\'s cat'
"That is Alic's cat"
>>>

#Escape character let you put quotes and other character that are hard to type inside strings.
-------------------------------------------
#Escape character  | print as
-------------------------------------------
\'                 |  Single quote
\"                 |  Double quote
\t                 | Tab
\n                 |  Newline (line break)
\\                 | Backslash
--------------------------------------------
>>> print('Hello there!\nHow are you?\nI\'m fine.')
Hello there!
How are you?
I'm fine.
>>>
#Strings within ''' or """ is considered as multiline string

>>> print("""Dear friends,
we are celebrating b\'dy today.
we will be having yummy snaks as well.
""")
Dear friends,
we are celebrating b'dy today.
we will be having yummy snaks as well.

>>> 

>>> 'Hello world!'
'Hello world!'
>>> spam = 'Hello world!'
>>> spam[0]
'H'
>>> spam[1:5]
'ello'
>>> spam[-1]
'!'
#in and not in are used to check whether specific string is present or not
>>> 'Hello' in spam
True
>>> 'X' in spam
False
>>> 'HELLO' in spam
False
>>> 
