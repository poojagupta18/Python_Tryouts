#try except in python is used to handle the exception

#Lets consider the code
#Before exception handling
#Here program causes crash after print(divide(0))
def divide(number):
    return 24/number;

print(divide(12));
print(divide(3));
print(divide(5));
#print(divide(0));    commented for working of after part
print(divide(2));

"""Output:
2.0
8.0
4.8
Traceback (most recent call last):
  File "G:/pooja_tryouts/python_tryout/tryout8_tryExcept.py", line 12, in <module>
    print(divide(0));
  File "G:/pooja_tryouts/python_tryout/tryout8_tryExcept.py", line 7, in divide
    return 24/number;
ZeroDivisionError: division by zero"""

#As it will print for 3 function calls,for fourth it will throw error 'ZeroDivisionError' as computer dont know to handle divide by zero.
#After try except

def divide(number):
    try:
        return 24/number
    except ZeroDivisionError:             #you can also write as except: if you dont know exception type
        print('You have entered zero...')

print(divide(12));
print(divide(3));
print(divide(5));
print(divide(0));
print(divide(2));

"""Output:
2.0
8.0
4.8
You have entered zero...
None
12.0"""
