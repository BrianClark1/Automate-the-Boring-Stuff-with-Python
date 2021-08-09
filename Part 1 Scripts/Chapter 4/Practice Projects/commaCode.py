spam = ['apples' , 'bananas' , 'tofu' , 'cats' ]

def commaCode(spam):
    if len(spam) > 1:
        spam[-1] = "and " + spam[-1]
    elif len(spam) == 1:
        spam[-1] = "and " + spam[-1]
    elif len(spam) == 0:
        print('Please Populate the List')
    print(*spam, sep=", ")
   
commaCode(spam)
