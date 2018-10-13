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

# findall() returns all the matched string within the list.

>>> phoneRegex.findall(resume)
['723-525-5555', '424-898-9009']
>>>


# If the regex has no groups(0 or 1), findall() returns a list of string.

# If the regex has 2 or more groups, findall() returns a list of tuples of strings.

# \d is shorthand character class that matches digits.

# \w is shorthand character class that matches characters.

# \s matches whitespaces characters.

# The uppercase shorthand characters \D, \W. \S match characters that are not digits, word characters and spaces.

# You can make your own character classes with [aieuo]

# A ^ caret makes it a negative character class, matching anything not in [^aieou]
