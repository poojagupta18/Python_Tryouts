# ilef

name = 'Bob'
age = 13

if name == 'Alice':
    print('Hi Alice')
elif age < 18:
    print('You are not elligible for voting')    
elif age > 18:
    print('You are eligible for voting')
elif age < 18 and name == 'Bob':
    print('You are not elligible for voting ' + name)

#wherever it gets first true condition it will skip all the elif after it.
