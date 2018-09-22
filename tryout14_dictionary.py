"""Like List dictionary is collection of many values, unlike list dictories can have indexes of any datatype not only integers.
Key with associated values is called key-value pair
Dictionaries are mutable. Variables hold references to dictionary values, not the dictionary value itself.

Dictionaries are represented using {}

>>> myCat = { 'size': 'fatty', 'colour':'brown', 'disposition':'loud'}
>>> mycat
>>> myCat['size']
'fatty'
>>> myCat['colour']
'brown'
>>> myCat['disposition']
'loud'
>>> 'My cat has '+myCat['colour']+' fur.'
'My cat has brown fur.'
>>> spam = {123: 'Luggage combination', 432: 'Answer key'}
>>> spam[123]
'Luggage combination'
>>> spam[432]
'Answer key'

list are ordered.

>>> [1, 2, 3] == [2, 3, 1]
False

Dictionaries are un-ordered

>>> {'A' : 'apple', 'B' : 'Bat', 'C' : 'Cat'} == { 'B' : 'Bat', 'C' : 'Cat', 'A': 'apple'}
True

If index is not present:
>>> myCat['food']
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    myCat['food']
KeyError: 'food'


>>>

In and not in operator:
>>> myCat = { 'size': 'fatty', 'colour':'brown', 'disposition':'loud'}
>>> 'size' in myCat
True
>>> 'size' not in myCat
False
>>>

keys(), values(), item()
>>> list(myCat.keys())
['size', 'colour', 'disposition']
>>> list(myCat.values())
['fatty', 'brown', 'loud']
>>> list(myCat.items())
[('size', 'fatty'), ('colour', 'brown'), ('disposition', 'loud')]
>>> myCat.keys()
dict_keys(['size', 'colour', 'disposition'])
>>> 

alphabet = {'A' : 'apple', 'B' : 'bat', 'C' : 'cat', 'D' : 'dog'}
>>> alphabet
{'A': 'apple', 'B': 'bat', 'C': 'cat', 'D': 'dog'}

To print key in aplhabet dictionary
>>> for k in alphabet.keys():   
	print(k)

	
A
B
C
D

To print values in alphabet dictionary
>>> for v in alphabet.values():
	print(v)

	
apple
bat
cat
dog

item returns key value. If we print k and v it will show output like:
>>> for k, v in alphabet.items():
	print(k, v)

	
A apple
B bat
C cat
D dog

If we print like this(print only one value in for), it will return tupple:

>>> for i in alphabet.items():
	print(i)

	
('A', 'apple')
('B', 'bat')
('C', 'cat')
('D', 'dog')

If we try to find value of key which is not present in dictory, it will throw key error.
>>> alphabet
{'A': 'apple', 'B': 'bat', 'C': 'cat', 'D': 'dog'}
>>> alphabet['A']
'apple'
>>> alphabet['E']
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    alphabet['E']
KeyError: 'E'

If is not efficient every time, as it supresses the error, so get() method is used
>>> if 'E' in alphabet:
	print(alphabet['E'])

	
>>>
get() method takes two arguments, first value is true key value and 2nd argument is default value that will be printed when
true key value is not present.

>>> alphabet
{'A': 'apple', 'B': 'bat', 'C': 'cat', 'D': 'dog'}
>>> alphabet.get('D', 0)
'dog'

As Key E is not present in dictionary, 2nd argument will be displayed:
>>> alphabet.get('E','Default value if key E is not present in dictionary')
'Default value if key E is not present in dictionary'

get() method is handy for creating the sentences like:
>>> picnicItems = {'apples':5, 'cups':2}
>>> print('I am bringing '+str(picnicItems.get('napkin', 0))+' to the picnic')
I am bringing 0 to the picnic
>>> 
>>> 

>>> eggs = {'name' : 'zophie', 'species' : 'cat', 'age' : 8}
>>> eggs
{'name': 'zophie', 'species': 'cat', 'age': 8}
>>> if 'colour' not in eggs:
	eggs['colour'] = 'black'

	
>>> eggs
{'name': 'zophie', 'species': 'cat', 'age': 8, 'colour': 'black'}
>>>

we can do this in one line using setDefault() method
setdefault() method takes two arguments 1st argument is key and 2nd argument is value
>>> eggs.setdefault('property','self')
'self'
>>> eggs
{'name': 'zophie', 'species': 'cat', 'age': 8, 'colour': 'black', 'property': 'self'}
>>>
>>> eggs.setdefault('colour','orange')
'black'
>>> eggs
{'name': 'zophie', 'species': 'cat', 'age': 8, 'colour': 'black', 'property': 'self'}
>>> 
setdefault() can't change the value of key which already exist. It 1st check whether that key is present or not, if key is present it will returns its value, if key doesn't exist it will set that key in dictionary.
































"""

