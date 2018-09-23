cat = {'name' : 'Zophie', 'age' : 7, 'colour' : 'blackish'}
>>> allcats = []
>>> allcats.append({'name' : 'Zomba', 'age' : 9, 'colour' : 'black'})
>>> allcats.append({'name' : 'Amka', 'age' : 17, 'colour' : 'gray'})
>>> allcats.append({'name' : 'pussy', 'age' : 7, 'colour' : 'gray'})

#List of dictionaries is called the data structure			
>>> allcats
			
[{'name': 'Zomba', 'age': 9, 'colour': 'black'}, {'name': 'Amka', 'age': 17, 'colour': 'gray'}, {'name': 'pussy', 'age': 7, 'colour': 'gray'}]
>>> 

#Tic-Tac-Toe game

#This tryout doesn't reperesent the whole tic-tac-toe game. But teaches how to form the tic-tac-toe table structure and tic-tac-toe move.

>>> theBoard = {}
			
>>> theBoard = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ', 'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ', 'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '}
			
>>> theBoard
			
{'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
>>> import pprint
			
>>> pprint.pprint(theBoard)
			
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> 
#python dosen't consider as tic-tac-toe X or 0 move but consider as dictionary of keys-values pair.
#Let's take 1st move at the centre
>>> theBoard['mid-M'] = 'X'
			
>>> pprint.pprint(theBoard)
			
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': 'X',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>>

			
>>> theBoard['top-L'] = '0'
			
>>> theBoard['top-M'] = '0'
			
>>> theBoard['top-R'] = ' '
			
>>> theBoard['mid-L'] = 'X'
			
>>> theBoard['low-L'] = 'X'

>>> pprint.pprint(theBoard)
			
{'low-L': 'X',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': 'X',
 'mid-M': 'X',
 'mid-R': ' ',
 'top-L': '0',
 'top-M': '0',
 'top-R': ' '}
>>>
#To drew the table, function is defined which takes the move dictionary as parameter

>>> 
			
>>> def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-----')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

			
>>> printBoard(theBoard)
			
0|0| 
-----
X|X| 
-----
X| | 
>>> 



