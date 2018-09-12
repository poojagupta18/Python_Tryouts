#Code before exception handling. See the output for more understanding.
def catCount(number):
    if int(number) >= 4:
        print('cat count '+ number +' is not acceptable')
    else:
        print('cat count '+ number +' is acceptable')

print('Before:')
print('Enter the number:')
number = input()          #user can enter any value like 6, six but six is not appropriate as it cannot covert to int using int('six')
catCount(number)

"""==== RESTART: G:/pooja_tryouts/python_tryout/tryout8_tryExcept_example.py ====
Enter the number:
5
cat count 5 is not acceptable
>>> 
>>> 
==== RESTART: G:/pooja_tryouts/python_tryout/tryout8_tryExcept_example.py ====
Enter the number:
six
Traceback (most recent call last):
  File "G:/pooja_tryouts/python_tryout/tryout8_tryExcept_example.py", line 9, in <module>
    catCount(number)
  File "G:/pooja_tryouts/python_tryout/tryout8_tryExcept_example.py", line 2, in catCount
    if int(number) >= 4:
ValueError: invalid literal for int() with base 10: 'six' """

#Code after exception handling

def catCount(number):
    try:
        if int(number) >= 4:
            print('cat count '+ number +' is not acceptable')
        else:
            print('cat count '+ number +' is acceptable')
    except:
        print('Wrong input....You have not entered the number properly....')

print('After:')
print('Enter the number:')
number = input()          
catCount(number)
