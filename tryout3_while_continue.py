#Use of continue statement
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:                           #when if condition becomes true continue will be executed.
        continue                            #continue skip the all the statment below it(within the block) and passes control back to loop.
    print('The spam value is ' + str(spam))
