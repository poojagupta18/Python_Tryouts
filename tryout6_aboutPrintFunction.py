#print() function has keyword argument end and sep
#print() function automatically adds the newline after printing the string closed in it.
#Example:

print('Hello')
print('World')

#Output:
#Hello
#World

#---------------------------

#If we don't want to print it on new line, we can use end argument
print('Hello',end = '')
print('World')

#Output:
#HelloWorld

#----------------------------

#We can pass multiple argument to print function, it will seperate out the different arguments using space
print('Hi','good','morning')

#output:
#Hi good morning

#We can change the seperator ie space with anything we want
print('Hi','good','morning',sep = '###')

#output:
#Hi###good###morning
