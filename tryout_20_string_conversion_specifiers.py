#This tryout is about string formatting:
    
>>> 'hello'+' world'
'hello world'
>>> name = 'Alex'
>>> place = 'main street'
>>> time = 6pm
SyntaxError: invalid syntax
>>> time = '6pm'
>>> food = 'turnips'
>>> 'Hello'+ name +', you are invited to a perty at '+ place +' at time '+time+'.Plase bring '+ food + '.'
'HelloAlex, you are invited to a perty at main street at time 6pm.Plase bring turnips.'

#String formatting can be used to make the above sentence easier.

>>> 'Hello %s, you are invited to a party at %s at time %s. Please bring %s' %(name, place, time, food)
'Hello Alex, you are invited to a party at main street at time 6pm. Please bring turnips'
>>>

#% (name, place, time, food) are called conversion specifiers.
