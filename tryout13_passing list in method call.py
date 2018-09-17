#This tryout is about passing the list in function call.
def eggs(cheese):             #here reference of list spam is copied in cheese
    cheese.append(6)          #though cheese will have scope into this function only,it makes the changes using references so even if cheese get destroyed we are able to see changes in spam.         

spam = [1,2,3,4,5]
eggs(spam)
print(spam)

"""
output:
[1, 2, 3, 4, 5, 6]
>>>
"""
