#This tryout is about different string methods.
#[>>> means they are carried out on python Idle]
>>> spam = 'Hello world!'
>>> spam.upper()
'HELLO WORLD!'
>>> spam
'Hello world!'
>>> spam = spam.upper()
>>> spam
'HELLO WORLD!'
>>> spam.upper()
'HELLO WORLD!'
>>> spam.lower()
'hello world!'
>>> answer = input()
yes
>>> answer
'yes'
>>> answer = input()
YES
>>> answer
'YES'
>>> answer.lower() == 'yes'
True
>>> answer = 'yEs'
>>> if answer.lower == 'yes':
	print('Playing again')

	
>>> if answer == 'yes':
	print('playing again')

	
>>> if answer.lower() == 'yes':
	print('playing again')

	
playing again
>>> spam = 'Hello world!'
>>> spam.islower()


False
>>> spam = 'hello world!'
>>> spam.islower()
True
>>> spam = 'HELLO WORLD!'
>>> spam.isupper()
True
>>> spam = ''
>>> spam.isupper
<built-in method isupper of str object at 0x0011C9A0>
>>> 
>>> spam.isupper()
False
>>> spam.islower()
False
>>> '1234'.islower()
False
>>> '1234'.isupper()
False
>>> 'HELLO'.upper()
'HELLO'
>>> 'Hello'.upper().isupper()
True
>>> '1234'.upper()
'1234'
>>> '1234'.lower()
'1234'
>>> '1234'.lower().islower()
False
>>> '1234'.upper().isupper()
False
>>> 

Returns true for following cases:
isalpha()   -letters only
isalnum()   -letters and number only
isdecimal() -numbers only
isspace()   -whitespace only
istitle()   -titlecase only

>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> 'hello123'.isalnum()
True
>>> '132'.isdecimal()
True
>>> '       '.isspace()
True
>>> 'hello world!'[5].isspace()
True
>>> 'hello world!'[5]
' '

#If 1st letter of each word is in upper case then istitle() returns true. 
>>> 'This Is Title Case.'.istitle()
True
>>>
>>> 'This is TITle case'.istitle()
False
>>> 

 #startswith()
>>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.startswith('H')
True
>>> 'Hello world!'.startswith('ello')
False

#endswith()
>>> 'Hello world!'.endswith('world!')
True
>>> 'Hello world!'.endswith('world')
False
>>> 

#To join list of strings join() method is used.
>>> ','.join(['cats','rats','bats'])
'cats,rats,bats'
>>> ''.join(['cats','rats','bats'])
'catsratsbats'
>>> ' '.join(['cats','rats','bats'])
'cats rats bats'
>>> '\n\n\n'.join(['cats','rats','bats'])
'cats\n\n\nrats\n\n\nbats'
>>> print('\n\n\n'.join(['cats','rats','bats']))
cats


rats


bats
>>>

#split() method is opposite to join, it splits the individual string based upon the cwhewhite space

>>> 'My name is Alice'.split()
['My', 'name', 'is', 'Alice']
>>>

#we can also split based upon the character we want.
#Here we split on character 'm'
>>> 'My name is Alice'.split('m')
['My na', 'e is Alice']
>>>

#ljust() and rjust():
 ljust() method adds the space padding at the end of the text to make the length equal to mentioned argument.
 rjust()method adds the space padding before the text to make the length equal to mentioned argument.
>>> 'Hello'.ljust(10)
'Hello     '
>>> 'Hello'.rjust(10)
'     Hello'
>>> len('     Hello')
10
>>> 

#We can also add different characters instead of space using 2nd parameter.
ljust() method adds anything instead of space for padding using 2nd parameter at the end of the text to make the length equal to mentioned argument.
rjust()method adds anything instead of space for padding before the text to make the length equal to mentioned argument and to justify the string towards
right.
>>> 'Hello'.ljust(10,'*')
'Hello*****'
>>> 'Hello'.rjust(10,'-')
'-----Hello'
>>>

#center() is used to justify the text at the center:
>>> 'Hello'.center(20)
'       Hello    
>>> 'Hello'.center(20,'*')
'*******Hello********'
>>>

#To remove the space from right, left or both side rstrip(), lstrip(), strip() methods are used.

>>> 
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.rjust(10).lstrip()
'Hello'
>>> spam = 'Hello'.rjust(10)
>>> spam.lstrip()
'Hello'
>>> 

>>> sapm = '    Hello      '
>>> spam.strip()
'Hello'
>>>

>>> spam = 'Hello           '

#We can also remove the characters from end of the text using second argument:
>>> 'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS')
'BaconSpamEggs'
>>> 'SpamSpamBaconSpamEggsSpamSpam'.strip('amp')
'SpamSpamBaconSpamEggsSpamS'
>>> 'SpamSpamBaconSpamEggsSpamSpam'.strip('a')
'SpamSpamBaconSpamEggsSpamSpam'
>>> 

#replace(string which to be replace, replacement string):
>>> 
>>> spam = 'Hello Their!'
>>> spam.replace('e','xyz')
'Hxyzllo Thxyzir!'
>>> 
