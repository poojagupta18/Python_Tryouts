# The regex method findall() is passed a string, and returns all matches in it, not just first match.
>>> import re
>>>>>> resume = '''
ABC
Phone: 723-525-5555
Home : 424-898-9009
Email: abc@ls.com

OBJECTIVE: Registered Medical Laboratory Technician requiring extensive experience with success in pediatrics and at a trauma emergency hospital.

SUMMARY OF SKILLS AND EXPERIENCE

LAB TECHNICIAN-- Highly skilled lab technologist with experience serving ER, Urgent Care, Pediatric ER, and Stab-Room Trauma Unit.  Processed cultures in microbiology, gram stains, urinalysis and various manual tests.

PHLEMBOTOMY-- Inpatient and outpatient, pre-op and post-op, blood draws.  Recognized for exceptional skill in serving hard-to-draw patients and children.

INSTRUMENT MAINTENANCE-- Skilled in troubleshooting and maintenance of technical equipment.

TEACHING-- Responsible for training staff on equipment operation and procedures.

QUALITY CONTROL—Maintained high quality standards with an emphasis on accuracy.  Maximized performance through organization, equipment testing, and procedures development.'''
>>> phoneRegex.search(resume)
<re.Match object; span=(12, 24), match='723-525-5555'>
>>>
# Search method always returns 1st match.

# findall() returns list of strings matching the pattern.

>>> phoneRegex.findall(resume)
['723-525-5555', '424-898-9009']
>>>


# If the regex has no groups(0 or 1), findall() returns a list of string.

# If the regex has 2 or more groups, findall() returns a list of tuples of strings.

>>> phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> phoneRegex.findall(resume)
[('723', '525-5555'), ('424', '898-9009')]
>>>

# you can see no dash(-) in output as - is not in group.

# To obtain whole string as well :

>>> phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
>>> phoneRegex.findall(resume)
[('723-525-5555', '723', '525-5555'), ('424-898-9009', '424', '898-9009')]
>>>
# \d can be represent as 0|1|2|3|4|5|6|7|8|9

# \d is shorthand character class that matches digits.

# \w is shorthand character class that matches characters.

# \s matches whitespaces characters.

# The uppercase shorthand characters \D, \W. \S match characters that are not digits, word characters and spaces.

>>> spellingRegex = '''
 1 one,2 two,3 three,4 four,5 five,6 six,7 seven,8 eight,9 nine,10 ten.'''
>>> spellRegex = re.compile(r'\d+\s\w+')
>>> spellRegex.findall(spellingRegex)
['1 one', '2 two', '3 three', '4 four', '5 five', '6 six', '7 seven', '8 eight', '9 nine', '10 ten']
>>> 

# You can make your own character classes with [aieuo]. [a-z] can be used to find any character between a to z(similar for A-Z).

>>> vowelRegex = re.compile(r'[aieouAEIOU]')
>>> voweelRegex.findall('Today is wenEsDAy.')
>>> vowelRegex.findall('Today is wenEsDAy.')
['o', 'a', 'i', 'e', 'E', 'A']
>>> vowelRegex = re.compile(r'[^aieouAEIOU]')

# To match exactly two vowels.
>>> vowelRegex.findall('Tooday is wednesDAy.')
['oo']
>>> 

# A ^ caret makes it a negative character class, matching anything not in [^aieou]

>>> vowelRegex.findall('Today is wenEsDAy.')
['T', 'd', 'y', ' ', 's', ' ', 'w', 'n', 's', 'D', 'y', '.']
>>> 
