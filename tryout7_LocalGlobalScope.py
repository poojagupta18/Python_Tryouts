#Understand the local and global scope. Why do we have local and global scopes? if by mistake someone assign bad value to local then we can findout easily
#Local scope- variable written inside the block has local scope
#global scope-Variable written outside the function has global scope

#Local scope
def print_var():
    age = 20        

print_var()
#print(age)          #age is present inside the function, So it is cannot access outside the function

# Output:NameError: name 'age' is not defined-----------------------------

#local variable present in one function cannot be accessed in another local scope
def func1():
    age = 12
    func2()
    #print(name)       name is defined inside the func2. So, it cannot be access outside the func2

def func2():
    name = 'Alice'

func1()

#Output:
#NameError: name 'name' is not defined
    
#Local scope variable can take global scoped variable value-----------
age = 20

def func1():
    print(age)

func1()
#output:
#20

#1st priority is given to local scope then global scope------------
#Trick: For printing.....
#           Assignment statement = local variable
#           No assignment statement = Global variable
age = 22

def func1():
    age = 12
    print(age)      #it will search for age if it is present in same function, it will print that value

func1()
print(age)
    
#Output:
#12
#22

#we can change the global variable value from the local scope---------
def func1():
    global age    
    age = 20;    
#it will refer to global variable age as in previous statement as it is referred as global

age = 40
func1()
print(age)

#output:
#20










    















