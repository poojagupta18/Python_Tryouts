#for loop iterates specific number of times.
print('Working of range() with one argument')
for i in range (5):								#This for loop iterates 5 times for the value of i=0 to i=4(always excludes the number written in range())
    print('hello world ' + str(i) + ' time.' )
 
#To understand range() with two argument
print('Working of range() with two argument')    
for i in range (12,15):               #This loop iterates from i=12 to i=14 (iterates upto 15 but does not include 15)
	print('Number is ' + str(i))

#To understand range() with three argumnets range(start,end,step)
#Here steps means increment/decrement to start.Step can be +ve or -ve
print('Working of range() with three argument')
for i in range (0,10,2):               #This loop iterates from i=12 to i=14 (iterates upto 15 but does not include 15)
	print('Number is ' + str(i))

	
	
	
