#Function returning the value

def onePlus(number):
    return number + 1        #returning number + 1 value to function

new_number = onePlus(4)      #onePlus(4) will be replaced by 5 and get assigned to new_number
print(new_number)

#Output:
#5 

#Every Function has return type. It is not necessary that each function contains the return statement. If function do not return anything then by default it returns 'None'
#print() function prints the value and return the none

spam = print('hello')   #print returns None 

if spam == None:
	print( "True..")
else:
	print("False")

#Output:
#hello
#True
