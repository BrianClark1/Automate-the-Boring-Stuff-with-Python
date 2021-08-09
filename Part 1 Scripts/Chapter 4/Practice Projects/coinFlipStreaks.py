import random #Import the random module for randint
from itertools import groupby

numberOfStreaks = 0 #Intialize the 6 in a row streak counter
count = 0 #Intialize counter
flipList = [] #Create 100 Flip list
realNumberOfStreaks = 0
for experimentNumber in range(10000):
    #Code that creates list of 100 'heads' or 'tails' values.
    count = 0
    flipList = []
    while count < 101:
         entry = random.randint(0,1)
         count = count + 1
         flipList.append(entry)
         
       
    
    #Code that checks if there is a streak of 6 heads or tails in a row.
    counterOne = 0
    counterZero = 0
    numberOfStreaks = 0
    
    lastItem = -1
    for item in flipList:    
        if item == NewItem:
            counterZero = counterZero + 1
            if counterZero >=6:
                numberOfStreaks = numberOfStreaks + 1
                NewItem = -1
        elif NewItem=-1
            
        else
            NewItem = item
            counterZero = 0
        
        else
            counterZero = 0
        
        if item == 0:
             counterZero = counterZero + 1
        elif counterZero >=6:
            numberOfStreaks = numberOfStreaks +1
            counterZero = 0
            
        if item == 1:
             counterOne = counterOne + 1
        elif counterZero >=6:
            numberOfStreaks = numberOfStreaks + 1
            counterOne = 0
            
    print(numberOfStreaks)
    realNumberOfStreaks = realNumberOfStreaks + numberOfStreaks
        
print(realNumberOfStreaks)
print(realNumberOfStreaks / 10000)
print('Chance of streak: %s%%' % (100*(realNumberOfStreaks / 10000  )))
print('Chance of streak: %s%%' % (numberOfStreaks / 10000  ))

