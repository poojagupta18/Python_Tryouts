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


