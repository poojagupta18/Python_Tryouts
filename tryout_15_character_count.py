#The program to count the character.

message = 'It was rainy days in June, unfortunatly I forgot my umbrella.'
count = {}

for character in message:
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

#The pprint module's pprint() "pretty print" function can display a dictionary value cleanly.

#The pformat() function returns a string value of this output.
