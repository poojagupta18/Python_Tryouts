import pprint

#The program to count the character.
message = 'It was rainy days in June, unfortunatly I forgot my umbrella.'
count = {}

for character in message:                 #character points to single letters in the string
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)

"""
Output:
{'I': 2, 't': 4, ' ': 10, 'w': 1, 'a': 5, 's': 2, 'r': 4, 'i': 2, 'n': 5, 'y': 4, 'd': 1, 'J': 1, 'u': 4, 'e': 2, ',': 1, 'f': 2, 'o': 3, 'l': 3, 'g': 1, 'm': 2, 'b': 1, '.': 1}
>>>

Here I and i seems different. If we want I and i to be consider as same, we can use upper() on message in for loop
"""
message = 'It was rainy days in June, unfortunatly I forgot my umbrella.'
count = {}

for character in message.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)

"""
Output:
{'I': 4, 'T': 4, ' ': 10, 'W': 1, 'A': 5, 'S': 2, 'R': 4, 'N': 5, 'Y': 4, 'D': 1, 'J': 1, 'U': 4, 'E': 2, ',': 1, 'F': 2, 'O': 3, 'L': 3, 'G': 1, 'M': 2, 'B': 1, '.': 1}
>>> Here I and i are same. so count is 4(i=2 and I=2)
"""

python = """     //triple quotes are used here to store multiline message
Python is a popular programming language. It was created in 1991 by Guido van Rossum.

It is used for:

web development (server-side),
software development,
mathematics,
system scripting.
What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.
Why Python?
Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
Python can be treated in a procedural way, an object-orientated way or a functional way.
Good to know
The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, although not being updated with anything other than security updates, is still quite popular.
In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.
Python Syntax compared to other programming languages
Python was designed to for readability, and has some similarities to the English language with influence from mathematics.
Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.
"""
count = {}

for character in python.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)
    
"""
Output:
{'\n': 28, 'P': 72, 'Y': 47, 'T': 152, 'H': 73, 'O': 139, 'N': 135, ' ': 294, 'I': 104, 'S': 115, 'A': 132, 'U': 44, 'L': 60, 'R': 96, 'G': 45, 'M': 48, 'E': 169, '.': 23, 'W': 36, 'C': 54, 'D': 48, '1': 2, '9': 2, 'B': 21, 'V': 12, 'F': 28, ':': 1, '(': 2, '-': 4, ')': 2, ',': 22, '?': 2, 'K': 5, 'X': 7, 'Q': 2, 'J': 2, '3': 1, '2': 1, ';': 1}
>>>
"""
#Above output looks messy, we can get clean and ordered output using pprint module
#The pprint module's pprint() "pretty print" function can display a dictionary value cleanly.

count = {}

for character in python.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count)

"""
Output:
{'\n': 28,
 ' ': 294,
 '(': 2,
 ')': 2,
 ',': 22,
 '-': 4,
 '.': 23,
 '1': 2,
 '2': 1,
 '3': 1,
 '9': 2,
 ':': 1,
 ';': 1,
 '?': 2,
 'A': 132,
 'B': 21,
 'C': 54,
 'D': 48,
 'E': 169,
 'F': 28,
 'G': 45,
 'H': 73,
 'I': 104,
 'J': 2,
 'K': 5,
 'L': 60,
 'M': 48,
 'N': 135,
 'O': 139,
 'P': 72,
 'Q': 2,
 'R': 96,
 'S': 115,
 'T': 152,
 'U': 44,
 'V': 12,
 'W': 36,
 'X': 7,
 'Y': 47}
>>>
"""
#The pformat() function returns a string value of this output.
count = {}

for character in python.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1

text= pprint.pformat(count)

print(text)
"""
Output:
{'\n': 28,
 ' ': 294,
 '(': 2,
 ')': 2,
 ',': 22,
 '-': 4,
 '.': 23,
 '1': 2,
 '2': 1,
 '3': 1,
 '9': 2,
 ':': 1,
 ';': 1,
 '?': 2,
 'A': 132,
 'B': 21,
 'C': 54,
 'D': 48,
 'E': 169,
 'F': 28,
 'G': 45,
 'H': 73,
 'I': 104,
 'J': 2,
 'K': 5,
 'L': 60,
 'M': 48,
 'N': 135,
 'O': 139,
 'P': 72,
 'Q': 2,
 'R': 96,
 'S': 115,
 'T': 152,
 'U': 44,
 'V': 12,
 'W': 36,
 'X': 7,
 'Y': 47}
{'\n': 28,
 ' ': 294,
 '(': 2,
 ')': 2,
 ',': 22,
 '-': 4,
 '.': 23,
 '1': 2,
 '2': 1,
 '3': 1,
 '9': 2,
 ':': 1,
 ';': 1,
 '?': 2,
 'A': 132,
 'B': 21,
 'C': 54,
 'D': 48,
 'E': 169,
 'F': 28,
 'G': 45,
 'H': 73,
 'I': 104,
 'J': 2,
 'K': 5,
 'L': 60,
 'M': 48,
 'N': 135,
 'O': 139,
 'P': 72,
 'Q': 2,
 'R': 96,
 'S': 115,
 'T': 152,
 'U': 44,
 'V': 12,
 'W': 36,
 'X': 7,
 'Y': 47}
>>>
"""
