"""Like List dictionary is collection of many values, unlike list dictories can have indexes of any datatype not only integers.
Key with associated values is called key-value pair

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
"""

